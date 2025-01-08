from pathlib import Path
from tests_lib.helpers.yaml_loader import YAMLLoader
from tests_lib.common.logger.log_level import LogLevel

class WebUIConfig:
    """Test configuration from YAML."""
    CONFIG_PATH = Path(__file__).resolve().parent / "web_ui_config.yaml"
    TEST_DATA_PATH = Path(__file__).resolve().parent.parent.parent.parent / "tests/data/web_ui_test_data.yaml"
    
    _config = YAMLLoader().load_data(CONFIG_PATH)["web_ui"]
    _test_data = YAMLLoader().load_data(TEST_DATA_PATH)["web_ui_test_data"]
    
    # Browser and Driver Configuration
    BASE_URL = _config["base_url"]
    IMPLICIT_WAIT = _config["implicit_wait"]
    SELENIUM_HUB = _config["selenium_hub"]
    BROWSER = _config["browser"]
    
    # Logger Configuration
    LOGGER_NAME = _config["logger"]["name"]
    LOG_LEVEL = LogLevel[_config["logger"]["level"]]
    
    # Common Test Data
    COMMON = _test_data["common"]
    CREDENTIALS = _test_data["credentials"]
    
    # Page Specific Data
    PAGES = _test_data["pages"]