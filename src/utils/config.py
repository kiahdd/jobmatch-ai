"""Configuration loader for the application."""

from dataclasses import dataclass
from pathlib import Path
from dotenv import load_dotenv
import os


@dataclass
class Config:
    OPENAI_API_KEY: str
    OPENAI_MODEL: str
    DATA_PATH: str
    LOG_LEVEL: str


def load_config() -> Config:
    load_dotenv(dotenv_path=Path(".env"))
    return Config(
        OPENAI_API_KEY=os.getenv("OPENAI_API_KEY", ""),
        OPENAI_MODEL=os.getenv("OPENAI_MODEL", "text-embedding-3-large"),
        DATA_PATH=os.getenv("DATA_PATH", "data"),
        LOG_LEVEL=os.getenv("LOG_LEVEL", "INFO"),
    )
