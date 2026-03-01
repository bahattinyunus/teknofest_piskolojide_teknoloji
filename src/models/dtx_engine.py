"""
TEKNOFEST 2025 — Elite Command Center
Digital Therapeutics (DTx) Engine

Implements evidence-based Cognitive Behavioral Therapy (CBT/BDT)
exercise modules for psychological intervention and skill-building.

Exercise types:
  - Breathing exercises (4-7-8 / Box breathing)
  - Cognitive restructuring prompts
  - Mindfulness exercises
  - Behavioural activation tasks
  - Gratitude journaling
"""

import random
from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

from src.utils.logger import get_logger

logger = get_logger("dtx")


class ExerciseType(str, Enum):
    BREATHING         = "Nefes Egzersizi"
    COGNITIVE_REFRAME = "Bilişsel Yeniden Yapılandırma"
    MINDFULNESS       = "Farkındalık (Mindfulness)"
    BEHAVIORAL        = "Davranışsal Aktivasyon"
    GRATITUDE         = "Minnettarlık Günlüğü"


@dataclass
class DTxExercise:
    exercise_type: ExerciseType
    title: str
    duration_minutes: int
    instructions: list[str]
    reflection_prompt: Optional[str] = None
    points: int = 50


@dataclass
class DTxSession:
    exercises: list[DTxExercise]
    session_points: int
    risk_level_targeted: str
    session_message: str


# ---------------------------------------------------------------------------
# Exercise Library (CBT / BDT evidence-based)
# ---------------------------------------------------------------------------

BREATHING_EXERCISES = [
    DTxExercise(
        exercise_type=ExerciseType.BREATHING,
        title="4-7-8 Nefes Tekniği",
        duration_minutes=5,
        instructions=[
            "Rahat bir pozisyona gelin, sırtınızı düzeltin.",
            "4 saniye boyunca burnunuzdan yavaşça nefes alın.",
            "7 saniye boyunca nefesinizi tutun.",
            "8 saniye boyunca ağzınızdan yavaşça nefes verin.",
            "Bu döngüyü 4 kez tekrarlayın.",
        ],
        reflection_prompt="Egzersiz sonunda bedeninizde nasıl bir değişim hissettiniz?",
        points=40,
    ),
    DTxExercise(
        exercise_type=ExerciseType.BREATHING,
        title="Kutu (Box) Nefes Tekniği",
        duration_minutes=4,
        instructions=[
            "Dik ve rahat bir oturun.",
            "4 saniye nefes alın.",
            "4 saniye nefesinizi tutun.",
            "4 saniye nefes verin.",
            "4 saniye tekrar bekleyin.",
            "Döngüyü 5 kez tekrarlayın.",
        ],
        reflection_prompt="Stres seviyeniz 1-10 arasında nasıl değişti?",
        points=40,
    ),
]

COGNITIVE_EXERCISES = [
    DTxExercise(
        exercise_type=ExerciseType.COGNITIVE_REFRAME,
        title="Düşünce Kaydı",
        duration_minutes=10,
        instructions=[
            "Sizi en çok zorlayan düşünceyi bir cümle olarak yazın.",
            "Bu düşünceyi destekleyen kanıtları listeleyin.",
            "Bu düşünceye karşı gelen kanıtları listeleyin.",
            "Daha dengeli ve gerçekçi bir bakış açısı oluşturun.",
            "Yeni bakış açınızı bir cümle olarak yazın.",
        ],
        reflection_prompt="Yeni bakış açınız sizi nasıl hissettiriyor?",
        points=60,
    ),
    DTxExercise(
        exercise_type=ExerciseType.COGNITIVE_REFRAME,
        title="Felaketleştirmeyle Yüzleşme",
        duration_minutes=8,
        instructions=[
            "Endişelendiğiniz en kötü senaryoyu yazın.",
            "Bu senaryonun gerçekleşme olasılığını 0-100% olarak tahmin edin.",
            "Gerçekleşse bile başa çıkabileceğiniz 3 strateji yazın.",
            "Gerçekçi/olasi senaryoyu yeniden tanımlayın.",
        ],
        reflection_prompt="Kaygı seviyeniz bu egzersiz öncesi ve sonrası nasıl değişti?",
        points=55,
    ),
]

MINDFULNESS_EXERCISES = [
    DTxExercise(
        exercise_type=ExerciseType.MINDFULNESS,
        title="5-4-3-2-1 Duyusal Farkındalık",
        duration_minutes=6,
        instructions=[
            "Gözlerinizi açık bırakın ve etrafınızı inceleyin.",
            "5 şey görün ve zihinsel olarak adlandırın.",
            "4 şeye dokunun (sandalye, kıyafet, yüzey...) ve hislerinizi fark edin.",
            "3 ses duyun ve isimlerini belirleyin.",
            "2 şeyin kokusunu alın.",
            "1 şeyin tadına bakın (ya da ağzınızdaki tadı fark edin).",
        ],
        reflection_prompt="Şu an nerede olduğunuzu ve nasıl hissettiğinizi bir cümleyle ifade edin.",
        points=45,
    ),
    DTxExercise(
        exercise_type=ExerciseType.MINDFULNESS,
        title="Bedensel Tarama (Body Scan)",
        duration_minutes=10,
        instructions=[
            "Sırt üstü uzanın veya rahat bir sandalyeye oturun.",
            "Gözlerinizi kapatın ve 3 derin nefes alın.",
            "Dikkatinizi ayak parmaklarınızdan başlatın.",
            "Bedeninizi yavaşça yukarı doğru tarayın.",
            "Gerilim hissettiğiniz bölgeleri fark edin ama yargılamayın.",
            "Her bölgeyi nefes vererek gevşetin.",
        ],
        reflection_prompt="Bedeninizin hangi bölgesinde en fazla gerilim hissettiniz?",
        points=50,
    ),
]

GRATITUDE_EXERCISES = [
    DTxExercise(
        exercise_type=ExerciseType.GRATITUDE,
        title="Minnettarlık Günlüğü",
        duration_minutes=7,
        instructions=[
            "Bugün için minnettar olduğunuz 3 şeyi yazın (küçük şeyler de olabilir).",
            "Her biri için 'neden' minnettar olduğunuzu bir cümle ekleyin.",
            "Bu şeylerin hayatınıza nasıl katkı sağladığını düşünün.",
        ],
        reflection_prompt="Bu egzersiz ruh halinizi nasıl etkiledi?",
        points=45,
    ),
]

BEHAVIORAL_EXERCISES = [
    DTxExercise(
        exercise_type=ExerciseType.BEHAVIORAL,
        title="Mikro-Aktivasyon Görevi",
        duration_minutes=5,
        instructions=[
            "Bugün yapabileceğiniz küçük ama anlamlı bir eylem belirleyin.",
            "Eylemi küçük adımlara bölün (maks. 3 adım).",
            "İlk adımı şimdi gerçekleştirin.",
            "Kendinizi bu başarı için tebrik edin.",
        ],
        reflection_prompt="Bu küçük eylem sizi nasıl hissettirdi?",
        points=55,
    ),
]

ALL_EXERCISES = (
    BREATHING_EXERCISES +
    COGNITIVE_EXERCISES +
    MINDFULNESS_EXERCISES +
    GRATITUDE_EXERCISES +
    BEHAVIORAL_EXERCISES
)


class DTxEngine:
    """
    Digital Therapeutics session planner.

    Based on the user's EWS risk level, selects evidence-based
    CBT exercises and composes a personalized therapy session.
    """

    RISK_PRIORITY = {
        "KRİTİK": [ExerciseType.BREATHING, ExerciseType.MINDFULNESS],
        "YÜKSEK": [ExerciseType.BREATHING, ExerciseType.COGNITIVE_REFRAME, ExerciseType.MINDFULNESS],
        "ORTA":   [ExerciseType.COGNITIVE_REFRAME, ExerciseType.BEHAVIORAL, ExerciseType.GRATITUDE],
        "DÜŞÜK":  [ExerciseType.GRATITUDE, ExerciseType.MINDFULNESS, ExerciseType.BEHAVIORAL],
    }

    SESSION_MESSAGES = {
        "KRİTİK": "Zor bir süreçtesiniz. Bu egzersizler sizi şu an için sabitlemek üzere seçildi. Bir profesyonele ulaşmanızı şiddetle öneririz.",
        "YÜKSEK": "Yoğun bir stres altındasınız. Bu oturum sizi sakinleştirmeye ve düşünceleri netleştirmeye odaklanıyor.",
        "ORTA":   "Gelişim devam ediyor. Bu egzersizler dayanıklılığınızı pekiştirmeye tasarlandı.",
        "DÜŞÜK":  "Harika gidiyorsunuz! Bu oturum güçlü yanlarınızı besliyor ve iyi ruh halinizi korumaya yardımcı oluyor.",
    }

    def create_session(
        self,
        risk_level: str = "ORTA",
        num_exercises: int = 3,
    ) -> DTxSession:
        """
        Creates a personalized DTx session based on the current risk level.

        Args:
            risk_level: EWS risk level string ("DÜŞÜK" / "ORTA" / "YÜKSEK" / "KRİTİK").
            num_exercises: Number of exercises in the session.

        Returns:
            DTxSession with curated exercises and session metadata.
        """
        priority_types = self.RISK_PRIORITY.get(risk_level, self.RISK_PRIORITY["ORTA"])

        selected = []
        available = {et: [e for e in ALL_EXERCISES if e.exercise_type == et] for et in priority_types}

        for et in priority_types:
            if available[et] and len(selected) < num_exercises:
                selected.append(random.choice(available[et]))

        # Fill remaining slots with any exercise if needed
        while len(selected) < num_exercises:
            pool = [e for e in ALL_EXERCISES if e not in selected]
            if not pool:
                break
            selected.append(random.choice(pool))

        total_points = sum(e.points for e in selected)
        message = self.SESSION_MESSAGES.get(risk_level, self.SESSION_MESSAGES["ORTA"])

        logger.info(
            f"DTx session created | Risk: {risk_level} | Exercises: {[e.title for e in selected]}"
        )

        return DTxSession(
            exercises=selected,
            session_points=total_points,
            risk_level_targeted=risk_level,
            session_message=message,
        )
