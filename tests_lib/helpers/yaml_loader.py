import yaml
from pathlib import Path
from tests_lib.common.base_loader import BaseLoader


class YAMLLoader(BaseLoader):
    """Class to handle loading YAML data."""
    
    VALID_EXTENSIONS = {".yaml", ".yml"}

    def load_data(self, filename, key=None):
        """Load data from a YAML file."""
        data_folder = Path(__file__).resolve().parent.parent.parent/ "tests_lib"/ "web_ui" / "config"
        file_path = data_folder / filename

        if file_path.suffix not in self.VALID_EXTENSIONS:
            raise ValueError(f"Invalid file extension. Expected {self.VALID_EXTENSIONS}")

        with open(file_path, 'r', encoding="utf-8") as file:
            data = yaml.safe_load(file)
        return data if key is None else data[key]