from pathlib import Path
from tests_lib.common.logger.log_level import LogLevel
from tests_lib.helpers.json_loader import JSONLoader
from tests_lib.helpers.yaml_loader import YAMLLoader

class DatabaseConfig:
    """Database configuration and test data."""    
    CONFIG_PATH = Path(__file__).resolve().parent / "database_config.yaml"
    
    _config = YAMLLoader().load_data(CONFIG_PATH)["database"]
    _test_data = JSONLoader().load_data("database_test_data.json")
    QUERIES = _test_data.get("queries", [])    
    
    # Logger Configuration
    LOGGER_NAME = _config["logger"]["name"]
    LOG_LEVEL = LogLevel[_config["logger"]["level"]]