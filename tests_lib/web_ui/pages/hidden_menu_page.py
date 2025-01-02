from tests_lib.web_ui.pages.base_page import BasePage
from selenium.webdriver.common.by import By


class HiddenMenuPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.menu_button = (By.CSS_SELECTOR, ".bm-burger-button")
        self.logout_button = (By.ID, "logout_sidebar_link")
        self.menu_container = (By.CLASS_NAME, "bm-menu-wrap")  # Container for the menu

    def click_menu_button(self):
        self.click(self.menu_button)

    def click_logout_button(self):
        self.click(self.logout_button)

    def is_menu_open(self):
        return self.find_element(self.logout_button).is_displayed()
