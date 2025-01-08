from tests_lib.web_ui.pages.login_page import LoginPage
from tests_lib.web_ui.pages.inventory_page import InventoryPage
from tests_lib.web_ui.pages.cart_page import CartPage
from tests_lib.web_ui.pages.checkout_page import CheckoutPage
from tests_lib.web_ui.pages.hidden_menu_page import HiddenMenuPage

class PageFactory:
    def __init__(self, driver, logger):
        self.driver = driver
        self.logger = logger
    
    def get_login_page(self):
        return LoginPage(self.driver, self.logger)
    
    def get_inventory_page(self):
        return InventoryPage(self.driver, self.logger)
    
    def get_cart_page(self):
        return CartPage(self.driver, self.logger)
    
    def get_checkout_page(self):
        return CheckoutPage(self.driver, self.logger)
    
    def get_hidden_menu_page(self):
        return HiddenMenuPage(self.driver, self.logger)