from tests_lib.web_ui.base_test import BaseTest


class TestLoginPage(BaseTest):
    """Test suite for login page functionality."""
    
    LOCKED_OUT_ERROR = "Epic sadface: Sorry, this user has been locked out."
    INVALID_CREDENTIALS_ERROR = "Epic sadface: Username and password do not match any user in this service"

    def test_login_with_valid_credentials(self, setup):
        """Test successful login with valid credentials."""
        self.logger.info("=== Starting test_login_with_valid_credentials ===")
        
        # Arrange
        self.logger.info("Arranging test data for valid user login")
        setup("valid_user")
        
        # Act
        self.logger.info("Performing login action")
        current_url = self.driver.current_url
        
        # Assert
        self.logger.info("Verifying successful login navigation")
        assert "inventory.html" in current_url
        self.logger.info("=== Completed test_login_with_valid_credentials ===")

    def test_login_with_invalid_credentials(self, setup, login_page):
        """Test login failure with invalid credentials."""
        self.logger.info("=== Starting test_login_with_invalid_credentials ===")
        
        # Arrange
        self.logger.info("Arranging test data for invalid user login")
        setup("invalid_user")
        
        # Act
        self.logger.info("Getting error message after failed login")
        error_message = login_page.get_error_message()
        
        # Assert
        self.logger.info("Verifying error message for invalid credentials")
        assert self.INVALID_CREDENTIALS_ERROR in error_message
        self.logger.info("=== Completed test_login_with_invalid_credentials ===")

    def test_login_with_locked_out_user(self, setup, login_page):
        """Test login attempt with locked out user."""
        self.logger.info("=== Starting test_login_with_locked_out_user ===")
        
        # Arrange
        self.logger.info("Arranging test data for locked out user")
        setup("locked_out_user")
        
        # Act
        self.logger.info("Getting error message after locked out user login attempt")
        error_message = login_page.get_error_message()
        
        # Assert
        self.logger.info("Verifying locked out user error message")
        assert self.LOCKED_OUT_ERROR in error_message
        self.logger.info("=== Completed test_login_with_locked_out_user ===")