from tests_lib.web_ui.pages.base_page import BasePage
from selenium.webdriver.common.by import By


class InventoryPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.cart_link = (By.CSS_SELECTOR, ".shopping_cart_link")
        self.products_title = (By.CLASS_NAME, "title")
        self.inventory_items = (By.CSS_SELECTOR, ".inventory_item")

    def add_to_cart_by_index(self, item_index):
        item_add_to_cart_button = (
            By.CSS_SELECTOR,
            f".inventory_item:nth-child({item_index + 1}) .btn_inventory"
        )
        self.click(item_add_to_cart_button)

    def add_to_cart_by_name(self, product_name):
        item_add_to_cart_button = (
            By.XPATH,
            f"//div[text()='{product_name}']"
            f"/ancestor::div[@class='inventory_item']//button[contains(@class, 'btn_inventory')]"
        )
        self.click(item_add_to_cart_button)

    def click_cart_link(self):
        self.click(self.cart_link)

    def is_inventory_displayed(self):
        return len(self.find_elements(self.inventory_items)) > 0

    def is_page_loaded(self):
        return (
            self.get_text(self.products_title) == "Products"
            and "inventory.html" in self.driver.current_url
        )
