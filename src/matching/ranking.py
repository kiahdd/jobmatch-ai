"""Ranking utilities for job recommendations."""

from typing import Sequence


def rank_jobs(fit_scores: Sequence[dict]) -> list[dict]:
    """Return job postings ordered by fit score."""
    return sorted(fit_scores, key=lambda item: item.get("fit_score", 0), reverse=True)
