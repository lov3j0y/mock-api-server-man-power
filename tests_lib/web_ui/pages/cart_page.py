from tests_lib.web_ui.config.web_ui_config import WebUIConfig
from tests_lib.web_ui.pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


class CartPage(BasePage):
    """Page object for the shopping cart page."""
    locators = WebUIConfig.PAGES["cart"]["locators"]
    
    # Page locators
    CART_ITEM = (By.CSS_SELECTOR, locators["cart_item"])
    CHECKOUT_BUTTON = (By.ID, locators["checkout_button"])

    def __init__(self, driver, logger):
        super().__init__(driver, logger)
        self.cart_item = self.CART_ITEM
        self.checkout_button = self.CHECKOUT_BUTTON

    def is_cart_item_displayed(self):
        """Check if cart has any items."""
        try:
            return self.find_element(self.cart_item).is_displayed()
        except TimeoutException:
            return False

    def click_checkout(self):
        """Click checkout button."""
        self.click(self.checkout_button)

    def get_cart_items_count(self):
        """Return number of items in cart."""
        return len(self.find_elements(self.cart_item))