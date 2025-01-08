import pytest
from tests_lib.web_ui.base_test import BaseTest


class TestCartPage(BaseTest):
    """Test suite for shopping cart functionality."""

    @pytest.fixture
    def cart_setup(self, setup, inventory_page):
        """Setup cart state with one item."""
        self.logger.info("=== Setting up cart test environment ===")
        setup()
        self.logger.info("Adding item to cart")
        inventory_page.add_to_cart_by_index(0)
        self.logger.info("Navigating to cart")
        inventory_page.click_cart_link()
        self.logger.info("=== Cart setup completed ===")

    def test_cart_item_displayed(self, cart_setup, cart_page):
        """Test that item is displayed in cart."""
        self.logger.info("=== Starting test_cart_item_displayed ===")
        
        # Arrange & Act
        self.logger.info("Verifying cart item visibility")
        
        # Assert
        assert cart_page.is_cart_item_displayed(), \
            "Item not displayed in cart"
        self.logger.info("=== Completed test_cart_item_displayed ===\n")

    def test_click_checkout(self, cart_setup, cart_page):
        """Test checkout button navigation."""
        self.logger.info("=== Starting test_click_checkout ===")
        
        # Act
        self.logger.info("Clicking checkout button")
        cart_page.click_checkout()
        
        # Assert
        self.logger.info("Verifying navigation to checkout page")
        assert "checkout-step-one.html" in self.driver.current_url, \
            "Not redirected to checkout page"
        self.logger.info("=== Completed test_click_checkout ===\n")

    def test_empty_cart(self, setup, cart_page):
        """Test empty cart state."""
        self.logger.info("=== Starting test_empty_cart ===")
        
        # Arrange
        self.logger.info("Setting up empty cart state")
        setup()
        
        # Assert
        self.logger.info("Verifying cart is empty")
        assert not cart_page.is_cart_item_displayed(), \
            "Cart should be empty initially"
        self.logger.info("=== Completed test_empty_cart ===\n")