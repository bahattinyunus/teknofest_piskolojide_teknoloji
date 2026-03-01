"""
TEKNOFEST 2025 — Elite Command Center
Main Orchestrator

Wires together:
  - ResilienceAnalyzer
  - EarlyWarningSystem (EWS)
  - NLPEngine
  - DTxEngine
Runs an interactive CLI demo session.
"""

import json
from src.analysis.resilience_analyzer import ResilienceAnalyzer, ClinicalScores
from src.models.ews import EarlyWarningSystem, BehavioralFlags
from src.models.nlp_engine import NLPEngine
from src.models.dtx_engine import DTxEngine
from src.utils.logger import get_logger
from src.utils.security import anonymize_id

logger = get_logger("main")

BANNER = """
╔══════════════════════════════════════════════════════════════╗
║   🧠  TEKNOFEST 2025 — Psikolojide Teknolojik Uygulamalar   ║
║         Elite Command Center  |  v1.0.0                      ║
║                                                              ║
║   Koruyucu Ruh Sağlığı · Erken Uyarı · Dijital Terapötikler ║
╚══════════════════════════════════════════════════════════════╝
"""


def run_demo():
    """
    Runs a full demo pipeline with mock data to demonstrate all modules.
    """
    print(BANNER)
    logger.info("Elite Command Center starting up...")

    # --- Mock user data ---
    user_id = "demo_user_001"
    anon_id = anonymize_id(user_id)
    logger.info(f"Anonymized user token: {anon_id}")

    mock_clinical = ClinicalScores(
        phq9=14,      # Moderate depression range
        gad7=12,      # Moderate anxiety range
        pss10=30,     # High perceived stress
        cd_risc=42,   # Below average resilience
        notes="Demo session — mock clinical data"
    )

    mock_text = (
        "Bugün çok yorgun ve tükenmiş hissediyorum. "
        "İşler iyi gitmiyor ve stres almak üzereyim. "
        "Ama yine de devam etmeye çalışıyorum."
    )

    mock_behavioral = BehavioralFlags(
        sleep_disruption=True,
        social_withdrawal=False,
        appetite_change=True,
        concentration_loss=True,
        hopelessness_reported=False,
    )

    # ──────────────────────────────────────────────────────────
    # STEP 1: Resilience Analysis
    # ──────────────────────────────────────────────────────────
    print("\n" + "="*60)
    print("📊  ADIM 1: PSİKOLOJİK DAYANIKLILIK ANALİZİ")
    print("="*60)

    resilience = ResilienceAnalyzer()
    r_result = resilience.analyze(mock_clinical)

    print(f"  Kompozit Skor     : {r_result.composite_score:.1f} / 100")
    print(f"  Kategori          : {r_result.category.value}")
    print(f"  Yorum             : {r_result.interpretation}")
    print(f"\n  Alt Skorlar:")
    print(f"    PHQ-9  (norm)   : {r_result.phq9_normalized:.1f}")
    print(f"    GAD-7  (norm)   : {r_result.gad7_normalized:.1f}")
    print(f"    PSS-10 (norm)   : {r_result.pss10_normalized:.1f}")
    print(f"    CD-RISC         : {r_result.cd_risc_normalized:.1f}")
    print(f"\n  Öneriler:")
    for rec in r_result.recommendations:
        print(f"    → {rec}")

    # ──────────────────────────────────────────────────────────
    # STEP 2: NLP Sentiment Analysis
    # ──────────────────────────────────────────────────────────
    print("\n" + "="*60)
    print("💬  ADIM 2: DOĞAL DİL İŞLEME (NLP) ANALİZİ")
    print("="*60)

    nlp = NLPEngine(use_transformer=False)  # Offline mode for demo
    nlp_result = nlp.analyze(mock_text)

    print(f"  Motor             : {nlp_result.engine_used}")
    print(f"  Duygu Etiketi     : {nlp_result.label}")
    print(f"  Negatiflik Skoru  : {nlp_result.negativity_score:.2%}")
    print(f"  Pozitiflik Skoru  : {nlp_result.positivity_score:.2%}")
    print(f"  Tespit Edilen KW  : {', '.join(nlp_result.detected_keywords) or 'Yok'}")

    # ──────────────────────────────────────────────────────────
    # STEP 3: Early Warning System
    # ──────────────────────────────────────────────────────────
    print("\n" + "="*60)
    print("🚨  ADIM 3: ERKEN UYARI SİSTEMİ (EWS)")
    print("="*60)

    ews = EarlyWarningSystem()
    ews_result = ews.assess(
        resilience_score=r_result.composite_score,
        phq9=mock_clinical.phq9,
        gad7=mock_clinical.gad7,
        sentiment_negativity=nlp_result.negativity_score,
        behavioral=mock_behavioral,
    )

    print(f"  Risk Seviyesi     : {ews_result.risk_level.value}")
    print(f"  Risk Skoru        : {ews_result.risk_score:.3f}")
    print(f"  Aksiyon Gerekli   : {'EVET ⚠️' if ews_result.action_required else 'HAYIR ✅'}")
    print(f"  Sonraki Kontrol   : {ews_result.next_check_days} gün içinde")
    print(f"\n  Mesaj:\n  {ews_result.alert_message}")

    # ──────────────────────────────────────────────────────────
    # STEP 4: DTx Session
    # ──────────────────────────────────────────────────────────
    print("\n" + "="*60)
    print("💊  ADIM 4: DİJİTAL TERAPÖTİK OTURUM (DTx)")
    print("="*60)

    dtx = DTxEngine()
    session = dtx.create_session(risk_level=ews_result.risk_level.value)

    print(f"  Mesaj: {session.session_message}")
    print(f"  Kazanılacak Puan  : {session.session_points}")
    print(f"\n  📋 Oturum Egzersizleri:")
    for i, ex in enumerate(session.exercises, 1):
        print(f"\n  [{i}] {ex.title} ({ex.duration_minutes} dk — {ex.points} puan)")
        print(f"       Tür: {ex.exercise_type.value}")
        for j, step in enumerate(ex.instructions, 1):
            print(f"         {j}. {step}")
        if ex.reflection_prompt:
            print(f"       💡 Yansıma: {ex.reflection_prompt}")

    print("\n" + "="*60)
    print("✅  Elite Command Center oturumu tamamlandı.")
    print("="*60 + "\n")
    logger.info("Demo session completed successfully.")


def main():
    run_demo()


if __name__ == "__main__":
    main()
