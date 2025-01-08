from tests_lib.web_ui.base_test import BaseTest, WebUIConfig


class TestHiddenMenu(BaseTest):
    """Test suite for hidden menu functionality."""

    def test_open_menu(self, login_page, hidden_menu_page):
        """Test that menu opens correctly."""
        self.logger.info("=== Starting test_open_menu ===")
        
        # Arrange
        self.logger.info("Setting up test environment")
        login_page.login_as("valid_user")
        
        # Act
        self.logger.info("Opening hidden menu")
        hidden_menu_page.click_menu_button()
        
        # Assert
        self.logger.info("Verifying menu is open")
        assert hidden_menu_page.is_menu_open()

    def test_logout(self, login_page, hidden_menu_page):
        """Test logout functionality."""
        
        # Arrange
        self.logger.info("Setting up test environment")
        login_page.login_as("valid_user")
        
        # Act
        self.logger.info("Opening hidden menu")
        hidden_menu_page.click_menu_button()
        self.logger.info("Clicking logout button")
        hidden_menu_page.click_logout_button()
        
        # Assert
        self.logger.info("Verifying redirection to login page")
        assert self.driver.current_url == WebUIConfig.BASE_URL