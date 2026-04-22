"""Agent for orchestrating resume and job matching."""

from src.matching.scoring import compute_fit_score, score_skill_match
from src.matching.similarity import compute_embeddings, cosine_similarity
from src.preprocessing.feature_extraction import extract_experience, extract_skills
from src.preprocessing.text_cleaning import clean_text


def evaluate_job_match(resume_text: str, job_description: str) -> dict:
    """Evaluate a single job description against a resume."""
    resume_clean = clean_text(resume_text)
    job_clean = clean_text(job_description)

    resume_skills = extract_skills(resume_clean)
    job_skills = extract_skills(job_clean)

    resume_experience = extract_experience(resume_clean)
    job_experience = extract_experience(job_clean)

    embeddings = compute_embeddings([resume_clean, job_clean])
    similarity_score = 0.0
    if len(embeddings) == 2:
        similarity_score = cosine_similarity(embeddings[0], embeddings[1])

    skill_score = score_skill_match(resume_skills, job_skills)

    expected_years = max(job_experience.get("years_experience", 0), 1)
    experience_score = min(resume_experience.get("years_experience", 0) / expected_years, 1.0)

    fit_score = compute_fit_score(similarity_score, skill_score, experience_score)

    return {
        "resume_skills": resume_skills,
        "job_skills": job_skills,
        "similarity_score": similarity_score,
        "skill_score": skill_score,
        "experience_score": experience_score,
        "fit_score": fit_score,
        "seniority_match": resume_experience.get("seniority") == job_experience.get("seniority"),
    }
