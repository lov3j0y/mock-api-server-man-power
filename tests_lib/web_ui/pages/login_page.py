from selenium.webdriver.common.by import By

from tests_lib.web_ui.pages.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.username_field = (By.ID, "user-name")
        self.password_field = (By.ID, "password")
        self.login_button = (By.ID, "login-button")
        self.error_message = (By.CSS_SELECTOR, ".error-message-container.error")

    def input_username(self, username):
        self.type(self.username_field, username)

    def input_password(self, password):
        self.type(self.password_field, password)

    def click_login_button(self):
        self.click(self.login_button)

    def get_error_message(self):
        return self.get_text(self.error_message)
