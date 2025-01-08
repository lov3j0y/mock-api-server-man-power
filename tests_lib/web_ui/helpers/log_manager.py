import logging
from tests_lib.common.logger.base_logger import BaseLogger

class LogManager(BaseLogger):
    """Class to manage logging configuration and creation."""
    
    def get_logger(self, name, level):
        """
        Create a logger that writes to a file in the logs directory.
        
        Args:
            name: Name of the logger and log file
            level: Minimum log level to record
        """
        logger = logging.getLogger(f"__{name}__")
        logger.setLevel(level.value)
        
        log_file = self.LOGS_DIR / f"{name}_run.log"
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(level.value)

        formatter = logging.Formatter(self.LOG_FORMAT, datefmt=self.DATE_FORMAT)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        
        return logger