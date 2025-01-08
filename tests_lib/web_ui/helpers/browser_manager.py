import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from tests_lib.web_ui.config.web_ui_config import WebUIConfig

class BrowserManager:
    def get_browser(self):
        """Get WebDriver instance with configured options."""
        browser_name = os.getenv("BROWSER", WebUIConfig.BROWSER["default"])
        options = self._get_browser_options(browser_name)
        return webdriver.Remote(
            command_executor=WebUIConfig.SELENIUM_HUB,
            options=options
        )
    
    def _get_browser_options(self, browser_name):
        """Configure browser options based on config."""
        if browser_name == "firefox":
            options = FirefoxOptions()
        elif browser_name == "chrome":
            options = ChromeOptions()
        else:
            raise ValueError(f"Unsupported browser: {browser_name}")
            
        for option in WebUIConfig.BROWSER["options"][browser_name]:
            options.add_argument(option)
        return options