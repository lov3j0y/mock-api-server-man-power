from pathlib import Path
from tests_lib.helpers.yaml_loader import YAMLLoader
from tests_lib.common.logger.log_level import LogLevel

class WebUIConfig:
    """Test configuration from YAML."""
    CONFIG_PATH = Path(__file__).resolve().parent / "web_ui_config.yaml"
    _config = YAMLLoader().load_data(CONFIG_PATH)["web_ui"]
    
    BASE_URL = _config["base_url"]
    IMPLICIT_WAIT = _config["implicit_wait"]
    SELENIUM_HUB = _config["selenium_hub"]
    LOGGER_NAME = _config["logger"]["name"]
    LOG_LEVEL = LogLevel[_config["logger"]["level"]]
    BROWSER = _config["browser"]