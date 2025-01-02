import pytest
from tests_lib.helpers.json_loader import JSONLoader
from tests_lib.web_ui.pages.login_page import LoginPage
from tests_lib.web_ui.base_test import login, driver




@pytest.mark.usefixtures("driver")
class TestLoginPage:
    
    @pytest.fixture(autouse=True)
    def setup_credentials(self):
        self.credentials = JSONLoader().load_data("test_data_webui_credentials.json", "credentials")

    def test_login_with_valid_credentials(self, driver):
        # Arrange
        valid_user = self.credentials["valid_user"]
        # Act
        login(valid_user["username"], valid_user["password"], driver)

        # Assert
        assert "inventory.html" in driver.current_url, "The inventory page did not load after login with valid credentials."

    def test_login_with_invalid_credentials(self, driver):
        # Arrange
        invalid_user = self.credentials["invalid_user"]
        login_page = LoginPage(driver)
        
        # Act
        login(invalid_user["username"], invalid_user["password"], driver)
        error = login_page.get_error_message()
        
        # Assert
        assert "Epic sadface: Username and password do not match any user in this service" in error

    def test_login_with_locked_out_user(self, driver):
        # Arrange
        locked_out_user = self.credentials["locked_out_user"]
        login_page = LoginPage(driver)
        
        # Act
        login(locked_out_user["username"], locked_out_user["password"], driver)
        error = login_page.get_error_message()
        
        # Assert
        assert "Epic sadface: Sorry, this user has been locked out." in error
