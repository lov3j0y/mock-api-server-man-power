from tests_lib.web_ui.base_test import BaseTest, TestConfig


class TestHiddenMenu(BaseTest):
    """Test suite for hidden menu functionality."""

    def test_open_menu(self, setup, hidden_menu_page):
        """Test that menu opens correctly."""
        # Arrange
        setup()
        
        # Act
        hidden_menu_page.click_menu_button()
        
        # Assert
        assert hidden_menu_page.is_menu_open(), \
            "Menu did not open correctly"

    def test_logout(self, setup, hidden_menu_page):
        """Test logout functionality."""
        # Arrange
        setup()
        
        # Act
        hidden_menu_page.click_menu_button()
        hidden_menu_page.click_logout_button()
        
        # Assert
        assert self.driver.current_url == TestConfig.BASE_URL, \
            "User not redirected to login page after logout"