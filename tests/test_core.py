"""
TEKNOFEST 2025 — Elite Command Center
Unit Tests for Core Logic
"""

import unittest
from src.analysis.resilience_analyzer import ResilienceAnalyzer, ClinicalScores, ResilienceCategory
from src.models.ews import EarlyWarningSystem, RiskLevel, BehavioralFlags
from src.utils.security import anonymize_id, sanitize_text


class TestResilienceAnalyzer(unittest.TestCase):
    def setUp(self):
        self.analyzer = ResilienceAnalyzer()

    def test_healthy_person(self):
        scores = ClinicalScores(phq9=2, gad7=2, pss10=5, cd_risc=90)
        result = self.analyzer.analyze(scores)
        self.assertGreater(result.composite_score, 80)
        self.assertEqual(result.category, ResilienceCategory.EXCEPTIONAL)

    def test_distressed_person(self):
        scores = ClinicalScores(phq9=20, gad7=18, pss10=35, cd_risc=20)
        result = self.analyzer.analyze(scores)
        self.assertLess(result.composite_score, 30)
        self.assertIn(result.category, [ResilienceCategory.CRITICAL, ResilienceCategory.LOW])


class TestEarlyWarningSystem(unittest.TestCase):
    def setUp(self):
        self.ews = EarlyWarningSystem()

    def test_critical_risk_override(self):
        # Even with good resilience, hopelessness should trigger critical/high risk
        behavioral = BehavioralFlags(hopelessness_reported=True)
        result = self.ews.assess(
            resilience_score=85,
            phq9=5,
            gad7=5,
            sentiment_negativity=0.1,
            behavioral=behavioral
        )
        self.assertEqual(result.risk_level, RiskLevel.CRITICAL)

    def test_low_risk(self):
        result = self.ews.assess(
            resilience_score=90,
            phq9=2,
            gad7=2,
            sentiment_negativity=0.05
        )
        self.assertEqual(result.risk_level, RiskLevel.LOW)


class TestSecurityUtils(unittest.TestCase):
    def test_anonymization(self):
        user_id = "test_user_123"
        anon1 = anonymize_id(user_id)
        anon2 = anonymize_id(user_id)
        self.assertEqual(anon1, anon2)
        self.assertNotEqual(user_id, anon1)
        self.assertEqual(len(anon1), 16)

    def test_pii_sanitization(self):
        raw_text = "Benim numaram 0532 123 45 67, mailim test@test.com"
        clean = sanitize_text(raw_text)
        self.assertIn("[PHONE]", clean)
        self.assertIn("[EMAIL]", clean)
        self.assertNotIn("0532", clean)
        self.assertNotIn("test@test.com", clean)


if __name__ == "__main__":
    unittest.main()
