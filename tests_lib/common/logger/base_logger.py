from abc import ABC, abstractmethod
from pathlib import Path
from tests_lib.common.logger.log_level import LogLevel

class BaseLogger(ABC):
    """Abstract base class for logging functionality."""
    LOGS_DIR = Path(__file__).resolve().parent.parent.parent.parent / "logs"
    LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    DATE_FORMAT = "%m/%d/%Y %I:%M:%S%p"

    @abstractmethod
    def get_logger(self, name, level):
        """Get configured logger instance."""
        pass