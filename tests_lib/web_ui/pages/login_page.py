from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from tests_lib.web_ui.pages.base_page import BasePage


class LoginPage(BasePage):
    """Page object for login functionality."""
    USERNAME_FIELD = (By.ID, "user-name")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, ".error-message-container.error")
    LOGIN_URL = "https://www.saucedemo.com/"

    def __init__(self, driver):
        super().__init__(driver)
        self.username_field = self.USERNAME_FIELD
        self.password_field = self.PASSWORD_FIELD
        self.login_button = self.LOGIN_BUTTON
        self.error_message = self.ERROR_MESSAGE

    def input_username(self, username):
        """Enter username into login form."""
        self.type(self.username_field, username)

    def input_password(self, password):
        """Enter password into login form."""
        self.type(self.password_field, password)

    def click_login_button(self):
        """Click login button to submit form."""
        self.click(self.login_button)
        
    def login(self, username, password):
        """ Perform login with given credentials. """
        self.input_username(username)
        self.input_password(password) 
        self.click_login_button()

    def get_error_message(self):
        """Get login error message if present."""
        return self.get_text(self.error_message)

    def is_on_login_page(self):
        """Verify if current page is login page."""
        return self.driver.current_url == self.LOGIN_URL