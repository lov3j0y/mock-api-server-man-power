from tests_lib.web_ui.pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


class CheckoutPage(BasePage):
    """Page object for checkout process."""
    STEP_ONE_URL = "checkout-step-one.html"
    STEP_TWO_URL = "checkout-step-two.html"
    SUCCESS_MESSAGE = "Thank you for your order!"
    ERROR_MESSAGES = {
        "first_name": "Error: First Name is required",
        "last_name": "Error: Last Name is required",
        "postal_code": "Error: Postal Code is required"
    }


    def __init__(self, driver, logger):
        super().__init__(driver, logger)
        self.first_name_field = (By.ID, "first-name")
        self.last_name_field = (By.ID, "last-name")
        self.postal_code_field = (By.ID, "postal-code")
        self.continue_button = (By.CSS_SELECTOR, ".cart_button")
        self.finish_button = (By.ID, "finish")
        self.complete_header = (By.CSS_SELECTOR, ".complete-header")
        self.error_message = (By.CSS_SELECTOR, "[data-test='error']")

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