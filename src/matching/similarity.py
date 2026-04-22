"""Semantic similarity utilities."""

import math
import os
from typing import Sequence


def compute_embeddings(items: Sequence[str]) -> list[list[float]]:
    """Convert text items into embeddings using local or OpenAI models."""
    if not items:
        return []

    embedding_model = os.getenv("OPENAI_MODEL", "text-embedding-3-large")

    try:
        from sentence_transformers import SentenceTransformer
        model_name = embedding_model if embedding_model.startswith("sentence-") else "all-MiniLM-L6-v2"
        model = SentenceTransformer(model_name)
        embeddings = model.encode(list(items), show_progress_bar=False)
        return [list(map(float, emb)) for emb in embeddings]
    except Exception:
        import openai

        api_key = os.getenv("OPENAI_API_KEY", "")
        if not api_key:
            raise RuntimeError("OpenAI API key is required for embedding generation.")

        openai.api_key = api_key
        response = openai.Embedding.create(
            model=embedding_model,
            input=list(items),
        )
        return [item.embedding for item in response.data]


def cosine_similarity(a: list[float], b: list[float]) -> float:
    """Compute cosine similarity between two vectors."""
    if len(a) != len(b):
        raise ValueError("Vectors must be the same length.")

    dot = sum(x * y for x, y in zip(a, b))
    norm_a = math.sqrt(sum(x * x for x in a))
    norm_b = math.sqrt(sum(y * y for y in b))
    if not norm_a or not norm_b:
        return 0.0

    return dot / (norm_a * norm_b)
