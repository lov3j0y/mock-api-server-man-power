from tests_lib.web_ui.base_test import BaseTest


class TestLoginPage(BaseTest):
    """Test suite for login page functionality."""
    
    LOCKED_OUT_ERROR = "Epic sadface: Sorry, this user has been locked out."
    INVALID_CREDENTIALS_ERROR = "Epic sadface: Username and password do not match any user in this service"

    def test_login_with_valid_credentials(self, setup):
        """Test successful login with valid credentials."""
        # Arrange & Act
        setup("valid_user")
        
        # Assert
        assert "inventory.html" in self.driver.current_url

    def test_login_with_invalid_credentials(self, setup, login_page):
        """Test login failure with invalid credentials."""
        # Arrange & Act  
        setup("invalid_user")
        
        # Assert
        error_message = login_page.get_error_message()
        assert self.INVALID_CREDENTIALS_ERROR in error_message

    def test_login_with_locked_out_user(self, setup, login_page):
        """Test login attempt with locked out user."""
        # Arrange & Act
        setup("locked_out_user")
        
        # Assert
        error_message = login_page.get_error_message()
        assert self.LOCKED_OUT_ERROR in error_message