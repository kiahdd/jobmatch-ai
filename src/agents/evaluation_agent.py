"""Higher-level evaluation agent for ranking job opportunities."""

from src.matching.ranking import rank_jobs


def generate_ranked_report(match_results: list[dict]) -> dict:
    """Generate a structured report for ranked job matches."""
    ranked = rank_jobs(match_results)
    return {
        "summary": {
            "total_matches": len(ranked),
            "top_match": ranked[0] if ranked else None,
        },
        "ranked_matches": ranked,
    }
