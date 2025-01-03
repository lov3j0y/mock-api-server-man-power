import pytest
from tests_lib.helpers.json_loader import JSONLoader
from tests_lib.web_ui.pages.inventory_page import InventoryPage
from tests_lib.web_ui.pages.cart_page import CartPage
from tests_lib.web_ui.base_test import login, driver

LOGIN_URL = "https://www.saucedemo.com/"
CHECKOUT_URL = "https://www.saucedemo.com/checkout-step-one.html"

@pytest.mark.usefixtures("driver")
class TestCartPage:

    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.credentials = JSONLoader().load_data("test_data_webui_credentials.json", "credentials")
        valid_user = self.credentials["valid_user"]
        self.login_and_add_item_to_cart(valid_user["username"], valid_user["password"], driver)

    def login_and_add_item_to_cart(self, username, password, driver):
        login(username, password, driver)
        inventory_page = InventoryPage(driver)
        inventory_page.add_to_cart_by_index(0)
        inventory_page.click_cart_link()

    def test_cart_item_displayed(self, driver):
        """Test that the item is displayed in the cart."""
        cart_page = CartPage(driver)
        assert cart_page.is_cart_item_displayed(), "The item was not displayed in the cart."

    def test_click_checkout(self, driver):
        """Test that clicking the checkout button redirects to the checkout page."""
        cart_page = CartPage(driver)
        cart_page.click_checkout()
        assert driver.current_url == CHECKOUT_URL, "The checkout page did not load after clicking checkout."