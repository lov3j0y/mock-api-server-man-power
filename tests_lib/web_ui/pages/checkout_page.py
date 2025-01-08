from tests_lib.web_ui.config.web_ui_config import WebUIConfig
from tests_lib.web_ui.pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


class CheckoutPage(BasePage):
    """Page object for checkout process."""
    # Page URLs and messages
    locators = WebUIConfig.PAGES["checkout"]["locators"]
    customer_data = WebUIConfig.PAGES["checkout"]["customer_data"]
    paths = WebUIConfig.COMMON["paths"]["checkout"]
    messages = WebUIConfig.COMMON["messages"]
    
    # Page locators
    FIRST_NAME_FIELD = (By.ID, locators["first_name_field"])
    LAST_NAME_FIELD = (By.ID, locators["last_name_field"])
    POSTAL_CODE_FIELD = (By.ID, locators["postal_code_field"])
    CONTINUE_BUTTON = (By.CSS_SELECTOR, locators["continue_button"])
    FINISH_BUTTON = (By.ID, locators["finish_button"])
    COMPLETE_HEADER = (By.CSS_SELECTOR, locators["complete_header"])
    ERROR_MESSAGE = (By.CSS_SELECTOR, locators["error_message"])
    
    # Page constants
    STEP_ONE_URL = paths["step_one"]
    STEP_TWO_URL = paths["step_two"]
    SUCCESS_MESSAGE = messages["success"]["checkout"]
    ERROR_MESSAGES = messages["errors"]["form"]
    
    def __init__(self, driver, logger):
        super().__init__(driver, logger)
        self.first_name_field = self.FIRST_NAME_FIELD
        self.last_name_field = self.LAST_NAME_FIELD
        self.postal_code_field = self.POSTAL_CODE_FIELD
        self.continue_button = self.CONTINUE_BUTTON
        self.finish_button = self.FINISH_BUTTON
        self.complete_header = self.COMPLETE_HEADER
        self.error_message = self.ERROR_MESSAGE

    def fill_checkout_form(self, first_name, last_name, postal_code):
        """Fill all checkout form fields at once."""
        self.enter_first_name(first_name)
        self.enter_last_name(last_name)
        self.enter_postal_code(postal_code)

    def enter_first_name(self, first_name):
        """Enter customer first name."""
        self.type(self.first_name_field, first_name)

    def enter_last_name(self, last_name):
        """Enter customer last name."""
        self.type(self.last_name_field, last_name)

    def enter_postal_code(self, postal_code):
        """Enter customer postal code."""
        self.type(self.postal_code_field, postal_code)

    def click_continue(self):
        """Proceed to next checkout step."""
        self.click(self.continue_button)

    def click_finish(self):
        """Complete checkout process."""
        self.click(self.finish_button)

    def is_page_loaded(self):
        """Check if on checkout page."""
        current_url = self.driver.current_url
        return self.STEP_ONE_URL in current_url or self.STEP_TWO_URL in current_url

    def is_checkout_complete(self):
        """Check if checkout was successful."""
        try:
            return self.get_text(self.complete_header) == self.SUCCESS_MESSAGE
        except TimeoutException:
            return False
        
    def get_error_message(self):
        """Get form validation error message."""
        try:
            return self.get_text(self.error_message)
        except TimeoutException:
            return None