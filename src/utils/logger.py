"""Simple logger configuration helper."""

import logging


def configure_logger(level: str = "INFO") -> logging.Logger:
    logger = logging.getLogger("jobmatch_ai")
    numeric_level = getattr(logging, level.upper(), logging.INFO)
    logger.setLevel(numeric_level)

    if not logger.handlers:
        handler = logging.StreamHandler()
        formatter = logging.Formatter("%(asctime)s %(levelname)s %(message)s")
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger
