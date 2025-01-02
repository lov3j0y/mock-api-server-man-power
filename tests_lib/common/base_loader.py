from pathlib import Path
from abc import ABC, abstractmethod

class BaseLoader(ABC):
    """Base class for loaders."""

    @abstractmethod
    def load_data(self, filename: str, key: str = None):
        """Load data from a file."""
        pass