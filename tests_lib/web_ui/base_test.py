import os
import pytest
from tests_lib.web_ui.helpers.log_manager import LogManager
from tests_lib.web_ui.config.web_ui_config import WebUIConfig
from tests_lib.web_ui.helpers.browser_manager import BrowserManager
from tests_lib.web_ui.factories.page_factory import PageFactory

class BaseTest:
    @pytest.fixture(autouse=True)
    def setup_logger(self, request):
        """Setup method to initialize the logger."""
        log_manager = LogManager()
        self.logger = log_manager.get_logger(WebUIConfig.LOGGER_NAME, WebUIConfig.LOG_LEVEL)
        test_name = f"{request.cls.__name__}.{request.node.name}"
        self.logger.info(f"=== Starting test: {test_name} ===")
        yield self.logger
        self.logger.info(f"=== Completed test: {test_name} ===\n")
        for handler in self.logger.handlers[:]:
            handler.close()
            self.logger.removeHandler(handler)
            
    @pytest.fixture()
    def driver(self):
        """Create WebDriver instance."""
        browser_manager = BrowserManager()
        driver = browser_manager.get_browser()
        driver.implicitly_wait(WebUIConfig.IMPLICIT_WAIT)
        yield driver
        driver.quit()
        


    @pytest.fixture
    def setup(self, driver, pages):
        """Setup test with driver and pages."""
        self.driver = driver
        self.pages = pages
        return self.pages.get_login_page().login_as

    @pytest.fixture
    def pages(self, driver):
        """Create page factory."""
        return PageFactory(driver, self.logger)

    @pytest.fixture
    def login_page(self, pages):
        return pages.get_login_page()

    @pytest.fixture
    def inventory_page(self, pages):
        return pages.get_inventory_page()

    @pytest.fixture
    def cart_page(self, pages):
        return pages.get_cart_page()

    @pytest.fixture
    def checkout_page(self, pages):
        return pages.get_checkout_page()

    @pytest.fixture
    def hidden_menu_page(self, pages):
        return pages.get_hidden_menu_page()