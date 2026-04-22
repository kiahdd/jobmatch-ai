"""Feature extraction for resumes and job descriptions."""

import re
from typing import Dict

SKILL_KEYWORDS = [
    "python",
    "sql",
    "machine learning",
    "deep learning",
    "data analysis",
    "nlp",
    "natural language processing",
    "pandas",
    "numpy",
    "scikit-learn",
    "tensorflow",
    "pytorch",
    "aws",
    "azure",
    "spark",
    "docker",
    "kubernetes",
    "project management",
    "communication",
]


def extract_skills(text: str) -> list[str]:
    """Extract candidate skill keywords from text."""
    normalized = text.lower()
    matches = set()
    for skill in SKILL_KEYWORDS:
        if skill in normalized:
            matches.add(skill)
    return sorted(matches)


def extract_experience(text: str) -> Dict[str, int]:
    """Extract experience and seniority details from text."""
    normalized = text.lower()
    experience_years = 0
    years_matches = re.findall(r"(\d+)\s*\+?\s*(?:years|yrs|year)", normalized)
    if years_matches:
        experience_years = max(int(value) for value in years_matches)

    seniority = "mid"
    if "senior" in normalized or "lead" in normalized:
        seniority = "senior"
    elif "junior" in normalized or "entry" in normalized:
        seniority = "junior"

    return {
        "years_experience": experience_years,
        "seniority": seniority,
    }
