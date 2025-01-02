from tests_lib.web_ui.pages.base_page import BasePage
from selenium.webdriver.common.by import By

class CheckoutPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.first_name_field = (By.ID, "first-name")
        self.last_name_field = (By.ID, "last-name")
        self.postal_code_field = (By.ID, "postal-code")
        self.continue_button = (By.CSS_SELECTOR, ".cart_button")
        self.finish_button = (By.ID, "finish")
        self.complete_header = (By.CSS_SELECTOR, ".complete-header")

    def enter_first_name(self, first_name):
        self.type(self.first_name_field, first_name)

    def enter_last_name(self, last_name):
        self.type(self.last_name_field, last_name)

    def enter_postal_code(self, postal_code):
        self.type(self.postal_code_field, postal_code)

    def click_continue(self):
        self.click(self.continue_button)

    def click_finish(self):
        self.click(self.finish_button)

    def is_page_loaded(self):
        current_url = self.driver.current_url
        return "checkout-step-one.html" in current_url or "checkout-step-two.html" in current_url

    def is_checkout_complete(self):
        return self.get_text(self.complete_header) == "Thank you for your order!"
