"""
TEKNOFEST 2025 — Elite Command Center
NLP Sentiment Analysis Engine

Analyzes free-text input to extract:
  - Sentiment (positive / neutral / negative)
  - Negativity probability (used by EWS)
  - Detected emotional keywords (Turkish)

Primary: savasy/bert-base-turkish-sentiment-cased (HuggingFace)
Fallback: Turkish sentiment lexicon (no-dependency offline mode)
"""

import re
from dataclasses import dataclass
from typing import Optional

from src.utils.logger import get_logger
from src.utils.security import sanitize_text

logger = get_logger("nlp_engine")


@dataclass
class SentimentResult:
    label: str                      # "positive", "neutral", "negative"
    negativity_score: float         # 0.0–1.0 (used by EWS)
    positivity_score: float         # 0.0–1.0
    confidence: float               # Model confidence
    detected_keywords: list[str]    # Flagged emotional words
    engine_used: str                # "transformer" or "lexicon"
    sanitized_input: str            # PII-removed version of input


# ---------------------------------------------------------------------------
# Turkish Sentiment Lexicon (Offline fallback)
# Sources: Turkish sentiment word lists from academic NLP corpora
# ---------------------------------------------------------------------------
NEGATIVE_KEYWORDS = [
    "yorgun", "tükenmiş", "bezgin", "mutsuz", "depresif", "kaygılı",
    "endişeli", "stresli", "bunaltıcı", "umutsuz", "çaresiz", "yalnız",
    "ağlamak", "sıkıntı", "korku", "panik", "gergin", "sinirli",
    "öfkeli", "hayal kırıklığı", "değersiz", "başarısız", "rezil",
    "nefret", "acı", "ıstırap", "acımasız", "bunaldım", "dayanamıyorum",
    "anlamsız", "kötü", "berbat", "iğrenç", "dehşet", "korkunç",
    "uykusuz", "iştahsız", "keyifsiz", "bitkin", "çökmüş", "yalnızlık",
    "karanlık", "boşluk", "ölüm", "intihar", "zarar", "nefret",
]

POSITIVE_KEYWORDS = [
    "mutlu", "neşeli", "huzurlu", "güçlü", "umutlu", "başarılı",
    "enerjik", "motive", "teşekkür", "sevgi", "minnettarlık", "güzel",
    "harika", "mükemmel", "olağanüstü", "verimli", "odaklı", "dinlendim",
    "rahatladım", "memnun", "tatmin", "coşkulu", "ilham", "keyif",
    "iyiyim", "süper", "heyecanlı", "başarı", "seviniyorum", "güven",
]

CRITICAL_FLAGS = [
    "intihar", "kendime zarar", "yaşamak istemiyorum", "ölmek istiyorum",
    "hayatıma son", "bitirmek istiyorum", "kendimi öldürmek", "ölsem daha iyi",
    "canıma kıymak", "vazgeçtim hayattan",
]


class NLPEngine:
    """
    Dual-mode NLP sentiment analysis engine.

    Mode 1 (transformer): Uses HuggingFace Turkish BERT model.
    Mode 2 (lexicon): Falls back to keyword-based scoring if transformers
                      library is not installed or model unavailable.
    """

    def __init__(self, use_transformer: bool = True):
        self._pipeline = None
        self._engine = "lexicon"

        if use_transformer:
            self._load_transformer()

    def _load_transformer(self):
        try:
            from transformers import pipeline
            logger.info("Loading Turkish BERT sentiment model...")
            self._pipeline = pipeline(
                "sentiment-analysis",
                model="savasy/bert-base-turkish-sentiment-cased",
                top_k=None,
            )
            self._engine = "transformer"
            logger.info("Transformer model loaded successfully.")
        except Exception as e:
            logger.warning(f"Transformer model unavailable, falling back to lexicon: {e}")
            self._engine = "lexicon"

    def analyze(self, text: str) -> SentimentResult:
        """
        Analyzes sentiment of the given Turkish text.

        Args:
            text: Raw user text input (will be sanitized internally).

        Returns:
            SentimentResult with sentiment label, scores, and flagged keywords.
        """
        clean_text = sanitize_text(text)

        # --- Critical keyword override (safety) ---
        for flag in CRITICAL_FLAGS:
            if flag.lower() in clean_text.lower():
                logger.critical(f"CRITICAL SAFETY FLAG detected in input: '{flag}'")
                return SentimentResult(
                    label="negative",
                    negativity_score=1.0,
                    positivity_score=0.0,
                    confidence=1.0,
                    detected_keywords=[flag],
                    engine_used="safety_override",
                    sanitized_input=clean_text,
                )

        if self._engine == "transformer" and self._pipeline:
            return self._analyze_transformer(clean_text)
        return self._analyze_lexicon(clean_text)

    def _analyze_transformer(self, text: str) -> SentimentResult:
        try:
            result = self._pipeline(text[:512])[0]  # Truncate to BERT max
            scores = {item["label"].lower(): item["score"] for item in result}

            neg = scores.get("negative", scores.get("negatif", 0.0))
            pos = scores.get("positive", scores.get("pozitif", 0.0))
            label = "negative" if neg > 0.5 else ("positive" if pos > 0.5 else "neutral")
            keywords = self._extract_keywords(text)

            return SentimentResult(
                label=label,
                negativity_score=round(neg, 4),
                positivity_score=round(pos, 4),
                confidence=round(max(neg, pos), 4),
                detected_keywords=keywords,
                engine_used="transformer",
                sanitized_input=text,
            )
        except Exception as e:
            logger.error(f"Transformer inference failed: {e}. Falling back to lexicon.")
            return self._analyze_lexicon(text)

    def _analyze_lexicon(self, text: str) -> SentimentResult:
        words = re.findall(r'\b\w+\b', text.lower())
        neg_hits = []
        pos_hits = []

        # Simple negation handling
        negators = ["değil", "yok", "hiç", "asla"]
        
        for i, word in enumerate(words):
            is_negated = False
            # Check previous word for negation
            if i > 0 and words[i-1] in negators:
                is_negated = True
            
            if word in NEGATIVE_KEYWORDS:
                if is_negated:
                    pos_hits.append(f"NOT_{word}") # Negated negative is positive
                else:
                    neg_hits.append(word)
            elif word in POSITIVE_KEYWORDS:
                if is_negated:
                    neg_hits.append(f"NOT_{word}") # Negated positive is negative
                else:
                    pos_hits.append(word)

        total = len(neg_hits) + len(pos_hits) + 1e-9
        neg_score = len(neg_hits) / total
        pos_score = len(pos_hits) / total

        if neg_score > 0.6:
            label = "negative"
        elif pos_score > 0.6:
            label = "positive"
        else:
            label = "neutral"

        return SentimentResult(
            label=label,
            negativity_score=round(neg_score, 4),
            positivity_score=round(pos_score, 4),
            confidence=round(max(neg_score, pos_score), 4),
            detected_keywords=neg_hits + pos_hits,
            engine_used="lexicon",
            sanitized_input=text,
        )

    def _extract_keywords(self, text: str) -> list[str]:
        words = re.findall(r'\b\w+\b', text.lower())
        return [w for w in words if w in NEGATIVE_KEYWORDS or w in POSITIVE_KEYWORDS]
