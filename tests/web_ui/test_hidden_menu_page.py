import pytest
from tests_lib.helpers.json_loader import JSONLoader
from tests_lib.web_ui.pages.hidden_menu_page import HiddenMenuPage
from tests_lib.web_ui.base_test import login, driver

LOGIN_URL = "https://www.saucedemo.com/"

@pytest.mark.usefixtures("driver")
class TestHiddenMenu:

    @pytest.fixture(autouse=True)
    def setup(self, driver):
        """Setup test by logging in"""
        self.credentials = JSONLoader().load_data("test_data_webui_credentials.json", "credentials")
        valid_user = self.credentials["valid_user"]
        login(valid_user["username"], valid_user["password"], driver)

    def test_open_menu(self, driver):
        """Test that menu opens correctly"""
        hidden_menu_page = HiddenMenuPage(driver)
        hidden_menu_page.click_menu_button()
        
        assert hidden_menu_page.is_menu_open(), \
            "Menu did not open correctly"

    def test_logout(self, driver):
        """Test logout functionality"""
        hidden_menu_page = HiddenMenuPage(driver)
        hidden_menu_page.click_menu_button()
        hidden_menu_page.click_logout_button()
        
        assert driver.current_url == LOGIN_URL, \
            "User not redirected to login page after logout"