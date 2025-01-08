from selenium.webdriver.common.by import By
from tests_lib.web_ui.pages.base_page import BasePage
from tests_lib.web_ui.config.web_ui_config import WebUIConfig

class LoginPage(BasePage):
    """Page object for login functionality."""
    # Page Locators
    locators = WebUIConfig.PAGES["login"]["locators"]    
    USERNAME_FIELD = (By.ID, locators["username_field"])
    PASSWORD_FIELD = (By.ID, locators["password_field"])
    LOGIN_BUTTON = (By.ID, locators["login_button"])
    ERROR_MESSAGE = (By.CSS_SELECTOR, locators["error_message"])

    def __init__(self, driver, logger):
        super().__init__(driver, logger)
        self.username_field = self.USERNAME_FIELD
        self.password_field = self.PASSWORD_FIELD
        self.login_button = self.LOGIN_BUTTON
        self.error_message = self.ERROR_MESSAGE
        self.logger.info("Login page initialized")

    def login_as(self, user_type="valid_user"):
        """Login with predefined user type."""
        user = WebUIConfig.CREDENTIALS[user_type]
        self.driver.get(WebUIConfig.BASE_URL)
        return self.login(user["username"], user["password"])

    def login(self, username, password):
        """Perform login with given credentials."""
        self.logger.info(f"Attempting login for user: {username}")
        try:
            self.input_username(username)
            self.input_password(password)
            self.click_login_button()
            return True
        except Exception as e:
            self.logger.error(f"Login failed: {str(e)}")
            return False
        
    def input_username(self, username):
        """Enter username into login form."""
        self.logger.info(f"Entering username: {username}")
        self.type(self.username_field, username)

    def input_password(self, password):
        """Enter password into login form."""
        self.logger.info("Entering password")
        self.type(self.password_field, password)

    def click_login_button(self):
        """Click login button to submit form."""
        self.logger.info("Clicking login button")
        self.click(self.login_button)
        
    def get_error_message(self):
        """Get login error message if present."""
        return self.get_text(self.error_message)