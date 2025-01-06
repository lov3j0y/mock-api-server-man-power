import os
import pytest
import logging
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.common.exceptions import WebDriverException
from tests_lib.web_ui.pages.login_page import LoginPage


class TestConfig:
    """Test configuration constants."""
    BASE_URL = "https://www.saucedemo.com/"
    IMPLICIT_WAIT = 10
    SELENIUM_HUB = "http://selenium-hub:4444"


@pytest.fixture()
def driver():
    """Create WebDriver instance with configured options."""
    browser = os.getenv("BROWSER", "firefox")
    
    if browser == "firefox":
        options = FirefoxOptions()
    elif browser == "chrome":
        options = ChromeOptions()
    else:
        raise ValueError(f"Unsupported browser: {browser}")

    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    
    driver = webdriver.Remote(
        command_executor=TestConfig.SELENIUM_HUB,
        options=options        
    )
    driver.implicitly_wait(TestConfig.IMPLICIT_WAIT)
    
    yield driver
    driver.quit()


def login(username, password, driver):
    driver.get(TestConfig.BASE_URL)
    login_page = LoginPage(driver)
    login_page.input_username(username)
    login_page.input_password(password)
    login_page.click_login_button()