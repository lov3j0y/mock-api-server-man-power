import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from tests_lib.web_ui.pages.login_page import LoginPage

@pytest.fixture()
def driver():
    browser = os.getenv("BROWSER", "firefox")
    if browser == "firefox":
        options = FirefoxOptions()
    elif browser == "chrome":
        options = ChromeOptions()
    else:
        raise ValueError(f"Unsupported browser: {browser}")

    
    options.add_argument("--headless")
    driver = webdriver.Remote(
        command_executor='http://selenium-hub:4444',
        options=options        
    )
    
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


def login(username, password, driver):
    driver.get("https://www.saucedemo.com/")
    login_page = LoginPage(driver)
    login_page.input_username(username)
    login_page.input_password(password)
    login_page.click_login_button()

    
