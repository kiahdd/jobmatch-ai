from pathlib import Path
from src.utils.config import load_config
from src.utils.logger import configure_logger


def main() -> None:
    config = load_config()
    logger = configure_logger(config.LOG_LEVEL)

    logger.info("Starting jobmatch-ai")
    logger.info(f"Data path: {config.DATA_PATH}")
    logger.info("The core resume-to-job matching modules are initialized.")
    logger.info("Extend src/ to implement custom ingestion, scoring, and ranking logic.")


if __name__ == "__main__":
    main()
