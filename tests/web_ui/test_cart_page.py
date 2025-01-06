import pytest
from tests_lib.web_ui.base_test import BaseTest


class TestCartPage(BaseTest):
    """Test suite for shopping cart functionality."""

    @pytest.fixture
    def cart_setup(self, setup, inventory_page):
        """Setup cart state with one item."""
        setup()
        inventory_page.add_to_cart_by_index(0)
        inventory_page.click_cart_link()

    def test_cart_item_displayed(self, cart_setup, cart_page):
        """Test that item is displayed in cart."""
        # Assert
        assert cart_page.is_cart_item_displayed(), \
            "Item not displayed in cart"

    def test_click_checkout(self, cart_setup, cart_page):
        """Test checkout button navigation."""
        # Act
        cart_page.click_checkout()
        
        # Assert
        assert "checkout-step-one.html" in self.driver.current_url, \
            "Not redirected to checkout page"

    def test_empty_cart(self, setup, cart_page):
        """Test empty cart state."""
        # Arrange
        setup()
        
        # Assert
        assert not cart_page.is_cart_item_displayed(), \
            "Cart should be empty initially"