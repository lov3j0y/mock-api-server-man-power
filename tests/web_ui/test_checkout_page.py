import pytest
from tests_lib.web_ui.base_test import BaseTest


class TestCheckoutPage(BaseTest):
    """Test suite for checkout functionality."""
    FIRST_NAME = "John"
    LAST_NAME = "Doe"
    POSTAL_CODE = "12345"
    
    @pytest.fixture
    def checkout_setup(self, setup, inventory_page, cart_page):
        """Setup checkout state with item in cart."""
        setup()
        inventory_page.add_to_cart_by_index(0)
        inventory_page.click_cart_link()
        cart_page.click_checkout()

    def test_checkout_page_loaded(self, checkout_setup, checkout_page):
        """Test that checkout page loads correctly."""
        assert checkout_page.is_page_loaded(), \
            "Checkout page did not load correctly"

    def test_continue_to_next_step(self, checkout_setup, checkout_page):
        """Test that user can continue to next checkout step."""
        # Act
        checkout_page.fill_checkout_form(
            self.FIRST_NAME,
            self.LAST_NAME,
            self.POSTAL_CODE
        )
        checkout_page.click_continue()

        # Assert
        assert "checkout-step-two.html" in self.driver.current_url, \
            "Not redirected to next checkout step"

    def test_complete_checkout(self, checkout_setup, checkout_page):
        """Test complete checkout flow."""
        # Arrange
        checkout_page.fill_checkout_form(
            self.FIRST_NAME,
            self.LAST_NAME,
            self.POSTAL_CODE
        )
        checkout_page.click_continue()

        # Act
        checkout_page.click_finish()

        # Assert
        assert checkout_page.is_checkout_complete(), \
            "Checkout was not completed successfully"
            
            
    def test_empty_form_validation(self, checkout_setup, checkout_page):
        """Test validation message for completely empty form."""
        # Act
        checkout_page.click_continue()
        
        # Assert
        assert checkout_page.get_error_message() == checkout_page.ERROR_MESSAGES["first_name"]

    def test_missing_last_name_validation(self, checkout_setup, checkout_page):
        """Test validation message when only first name is provided."""
        # Arrange
        checkout_page.enter_first_name(self.FIRST_NAME)
        
        # Act
        checkout_page.click_continue()
        
        # Assert
        assert checkout_page.get_error_message() == checkout_page.ERROR_MESSAGES["last_name"]

    def test_missing_postal_code_validation(self, checkout_setup, checkout_page):
        """Test validation message when postal code is missing."""
        # Arrange
        checkout_page.enter_first_name(self.FIRST_NAME)
        checkout_page.enter_last_name(self.LAST_NAME)
        
        # Act
        checkout_page.click_continue()
        
        # Assert
        assert checkout_page.get_error_message() == checkout_page.ERROR_MESSAGES["postal_code"]