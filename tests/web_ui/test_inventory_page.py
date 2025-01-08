from tests_lib.web_ui.base_test import BaseTest
from tests_lib.web_ui.pages.inventory_page import InventoryPage


class TestInventoryPage(BaseTest):
    """Test suite for inventory page functionality."""
    
    def test_inventory_display(self, login_page, inventory_page):
        """Test that inventory items are displayed."""
                
        # Arrange & Act
        self.logger.info("Setting up inventory page")
        login_page.login_as("valid_user")
        
        # Assert
        self.logger.info("Verifying inventory items are displayed")
        assert inventory_page.is_inventory_displayed()

    def test_add_to_cart_by_index(self, login_page, inventory_page, cart_page):
        """Test adding item to cart by index."""
        
        # Arrange
        self.logger.info("Setting up inventory page")
        login_page.login_as("valid_user")
        
        # Act
        self.logger.info("Adding first item to cart")
        inventory_page.add_to_cart_by_index(0)
        self.logger.info("Navigating to cart")
        inventory_page.click_cart_link()

        # Assert
        self.logger.info("Verifying item was added to cart")
        assert cart_page.is_cart_item_displayed()

    def test_add_to_cart_by_name(self, login_page, inventory_page):
        """Test adding item to cart by name."""
        
        # Arrange
        self.logger.info("Setting up inventory page")
        login_page.login_as("valid_user")
        
        # Act
        self.logger.info(f"Adding item '{InventoryPage.PRODUCT_BACKPACK_NAME}' to cart")
        inventory_page.add_to_cart_by_name(InventoryPage.PRODUCT_BACKPACK_NAME)