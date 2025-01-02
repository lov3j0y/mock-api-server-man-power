from tests_lib.web_ui.pages.base_page import BasePage
from selenium.webdriver.common.by import By


class CartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.cart_item = (By.CSS_SELECTOR, ".cart_item")
        self.checkout_button = (By.CSS_SELECTOR, "#checkout")

    def is_cart_item_displayed(self):
        return self.find_element(self.cart_item).is_displayed()

    def click_checkout(self):
        self.click(self.checkout_button)
