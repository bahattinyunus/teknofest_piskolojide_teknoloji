"""
TEKNOFEST 2025 — Elite Command Center
Security & Anonymization Utilities
KVKK / HIPAA Compliant
"""

import hashlib
import os
import re


def anonymize_id(user_id: str) -> str:
    """
    Creates a one-way SHA-256 hash of the user ID for KVKK-compliant anonymization.

    Args:
        user_id: Raw user identifier.

    Returns:
        str: 16-character anonymized hash token.
    """
    salt = os.environ.get("ANON_SALT", "teknofest2025_default_salt")
    raw = f"{salt}::{user_id}"
    return hashlib.sha256(raw.encode()).hexdigest()[:16]


def sanitize_text(text: str) -> str:
    """
    Removes personally identifiable information (PII) from free-text input.
    Strips phone numbers, emails, and Turkish TC ID numbers.

    Args:
        text: Raw user text input.

    Returns:
        str: Sanitized text.
    """
    # Remove email addresses
    text = re.sub(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', '[EMAIL]', text)
    # Remove Turkish phone numbers
    text = re.sub(r'0?\s?5\d{2}[\s\-]?\d{3}[\s\-]?\d{2}[\s\-]?\d{2}', '[PHONE]', text)
    # Remove 11-digit TC ID numbers
    text = re.sub(r'\b[1-9]\d{10}\b', '[TC_NO]', text)
    return text.strip()


def validate_score(score: float, scale_name: str, min_val: float, max_val: float) -> float:
    """
    Validates that a psychometric score is within the expected clinical range.

    Args:
        score: Raw score value.
        scale_name: Name of the psychometric scale (for logging).
        min_val: Minimum valid value.
        max_val: Maximum valid value.

    Returns:
        float: Clamped score value.

    Raises:
        ValueError: If score is not a number.
    """
    if not isinstance(score, (int, float)):
        raise ValueError(f"[{scale_name}] Score must be numeric, got: {type(score)}")
    return float(max(min_val, min(max_val, score)))
