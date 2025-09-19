import logging
import os

def setup_logging(level: int | str = None):
    level = level or os.environ.get("LOG_LEVEL", "INFO")
    logging.basicConfig(level=level, format="%(levelname)s: %(message)s")
    logging.getLogger("httpx").setLevel(logging.WARNING)
    logging.getLogger("urllib3").setLevel(logging.WARNING)
    return logging.getLogger(__name__)
