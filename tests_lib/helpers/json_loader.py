import json
from pathlib import Path
from tests_lib.common.base_loader import BaseLoader

class JSONLoader(BaseLoader):
    """Class to handle loading JSON data."""

    def load_data(self, filename: str, key: str = None):
        """Load data from a JSON file."""
        data_folder = Path(__file__).resolve().parent.parent.parent / "tests" / "data"
        file_path = data_folder / filename

        if file_path.suffix == ".json":
            with open(file_path, 'r', encoding="utf-8") as file:
                data = json.load(file)
            return data if key is None else data[key]
