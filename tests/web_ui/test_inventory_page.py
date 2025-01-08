from tests_lib.web_ui.base_test import BaseTest


class TestInventoryPage(BaseTest):
    """Test suite for inventory page functionality."""
    
    PRODUCT_NAME = "Sauce Labs Backpack"

    def test_inventory_display(self, setup, inventory_page):
        """Test that inventory items are displayed."""
                
        # Arrange & Act
        self.logger.info("Setting up inventory page")
        setup()
        
        # Assert
        self.logger.info("Verifying inventory items are displayed")
        assert inventory_page.is_inventory_displayed(), \
            "Inventory items are not displayed"

    def test_add_to_cart_by_index(self, setup, inventory_page, cart_page):
        """Test adding item to cart by index."""
        
        # Arrange
        self.logger.info("Setting up inventory page")
        setup()
        
        # Act
        self.logger.info("Adding first item to cart")
        inventory_page.add_to_cart_by_index(0)
        self.logger.info("Navigating to cart")
        inventory_page.click_cart_link()

        # Assert
        self.logger.info("Verifying item was added to cart")
        assert cart_page.is_cart_item_displayed(), \
            "Item was not added to cart"

    def test_add_to_cart_by_name(self, setup, inventory_page):
        """Test adding item to cart by name."""
        
        # Arrange
        self.logger.info("Setting up inventory page")
        setup()
        
        # Act
        self.logger.info(f"Adding item '{self.PRODUCT_NAME}' to cart")
        inventory_page.add_to_cart_by_name(self.PRODUCT_NAME)