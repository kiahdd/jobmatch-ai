"""Scoring functions for candidate-job fit."""


def score_skill_match(resume_skills: list[str], job_skills: list[str]) -> float:
    """Compute a skill match score based on shared keywords."""
    if not job_skills:
        return 0.0

    resume_set = {skill.lower() for skill in resume_skills}
    job_set = {skill.lower() for skill in job_skills}
    match_count = len(resume_set & job_set)
    return float(match_count) / len(job_set)


def compute_fit_score(similarity_score: float, skill_score: float, experience_score: float) -> float:
    """Combine similarity and structured factors into a final fit score."""
    weights = {
        "similarity": 0.5,
        "skill": 0.3,
        "experience": 0.2,
    }
    return (
        similarity_score * weights["similarity"]
        + skill_score * weights["skill"]
        + experience_score * weights["experience"]
    )
