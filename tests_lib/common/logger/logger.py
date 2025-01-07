import logging
from enum import Enum
from pathlib import Path

LOGS_DIR = Path(__file__).resolve().parent.parent.parent.parent / "logs"
LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
DATE_FORMAT = "%m/%d/%Y %I:%M:%S%p"

class LogLevel(Enum):
    """Logging levels enumeration."""
    DEBUG = logging.DEBUG  # 10
    INFO = logging.INFO  # 20
    WARNING = logging.WARNING  # 30
    ERROR = logging.ERROR  # 40
    CRITICAL = logging.CRITICAL  # 50

def logger(name, level):
    """
    Create a logger that writes to a file in the logs directory.
    
    Args:
        name: Name of the logger and log file
        level: Minimum log level to record
    """

    # Create logger
    logger = logging.getLogger(f"__{name}__")
    logger.setLevel(level.value)
    log_file = LOGS_DIR / f"{name}_run.log"
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(level.value)

    # Setup formatter
    formatter = logging.Formatter(LOG_FORMAT, datefmt=DATE_FORMAT)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger