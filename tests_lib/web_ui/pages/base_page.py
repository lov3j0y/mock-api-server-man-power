from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests_lib.web_ui.config.web_ui_config import WebUIConfig

class BasePage:
    """Base class for all page objects."""

    def __init__(self, driver, logger):
        self.driver = driver
        self.wait = WebDriverWait(driver, WebUIConfig.IMPLICIT_WAIT)
        self.logger = logger

    def find_element(self, by):
        """Find element with explicit wait."""
        return self.wait.until(EC.visibility_of_element_located(by))

    def find_elements(self, by):
        """Find multiple elements."""
        return self.driver.find_elements(*by)

    def click(self, by):
        """Click on element."""
        self.find_element(by).click()

    def type(self, by, text):
        """Type text into element."""
        element = self.find_element(by)
        element.clear()
        element.send_keys(str(text))

    def get_text(self, by):
        """Get element's text content."""
        return self.find_element(by).text