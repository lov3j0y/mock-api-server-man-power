from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class BasePage:
    """Base class for all page objects."""
    
    TIMEOUT = 10

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, self.TIMEOUT)

    def find_element(self, by):
        """Find element with explicit wait."""
        try:
            return self.wait.until(EC.visibility_of_element_located(by))
        except TimeoutException:
            raise TimeoutException(f"Element not found: {by}")

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