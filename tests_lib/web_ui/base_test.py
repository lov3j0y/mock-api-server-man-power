import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from tests_lib.common.logger.logger import LogManager
from tests_lib.helpers.json_loader import JSONLoader
from tests_lib.web_ui.pages.login_page import LoginPage
from tests_lib.web_ui.pages.inventory_page import InventoryPage
from tests_lib.web_ui.pages.cart_page import CartPage
from tests_lib.web_ui.pages.checkout_page import CheckoutPage
from tests_lib.web_ui.pages.hidden_menu_page import HiddenMenuPage
from tests_lib.web_ui.config.web_ui_config import WebUIConfig


class BaseTest:
    """Base class for UI tests with common setup."""
    @pytest.fixture(autouse=True)
    def setup_logger(self):
        """Setup method to initialize the logger."""
        log_manager = LogManager()
        self.logger = log_manager.get_logger(WebUIConfig.LOGGER_NAME, WebUIConfig.LOG_LEVEL)
        yield self.logger
        # Cleanup handlers to prevent duplication
        for handler in self.logger.handlers[:]:
            handler.close()
            self.logger.removeHandler(handler)
            
    @pytest.fixture()
    def driver(self):
        """Create WebDriver instance."""
        browser = os.getenv("BROWSER", "firefox")
        
        if browser == "firefox":
            options = FirefoxOptions()
        elif browser == "chrome":
            options = ChromeOptions()
        else:
            raise ValueError(f"Unsupported browser: {browser}")

        options.add_argument("--headless")
        
        driver = webdriver.Remote(
            command_executor=WebUIConfig.SELENIUM_HUB,
            options=options        
        )
        driver.implicitly_wait(WebUIConfig.IMPLICIT_WAIT)
        
        yield driver
        driver.quit()

    
    def login(self, user_type="valid_user"):
        """Login with specified user type."""
        credentials = JSONLoader().load_data("test_data_webui_credentials.json", "credentials")
        user = credentials[user_type]
        
        login_page = LoginPage(self.driver, self.logger)
        self.driver.get(WebUIConfig.BASE_URL)
        login_page.input_username(user["username"])
        login_page.input_password(user["password"])
        login_page.click_login_button()

    @pytest.fixture
    def setup(self, driver):
        """Setup test with driver."""
        self.driver = driver
        return self.login


    @pytest.fixture
    def login_page(self):
        """Create LoginPage instance."""
        return LoginPage(self.driver, self.logger)

    @pytest.fixture 
    def inventory_page(self):
        """Create InventoryPage instance."""
        return InventoryPage(self.driver, self.logger)

    @pytest.fixture
    def cart_page(self):
        """Create CartPage instance."""
        return CartPage(self.driver, self.logger)

    @pytest.fixture
    def checkout_page(self):
        """Create CheckoutPage instance."""
        return CheckoutPage(self.driver, self.logger)

    @pytest.fixture
    def hidden_menu_page(self):
        """Create HiddenMenuPage instance."""
        return HiddenMenuPage(self.driver, self.logger)