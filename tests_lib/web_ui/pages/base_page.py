from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def find_element(self, by):
        return self.wait.until(EC.visibility_of_element_located(by))

    def find_elements(self, by):
        return self.driver.find_elements(*by)

    def click(self, by):
        self.find_element(by).click()

    def type(self, by, text):
        element = self.find_element(by)
        element.clear()
        element.send_keys(text)

    def get_text(self, by):
        return self.find_element(by).text
