"""Text cleaning utilities for resumes and job descriptions."""

import re


def clean_text(text: str) -> str:
    """Normalize text, remove noise, and prepare for feature extraction."""
    text = text.lower()
    text = re.sub(r"\s+", " ", text)
    text = re.sub(r"[^a-z0-9\s\-\.,]", "", text)
    return text.strip()
