import pytest
from tests_lib.web_ui.base_test import BaseTest
from tests_lib.web_ui.pages.checkout_page import CheckoutPage


class TestCheckoutPage(BaseTest):
    """Test suite for checkout functionality."""    
    @pytest.fixture
    def checkout_setup(self, login_page, inventory_page, cart_page):
        """Setup checkout state with item in cart."""
        login_page.login_as("valid_user")
        self.logger.info("Adding item to cart")
        inventory_page.add_to_cart_by_index(0)
        self.logger.info("Navigating to cart")
        inventory_page.click_cart_link()
        self.logger.info("Proceeding to checkout")
        cart_page.click_checkout()

    def test_checkout_page_loaded(self, checkout_setup, checkout_page):
        """Test that checkout page loads correctly."""
        
        # Arrange & Act
        self.logger.info("Verifying checkout page state")
        
        # Assert
        assert checkout_page.is_page_loaded()

    def test_continue_to_next_step(self, checkout_setup, checkout_page):
        """Test that user can continue to next checkout step."""
        
        # Arrange & Act
        self.logger.info("Filling checkout form with test data")
        checkout_page.fill_checkout_form(
            CheckoutPage.customer_data["first_name"],
            CheckoutPage.customer_data["last_name"],
            CheckoutPage.customer_data["postal_code"]
        )
        self.logger.info("Proceeding to next checkout step")
        checkout_page.click_continue()

        # Assert
        self.logger.info("Verifying navigation to next checkout step")
        assert CheckoutPage.STEP_TWO_URL in self.driver.current_url
        
    def test_complete_checkout(self, checkout_setup, checkout_page):
        """Test complete checkout flow."""
        
        # Arrange
        self.logger.info(f"Filling checkout form with: {CheckoutPage.customer_data["first_name"]} {CheckoutPage.customer_data["last_name"]} {CheckoutPage.customer_data["postal_code"]}")
        checkout_page.fill_checkout_form(
            CheckoutPage.customer_data["first_name"],
            CheckoutPage.customer_data["last_name"],
            CheckoutPage.customer_data["postal_code"]
        )
        self.logger.info("Continuing to next step")
        checkout_page.click_continue()

        # Act
        self.logger.info("Completing checkout process")
        checkout_page.click_finish()

        # Assert
        self.logger.info("Verifying checkout completion")
        assert checkout_page.is_checkout_complete(), \
            "Checkout was not completed successfully"

    def test_empty_form_validation(self, checkout_setup, checkout_page):
        """Test validation message for completely empty form."""
        
        # Arrange
        self.logger.info("Verifying checkout page is ready")
        
        # Act
        self.logger.info("Attempting to continue with empty form")
        checkout_page.click_continue()
        
        # Assert
        self.logger.info("Verifying first name validation message")
        assert checkout_page.get_error_message() == checkout_page.ERROR_MESSAGES["first_name"]

    def test_missing_last_name_validation(self, checkout_setup, checkout_page):
        """Test validation message when only first name is provided."""
        
        # Arrange
        self.logger.info(f"Entering first name: {CheckoutPage.customer_data["first_name"]}")
        checkout_page.enter_first_name(CheckoutPage.customer_data["first_name"])
        
        # Act
        self.logger.info("Attempting to continue with missing last name")
        checkout_page.click_continue()
        
        # Assert
        self.logger.info("Verifying last name validation message")
        assert checkout_page.get_error_message() == checkout_page.ERROR_MESSAGES["last_name"]

    def test_missing_postal_code_validation(self, checkout_setup, checkout_page):
        """Test validation message when postal code is missing."""
        
        # Arrange
        self.logger.info(f"Entering first name: {CheckoutPage.customer_data["first_name"]} and last name: {CheckoutPage.customer_data["last_name"]}")
        checkout_page.enter_first_name(CheckoutPage.customer_data["first_name"])
        checkout_page.enter_last_name(CheckoutPage.customer_data["last_name"])
        
        # Act
        self.logger.info("Attempting to continue with missing postal code")
        checkout_page.click_continue()
        
        # Assert
        self.logger.info("Verifying postal code validation message")
        assert checkout_page.get_error_message() == checkout_page.ERROR_MESSAGES["postal_code"]