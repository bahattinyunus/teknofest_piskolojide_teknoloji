"""
TEKNOFEST 2025 — Elite Command Center
Early Warning System (EWS)

Implements a multi-signal risk detection engine that combines:
  - Clinical scale scores (from ResilienceAnalyzer)
  - NLP sentiment signal (from NLPEngine)
  - Behavioral pattern flags

Risk levels: LOW / MEDIUM / HIGH / CRITICAL
"""

from dataclasses import dataclass
from enum import Enum
from typing import Optional

from src.utils.logger import get_logger

logger = get_logger("ews")


class RiskLevel(str, Enum):
    LOW      = "DÜŞÜK"
    MEDIUM   = "ORTA"
    HIGH     = "YÜKSEK"
    CRITICAL = "KRİTİK"


@dataclass
class BehavioralFlags:
    """Behavioral signals that can elevate risk independently of scale scores."""
    sleep_disruption:     bool = False   # Uyku bozukluğu bildirimi
    social_withdrawal:    bool = False   # Sosyal geri çekilme
    appetite_change:      bool = False   # Belirgin iştah değişimi
    concentration_loss:   bool = False   # Konsantrasyon güçlüğü
    hopelessness_reported: bool = False  # Umutsuzluk ifadesi (kritik sinyal)


@dataclass
class EWSResult:
    risk_level: RiskLevel
    risk_score: float             # 0.0 – 1.0 normalized risk
    triggered_signals: list[str]  # Human-readable list of active risk signals
    action_required: bool
    alert_message: str
    next_check_days: int          # Recommended follow-up interval


class EarlyWarningSystem:
    """
    Multi-signal early warning engine for psychological risk detection.

    Combines:
      - Composite resilience score (40% weight)
      - NLP sentiment negativity (25% weight)
      - Clinical scale thresholds (20% weight)
      - Behavioral flags (15% weight)
    """

    # Weights for composite risk calculation
    WEIGHTS = {
        "resilience": 0.40,
        "sentiment":  0.25,
        "clinical":   0.20,
        "behavioral": 0.15,
    }

    # Thresholds for risk classification (0.0–1.0)
    THRESHOLDS = {
        RiskLevel.LOW:      0.25,
        RiskLevel.MEDIUM:   0.50,
        RiskLevel.HIGH:     0.75,
        RiskLevel.CRITICAL: 0.90,
    }

    def assess(
        self,
        resilience_score: float,      # 0–100 (higher = better → invert for risk)
        phq9: float,
        gad7: float,
        sentiment_negativity: float,  # 0.0–1.0 (from NLP engine)
        behavioral: Optional[BehavioralFlags] = None,
    ) -> EWSResult:
        """
        Runs the full EWS assessment pipeline.

        Args:
            resilience_score: Composite resilience score (0–100).
            phq9: PHQ-9 raw score (0–27).
            gad7: GAD-7 raw score (0–21).
            sentiment_negativity: Negative sentiment probability from NLP (0–1).
            behavioral: Optional behavioral flags.

        Returns:
            EWSResult with risk level, score, signals, and recommendations.
        """
        if behavioral is None:
            behavioral = BehavioralFlags()

        signals = []

        # --- Component 1: Resilience (inverted) ---
        resilience_risk = (100 - resilience_score) / 100
        if resilience_score < 40:
            signals.append(f"Düşük psikolojik dayanıklılık skoru: {resilience_score:.1f}/100")

        # --- Component 2: Sentiment negativity ---
        sentiment_risk = sentiment_negativity
        if sentiment_negativity > 0.65:
            signals.append(f"Yüksek negatif duygu yoğunluğu (NLP): {sentiment_negativity:.0%}")

        # --- Component 3: Clinical scale thresholds ---
        clinical_risk = 0.0
        if phq9 >= 15:
            clinical_risk = max(clinical_risk, 0.85)
            signals.append(f"PHQ-9 orta-şiddetli depresyon eşiği aşıldı: {phq9}/27")
        elif phq9 >= 10:
            clinical_risk = max(clinical_risk, 0.55)
            signals.append(f"PHQ-9 orta depresyon belirtisi: {phq9}/27")
        if gad7 >= 15:
            clinical_risk = max(clinical_risk, 0.80)
            signals.append(f"GAD-7 şiddetli anksiyete eşiği aşıldı: {gad7}/21")
        elif gad7 >= 10:
            clinical_risk = max(clinical_risk, 0.50)
            signals.append(f"GAD-7 orta anksiyete belirtisi: {gad7}/21")

        # --- Component 4: Behavioral flags ---
        flag_count = sum([
            behavioral.sleep_disruption,
            behavioral.social_withdrawal,
            behavioral.appetite_change,
            behavioral.concentration_loss,
        ])
        behavioral_risk = flag_count / 4

        if behavioral.hopelessness_reported:
            behavioral_risk = 1.0  # Immediate override to maximum
            signals.append("⚠️ Umutsuzluk ifadesi tespit edildi — Acil Müdahale Gerekli")

        if behavioral.sleep_disruption:
            signals.append("Uyku bozukluğu bildirimi")
        if behavioral.social_withdrawal:
            signals.append("Sosyal geri çekilme örüntüsü")
        if behavioral.concentration_loss:
            signals.append("Konsantrasyon güçlüğü")

        # --- Composite risk score ---
        composite = (
            self.WEIGHTS["resilience"] * resilience_risk +
            self.WEIGHTS["sentiment"]  * sentiment_risk +
            self.WEIGHTS["clinical"]   * clinical_risk +
            self.WEIGHTS["behavioral"] * behavioral_risk
        )
        composite = round(min(composite, 1.0), 4)

        risk_level = self._classify(composite)
        alert_msg  = self._compose_alert(risk_level, signals)
        next_check = self._next_check_interval(risk_level)

        logger.warning(f"EWS result | Risk: {risk_level.value} | Score: {composite:.3f}")

        return EWSResult(
            risk_level=risk_level,
            risk_score=composite,
            triggered_signals=signals,
            action_required=risk_level in (RiskLevel.HIGH, RiskLevel.CRITICAL),
            alert_message=alert_msg,
            next_check_days=next_check,
        )

    def _classify(self, score: float) -> RiskLevel:
        if score >= self.THRESHOLDS[RiskLevel.CRITICAL]:
            return RiskLevel.CRITICAL
        elif score >= self.THRESHOLDS[RiskLevel.HIGH]:
            return RiskLevel.HIGH
        elif score >= self.THRESHOLDS[RiskLevel.MEDIUM]:
            return RiskLevel.MEDIUM
        return RiskLevel.LOW

    def _compose_alert(self, level: RiskLevel, signals: list[str]) -> str:
        headers = {
            RiskLevel.LOW:      "✅ Risk düşük. Rutin takip önerilir.",
            RiskLevel.MEDIUM:   "⚠️ Orta risk tespit edildi. DTx müdahale modülleri başlatıldı.",
            RiskLevel.HIGH:     "🔴 Yüksek risk! Kullanıcıya destek kaynakları yönlendirilmeli.",
            RiskLevel.CRITICAL: "🚨 KRİTİK RİSK! Uzman bildirimi gönderiliyor. Acil müdahale gerekli.",
        }
        signal_text = "\n  — ".join(signals) if signals else "Aktif sinyal bulunamadı."
        return f"{headers[level]}\nAktif Sinyaller:\n  — {signal_text}"

    def _next_check_interval(self, level: RiskLevel) -> int:
        return {
            RiskLevel.LOW:      30,
            RiskLevel.MEDIUM:   14,
            RiskLevel.HIGH:     3,
            RiskLevel.CRITICAL: 1,
        }[level]
