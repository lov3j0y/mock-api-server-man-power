from tests_lib.web_ui.config.web_ui_config import WebUIConfig
from tests_lib.web_ui.pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


class HiddenMenuPage(BasePage):
    """Page object for the hidden menu functionality."""
    locators = WebUIConfig.PAGES["hidden_menu"]["locators"]
    
    # Page locators
    MENU_BUTTON = (By.CSS_SELECTOR, locators["menu_button"])
    LOGOUT_BUTTON = (By.ID, locators["logout_button"])
    MENU_CONTAINER = (By.CLASS_NAME, locators["menu_container"])
    
    def __init__(self, driver, logger):
        super().__init__(driver, logger)
        self.menu_button = self.MENU_BUTTON
        self.logout_button = self.LOGOUT_BUTTON
        self.menu_container = self.MENU_CONTAINER

    def click_menu_button(self):
        """Open the hidden menu."""
        self.click(self.menu_button)

    def click_logout_button(self):
        """Click logout button if menu is open."""
        if not self.is_menu_open():
            self.click_menu_button()
        self.click(self.logout_button)

    def is_menu_open(self):
        """Check if menu is currently open."""
        try:
            return self.find_element(self.menu_container).is_displayed()
        except TimeoutException:
            return False