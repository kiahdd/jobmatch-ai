"""Resume ingestion and parsing utilities."""

from pathlib import Path


def load_resume(file_path: str) -> str:
    """Load a resume from PDF or plain text and return raw content."""
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"Resume file not found: {file_path}")

    if path.suffix.lower() == ".pdf":
        try:
            from pypdf import PdfReader
        except ImportError:  # pragma: no cover
            from PyPDF2 import PdfReader

        reader = PdfReader(path)
        text = []
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text.append(page_text)
        return "\n".join(text)

    return path.read_text(encoding="utf-8", errors="ignore")
