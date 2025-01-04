import pytest
from tests_lib.helpers.json_loader import JSONLoader
from tests_lib.web_ui.pages.inventory_page import InventoryPage
from tests_lib.web_ui.pages.cart_page import CartPage
from tests_lib.web_ui.base_test import login, driver

PRODUCT_NAME = "Sauce Labs Backpack"

@pytest.mark.usefixtures("driver")
class TestInventoryPage:

    @pytest.fixture(autouse=True)
    def setup(self, driver):
        """Setup test by logging in"""
        self.credentials = JSONLoader().load_data("test_data_webui_credentials.json", "credentials")
        valid_user = self.credentials["valid_user"]
        login(valid_user["username"], valid_user["password"], driver)

    def test_inventory_display(self, driver):
        """Test that inventory items are displayed"""
        inventory_page = InventoryPage(driver)
        assert inventory_page.is_inventory_displayed(), \
            "Inventory items are not displayed"

    def test_add_to_cart_by_index(self, driver):
        """Test adding item to cart by index"""
        inventory_page = InventoryPage(driver)
        inventory_page.add_to_cart_by_index(0)
        inventory_page.click_cart_link()

        cart_page = CartPage(driver)
        assert cart_page.is_cart_item_displayed(), \
            "Item was not added to cart"

    def test_add_to_cart_by_name(self, driver):
        """Test adding item to cart by name"""
        inventory_page = InventoryPage(driver)
        inventory_page.add_to_cart_by_name(PRODUCT_NAME)
        inventory_page.click_cart_link()

        cart_page = CartPage(driver)
        assert cart_page.is_cart_item_displayed(), \
            "Item was not added to cart"

    def test_page_title(self, driver):
        """Test that inventory page loads correctly"""
        inventory_page = InventoryPage(driver)
        assert inventory_page.is_page_loaded(), \
            "Inventory page did not load correctly"