from tests_lib.web_ui.base_test import BaseTest, WebUIConfig


class TestHiddenMenu(BaseTest):
    """Test suite for hidden menu functionality."""

    def test_open_menu(self, setup, hidden_menu_page):
        """Test that menu opens correctly."""
        self.logger.info("=== Starting test_open_menu ===")
        
        # Arrange
        self.logger.info("Setting up test environment")
        setup()
        
        # Act
        self.logger.info("Opening hidden menu")
        hidden_menu_page.click_menu_button()
        
        # Assert
        self.logger.info("Verifying menu is open")
        assert hidden_menu_page.is_menu_open(), \
            "Menu did not open correctly"
        self.logger.info("=== Completed test_open_menu ===")

    def test_logout(self, setup, hidden_menu_page):
        """Test logout functionality."""
        self.logger.info("=== Starting test_logout ===")
        
        # Arrange
        self.logger.info("Setting up test environment")
        setup()
        
        # Act
        self.logger.info("Opening hidden menu")
        hidden_menu_page.click_menu_button()
        self.logger.info("Clicking logout button")
        hidden_menu_page.click_logout_button()
        
        # Assert
        self.logger.info("Verifying redirection to login page")
        assert self.driver.current_url == WebUIConfig.BASE_URL, \
            "User not redirected to login page after logout"
        self.logger.info("=== Completed test_logout ===")