from tests_lib.web_ui.base_test import BaseTest


class TestInventoryPage(BaseTest):
    """Test suite for inventory page functionality."""
    
    PRODUCT_NAME = "Sauce Labs Backpack"

    def test_inventory_display(self, setup, inventory_page):
        """Test that inventory items are displayed."""
        # Arrange & Act
        setup()
        
        # Assert
        assert inventory_page.is_inventory_displayed(), \
            "Inventory items are not displayed"

    def test_add_to_cart_by_index(self, setup, inventory_page, cart_page):
        """Test adding item to cart by index."""
        # Arrange
        setup()
        
        # Act
        inventory_page.add_to_cart_by_index(0)
        inventory_page.click_cart_link()

        # Assert
        assert cart_page.is_cart_item_displayed(), \
            "Item was not added to cart"

    def test_add_to_cart_by_name(self, setup, inventory_page, cart_page):
        """Test adding item to cart by name."""
        # Arrange
        setup()
        
        # Act
        inventory_page.add_to_cart_by_name(self.PRODUCT_NAME)
        inventory_page.click_cart_link()

        # Assert
        assert cart_page.is_cart_item_displayed(), \
            "Item was not added to cart"