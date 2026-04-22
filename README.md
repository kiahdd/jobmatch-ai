# jobmatch-ai

jobmatch-ai is an AI-driven pipeline for evaluating and ranking job opportunities against a candidate resume.
It supports resume ingestion, text preprocessing, semantic similarity matching, structured scoring, and ranked job recommendations.

## What it does

- Accepts a resume in PDF or plain text format
- Ingests multiple job descriptions for comparison
- Preprocesses text and extracts key features such as skills, experience, and keywords
- Computes semantic similarity using embeddings (OpenAI or sentence-transformers)
- Calculates a structured fit score based on skill match, experience alignment, and role relevance
- Produces a ranked list of job postings with explanations for each score
- Provides an AI agent architecture for resume-to-job evaluation and ranking

## Project structure

- `data/`
  - `resumes/` — raw candidate resumes
  - `job_descriptions/` — raw job posting content
  - `processed/` — prepared artifacts and extracted features
- `src/`
  - `ingestion/` — resume and job description loading utilities
  - `preprocessing/` — text cleaning and feature extraction
  - `matching/` — semantic similarity, scoring, and ranking logic
  - `agents/` — higher-level evaluation and ranking agents
  - `utils/` — configuration and logging helpers
- `notebooks/` — notebooks for exploration and prototyping
- `tests/` — unit tests for core scoring and matching workflows
- `main.py` — application entrypoint

## Setup

1. Create a Python virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

2. Copy the environment example

```bash
cp .env.example .env
```

3. Add your OpenAI API key to `.env`

4. Run the application

```bash
python main.py
```

> Note: The project uses `pypdf` for PDF resume parsing and supports OpenAI or local sentence-transformers embeddings.

3. Add your OpenAI API key to `.env`

4. Run the application

```bash
python main.py
```

## Notes

This repository provides the initial structure and starter implementations for each module.
Extend the modules in `src/` to add real resume parsing, embedding generation, scoring formulas, and reporting logic.
