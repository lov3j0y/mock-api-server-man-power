from tests_lib.web_ui.base_test import BaseTest
from tests_lib.web_ui.pages.inventory_page import InventoryPage
from tests_lib.web_ui.pages.login_page import LoginPage


class TestLoginPage(BaseTest):
    """Test suite for login page functionality."""

    def test_login_with_valid_credentials(self, setup):
        """Test successful login with valid credentials."""
        
        # Arrange
        self.logger.info("Arranging test data for valid user login")
        setup("valid_user")
        
        # Act
        self.logger.info("Performing login action")
        current_url = self.driver.current_url
        
        # Assert
        self.logger.info("Verifying successful login navigation")
        assert InventoryPage.INVENTORY_PATH in current_url

    def test_login_with_invalid_credentials(self, setup):
        """Test login failure with invalid credentials."""
        
        # Arrange
        self.logger.info("Arranging test data for invalid user login")
        setup("invalid_user")
        
        # Act
        self.logger.info("Getting error message after failed login")
        error_message = self.pages.get_login_page().get_error_message()
        
        # Assert
        self.logger.info("Verifying error message for invalid credentials")
        assert LoginPage.INVALID_CREDENTIALS_ERROR in error_message

    def test_login_with_locked_out_user(self, setup):
        """Test login attempt with locked out user."""
        
        # Arrange
        self.logger.info("Arranging test data for locked out user")
        setup("locked_out_user")
        
        # Act
        self.logger.info("Getting error message after locked out user login attempt")
        error_message = self.pages.get_login_page().get_error_message()
        
        # Assert
        self.logger.info("Verifying locked out user error message")
        assert LoginPage.LOCKED_OUT_ERROR in error_message