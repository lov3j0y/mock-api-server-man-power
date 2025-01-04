import pytest
from tests_lib.helpers.json_loader import JSONLoader
from tests_lib.web_ui.pages.inventory_page import InventoryPage
from tests_lib.web_ui.pages.cart_page import CartPage
from tests_lib.web_ui.pages.checkout_page import CheckoutPage
from tests_lib.web_ui.base_test import login, driver

CHECKOUT_STEP_ONE_URL = "https://www.saucedemo.com/checkout-step-two.html"
CHECKOUT_COMPLETE_URL = "https://www.saucedemo.com/checkout-complete.html"

@pytest.mark.usefixtures("driver")
class TestCheckoutPage:

    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.credentials = JSONLoader().load_data("test_data_webui_credentials.json", "credentials")
        valid_user = self.credentials["valid_user"]
        self.login_and_setup_checkout(valid_user["username"], valid_user["password"], driver)

    def login_and_setup_checkout(self, username, password, driver):
        """Helper method to login and setup checkout state"""
        login(username, password, driver)
        inventory_page = InventoryPage(driver)
        inventory_page.add_to_cart_by_index(0)
        inventory_page.click_cart_link()
        cart_page = CartPage(driver)
        cart_page.click_checkout()

    def test_checkout_page_loaded(self, driver):
        """Test that checkout page loads correctly."""
        checkout_page = CheckoutPage(driver)
        assert checkout_page.is_page_loaded(), "Checkout page did not load correctly"

    def test_continue_to_next_step(self, driver):
        """Test that user can continue to next checkout step."""
        checkout_page = CheckoutPage(driver)
        checkout_page.enter_first_name("John")
        checkout_page.enter_last_name("Doe")
        checkout_page.enter_postal_code("12345")
        checkout_page.click_continue()
        
        assert CHECKOUT_STEP_ONE_URL in driver.current_url, \
            "Failed to proceed to next checkout step"

    def test_complete_order(self, driver):
        """Test complete checkout process."""
        checkout_page = CheckoutPage(driver)
        checkout_page.enter_first_name("John")
        checkout_page.enter_last_name("Doe")
        checkout_page.enter_postal_code("12345")
        checkout_page.click_continue()
        checkout_page.click_finish()

        assert CHECKOUT_COMPLETE_URL in driver.current_url, \
            "Failed to reach order completion page"
        assert checkout_page.is_checkout_complete(), \
            "Order completion message not displayed"