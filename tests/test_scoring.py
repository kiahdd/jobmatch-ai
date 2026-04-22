import pytest

from src.matching.scoring import compute_fit_score


def test_compute_fit_score_range() -> None:
    score = compute_fit_score(0.8, 0.6, 0.5)
    assert 0 <= score <= 1
    assert score == pytest.approx(0.8 * 0.5 + 0.6 * 0.3 + 0.5 * 0.2)
