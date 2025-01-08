from pathlib import Path
from tests_lib.helpers.yaml_loader import YAMLLoader
from tests_lib.common.logger.log_level import LogLevel

class WebUIConfig:
    """Test configuration from YAML."""
    CONFIG_PATH = Path(__file__).resolve().parent / "web_ui_config.yaml"
    TEST_DATA_PATH = Path(__file__).resolve().parent.parent.parent.parent / "tests/data/web_ui_test_data.yaml"
    
    _config = YAMLLoader().load_data(CONFIG_PATH)["web_ui"]
    _test_data = YAMLLoader().load_data(TEST_DATA_PATH)["web_ui_test_data"]
    
    BASE_URL = _config["base_url"]
    IMPLICIT_WAIT = _config["implicit_wait"]
    SELENIUM_HUB = _config["selenium_hub"]
    LOGGER_NAME = _config["logger"]["name"]
    LOG_LEVEL = LogLevel[_config["logger"]["level"]]
    BROWSER = _config["browser"]
    
    CREDENTIALS = _test_data["credentials"]
    ERROR_MESSAGES = _test_data["messages"]["errors"]