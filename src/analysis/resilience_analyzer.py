"""
TEKNOFEST 2025 — Elite Command Center
Resilience Score Calculator

Implements a composite psychological resilience scoring system
based on validated clinical scales:
  - PHQ-9  (Patient Health Questionnaire - Depression)
  - GAD-7  (Generalized Anxiety Disorder)
  - PSS-10 (Perceived Stress Scale)
  - CD-RISC (Connor-Davidson Resilience Scale)
"""

from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

from src.utils.logger import get_logger
from src.utils.security import validate_score

logger = get_logger("resilience")


class ResilienceCategory(str, Enum):
    CRITICAL = "KRİTİK"
    LOW = "DÜŞÜK"
    MODERATE = "ORTA"
    HIGH = "YÜKSEK"
    EXCEPTIONAL = "ÜSTÜN"


@dataclass
class ClinicalScores:
    """
    Container for validated psychometric scale scores.
    All scores are float values in their native clinical ranges.
    """
    phq9:    float   # Range 0–27  (PHQ-9 Depression)
    gad7:    float   # Range 0–21  (GAD-7 Anxiety)
    pss10:   float   # Range 0–40  (PSS-10 Stress)
    cd_risc: float   # Range 0–100 (Connor-Davidson — higher is better)
    notes:   Optional[str] = field(default=None)

    def validate(self) -> "ClinicalScores":
        self.phq9    = validate_score(self.phq9,    "PHQ-9",   0, 27)
        self.gad7    = validate_score(self.gad7,    "GAD-7",   0, 21)
        self.pss10   = validate_score(self.pss10,   "PSS-10",  0, 40)
        self.cd_risc = validate_score(self.cd_risc, "CD-RISC", 0, 100)
        return self


@dataclass
class ResilienceResult:
    composite_score: float
    category: ResilienceCategory
    phq9_normalized: float
    gad7_normalized: float
    pss10_normalized: float
    cd_risc_normalized: float
    interpretation: str
    recommendations: list[str]


class ResilienceAnalyzer:
    """
    Calculates a composite psikolojik dayanıklılık (resilience) score
    by normalizing and weighting validated clinical scale scores.

    Weights (configurable via settings.yaml):
        PHQ-9  : 30% (depression impact on resilience)
        GAD-7  : 25% (anxiety burden)
        PSS-10 : 20% (perceived stress load)
        CD-RISC: 25% (direct resilience capacity)
    """

    # Scale weights (sum to 1.0)
    WEIGHTS = {
        "phq9":    0.30,
        "gad7":    0.25,
        "pss10":   0.20,
        "cd_risc": 0.25,
    }

    # Category thresholds (0–100 composite)
    THRESHOLDS = {
        ResilienceCategory.CRITICAL:    (0,  20),
        ResilienceCategory.LOW:         (20, 40),
        ResilienceCategory.MODERATE:    (40, 60),
        ResilienceCategory.HIGH:        (60, 80),
        ResilienceCategory.EXCEPTIONAL: (80, 100),
    }

    def analyze(self, scores: ClinicalScores) -> ResilienceResult:
        """
        Runs the full resilience analysis pipeline.

        Args:
            scores: Validated ClinicalScores instance.

        Returns:
            ResilienceResult with composite score, category, and recommendations.
        """
        scores.validate()

        # Normalize each scale to 0–100 (invert burden scales so higher = better)
        phq9_n    = (1 - scores.phq9 / 27)    * 100
        gad7_n    = (1 - scores.gad7 / 21)    * 100
        pss10_n   = (1 - scores.pss10 / 40)   * 100
        cd_risc_n = scores.cd_risc  # already 0–100, higher = better

        composite = (
            self.WEIGHTS["phq9"]    * phq9_n    +
            self.WEIGHTS["gad7"]    * gad7_n    +
            self.WEIGHTS["pss10"]   * pss10_n   +
            self.WEIGHTS["cd_risc"] * cd_risc_n
        )

        category = self._classify(composite)
        interpretation = self._interpret(category, scores)
        recommendations = self._recommend(category, scores)

        logger.info(
            f"Resilience analysis complete | Score: {composite:.1f} | Category: {category.value}"
        )

        return ResilienceResult(
            composite_score=round(composite, 2),
            category=category,
            phq9_normalized=round(phq9_n, 2),
            gad7_normalized=round(gad7_n, 2),
            pss10_normalized=round(pss10_n, 2),
            cd_risc_normalized=round(cd_risc_n, 2),
            interpretation=interpretation,
            recommendations=recommendations,
        )

    def _classify(self, score: float) -> ResilienceCategory:
        for category, (low, high) in self.THRESHOLDS.items():
            if low <= score < high:
                return category
        return ResilienceCategory.EXCEPTIONAL

    def _interpret(self, category: ResilienceCategory, scores: ClinicalScores) -> str:
        base = {
            ResilienceCategory.CRITICAL:    "Kritik düzeyde psikolojik yük tespit edildi. Acil profesyonel destek önerilir.",
            ResilienceCategory.LOW:         "Psikolojik dayanıklılık düşük. Stres yönetimi ve destek programlarına katılım faydalı olacaktır.",
            ResilienceCategory.MODERATE:    "Orta düzeyde dayanıklılık. Koruyucu faktörleri güçlendirmeye yönelik müdahaleler planlanabilir.",
            ResilienceCategory.HIGH:        "Psikolojik dayanıklılık yüksek. Mevcut başa çıkma stratejileri etkili görünmektedir.",
            ResilienceCategory.EXCEPTIONAL: "Üstün düzeyde dayanıklılık. Bireysel güçler ön plana çıkmaktadır.",
        }
        return base[category]

    def _recommend(self, category: ResilienceCategory, scores: ClinicalScores) -> list[str]:
        recs = []
        if scores.phq9 >= 10:
            recs.append("Depresyon belirtileri klinik eşiğin üzerinde — PHQ-9 takibi ve klinisyen konsültasyonu önerilir.")
        if scores.gad7 >= 10:
            recs.append("Anksiyete yükü orta-yüksek düzeyde — BDT tabanlı nefes & bilişsel yeniden yapılandırma egzersizleri başlatılsın.")
        if scores.pss10 >= 27:
            recs.append("Algılanan stres yüksek — mindfulness ve zaman yönetimi modülleri önceliklendirilsin.")
        if scores.cd_risc < 50:
            recs.append("Dayanıklılık kapasitesi geliştirilmeli — PERMA modeli tabanlı güçlü yanlar egzersizleri önerilir.")
        if not recs:
            recs.append("Mevcut başa çıkma ve dayanıklılık stratejilerine devam edin. Periyodik takip sürdürülsün.")
        return recs
