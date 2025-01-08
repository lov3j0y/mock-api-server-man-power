from tests_lib.web_ui.config.web_ui_config import WebUIConfig
from tests_lib.web_ui.pages.base_page import BasePage
from selenium.webdriver.common.by import By


class InventoryPage(BasePage):
    """Page object for inventory functionality."""
    locators = WebUIConfig.PAGES["inventory"]["locators"]
    constants = WebUIConfig.PAGES["inventory"]["constants"]
    errors = WebUIConfig.COMMON["messages"]["errors"]["inventory"]    
    INVENTORY_PATH = WebUIConfig.COMMON["paths"]["inventory"]
    
    # Page locators
    CART_LINK = (By.ID, locators["cart_link"])
    INVENTORY_ITEMS = (By.CSS_SELECTOR, locators["inventory_items"])
    PRODUCTS_TITLE = (By.CSS_SELECTOR, locators["products_title"])
    
    # Page constants
    PRODUCTS_TITLE_TEXT = constants["products_title_text"]
    PRODUCT_BACKPACK_NAME = constants["products"]["backpack_name"]

    def __init__(self, driver, logger):
        super().__init__(driver, logger)
        self.cart_link = self.CART_LINK
        self.inventory_items = self.INVENTORY_ITEMS
        self.products_title = self.PRODUCTS_TITLE
        self.logger.info("Inventory page initialized")

    def _validate_inventory_items(self):
        """Validates inventory items presence on the page."""
        if not self.find_elements(self.inventory_items):
            raise ValueError(self.errors["no_items"])

    def add_to_cart_by_index(self, item_index):
        """Adds an item to cart using its index."""
        inventory_items = self.find_elements(self.inventory_items)
        if not inventory_items:
            raise ValueError(self.errors["no_items"])
        
        if not (0 <= item_index < len(inventory_items)):
            raise IndexError(self.errors["index_range"].format(index=item_index))

        item_add_to_cart_button = (
            By.XPATH,
            self.locators["item_xpath"].format(index=item_index + 1)
        )
        
        if not self.find_elements(item_add_to_cart_button):
            raise ValueError(self.errors["item_in_cart"].format(item=f"#{item_index + 1}"))
            
        self.click(item_add_to_cart_button)

    def add_to_cart_by_name(self, product_name):
        """Adds an item to cart using its name."""
        self._validate_inventory_items()
            
        formatted_name = product_name.lower().replace(" ", "-")
        item_add_to_cart_button = (
            By.CSS_SELECTOR,
            f'[data-test="{self.locators["item_data_test"].format(name=formatted_name)}"]'
        )
        
        if not self.find_elements(item_add_to_cart_button):
            raise ValueError(self.errors["item_in_cart"].format(item=product_name))
            
        self.click(item_add_to_cart_button)

    def click_cart_link(self):
        """Navigates to cart page."""
        if not self.find_elements(self.cart_link):
            raise ValueError(self.errors["cart_inaccessible"])
            
        self.click(self.cart_link)

    def is_inventory_displayed(self):
        """Checks if inventory items are visible."""
        return len(self.find_elements(self.inventory_items)) > 0

    def is_page_loaded(self):
        """Verifies if inventory page is loaded."""
        return (
            self.get_text(self.products_title) == self.PRODUCTS_TITLE_TEXT
            and self.INVENTORY_PATH in self.driver.current_url
        )