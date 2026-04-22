from src.matching.ranking import rank_jobs


def test_rank_jobs_sorts_by_fit_score() -> None:
    items = [
        {"title": "Job A", "fit_score": 0.5},
        {"title": "Job B", "fit_score": 0.9},
        {"title": "Job C", "fit_score": 0.7},
    ]
    ranked = rank_jobs(items)
    assert ranked[0]["title"] == "Job B"
    assert ranked[-1]["title"] == "Job A"
