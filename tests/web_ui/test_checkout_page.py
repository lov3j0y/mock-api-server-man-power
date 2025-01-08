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
        self.logger.info("=== Setting up checkout test environment ===")
        setup()
        self.logger.info("Adding item to cart")
        inventory_page.add_to_cart_by_index(0)
        self.logger.info("Navigating to cart")
        inventory_page.click_cart_link()
        self.logger.info("Proceeding to checkout")
        cart_page.click_checkout()
        self.logger.info("=== Checkout setup completed ===")

    def test_checkout_page_loaded(self, checkout_setup, checkout_page):
        """Test that checkout page loads correctly."""
        self.logger.info("=== Starting test_checkout_page_loaded ===")
        
        # Arrange & Act
        self.logger.info("Verifying checkout page state")
        
        # Assert
        assert checkout_page.is_page_loaded(), \
            "Checkout page did not load correctly"
        self.logger.info("=== Completed test_checkout_page_loaded ===")

    def test_continue_to_next_step(self, checkout_setup, checkout_page):
        """Test that user can continue to next checkout step."""
        self.logger.info("=== Starting test_continue_to_next_step ===")
        
        # Arrange & Act
        self.logger.info("Filling checkout form with test data")
        checkout_page.fill_checkout_form(
            self.FIRST_NAME,
            self.LAST_NAME,
            self.POSTAL_CODE
        )
        self.logger.info("Proceeding to next checkout step")
        checkout_page.click_continue()

        # Assert
        self.logger.info("Verifying navigation to next checkout step")
        assert "checkout-step-two.html" in self.driver.current_url, \
            "Not redirected to next checkout step"
        self.logger.info("=== Completed test_continue_to_next_step ===")
        
    def test_complete_checkout(self, checkout_setup, checkout_page):
        """Test complete checkout flow."""
        self.logger.info("=== Starting test_complete_checkout ===")
        
        # Arrange
        self.logger.info(f"Filling checkout form with: {self.FIRST_NAME} {self.LAST_NAME} {self.POSTAL_CODE}")
        checkout_page.fill_checkout_form(
            self.FIRST_NAME,
            self.LAST_NAME,
            self.POSTAL_CODE
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
        self.logger.info("=== Completed test_complete_checkout ===")

    def test_empty_form_validation(self, checkout_setup, checkout_page):
        """Test validation message for completely empty form."""
        self.logger.info("=== Starting test_empty_form_validation ===")
        
        # Arrange
        self.logger.info("Verifying checkout page is ready")
        
        # Act
        self.logger.info("Attempting to continue with empty form")
        checkout_page.click_continue()
        
        # Assert
        self.logger.info("Verifying first name validation message")
        assert checkout_page.get_error_message() == checkout_page.ERROR_MESSAGES["first_name"]
        self.logger.info("=== Completed test_empty_form_validation ===")

    def test_missing_last_name_validation(self, checkout_setup, checkout_page):
        """Test validation message when only first name is provided."""
        self.logger.info("=== Starting test_missing_last_name_validation ===")
        
        # Arrange
        self.logger.info(f"Entering first name: {self.FIRST_NAME}")
        checkout_page.enter_first_name(self.FIRST_NAME)
        
        # Act
        self.logger.info("Attempting to continue with missing last name")
        checkout_page.click_continue()
        
        # Assert
        self.logger.info("Verifying last name validation message")
        assert checkout_page.get_error_message() == checkout_page.ERROR_MESSAGES["last_name"]
        self.logger.info("=== Completed test_missing_last_name_validation ===")

    def test_missing_postal_code_validation(self, checkout_setup, checkout_page):
        """Test validation message when postal code is missing."""
        self.logger.info("=== Starting test_missing_postal_code_validation ===")
        
        # Arrange
        self.logger.info(f"Entering first name: {self.FIRST_NAME} and last name: {self.LAST_NAME}")
        checkout_page.enter_first_name(self.FIRST_NAME)
        checkout_page.enter_last_name(self.LAST_NAME)
        
        # Act
        self.logger.info("Attempting to continue with missing postal code")
        checkout_page.click_continue()
        
        # Assert
        self.logger.info("Verifying postal code validation message")
        assert checkout_page.get_error_message() == checkout_page.ERROR_MESSAGES["postal_code"]
        self.logger.info("=== Completed test_missing_postal_code_validation ===")