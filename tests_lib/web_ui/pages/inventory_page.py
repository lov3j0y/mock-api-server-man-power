from tests_lib.web_ui.pages.base_page import BasePage
from selenium.webdriver.common.by import By


class InventoryPage(BasePage):
    PRODUCTS_TITLE = "Products"
    INVENTORY_PATH = "inventory.html"
    
    def __init__(self, driver, logger):
        super().__init__(driver, logger)
        self.cart_link = (By.CSS_SELECTOR, ".shopping_cart_link")
        self.products_title = (By.CLASS_NAME, "title")
        self.inventory_items = (By.CSS_SELECTOR, ".inventory_item")

    def _validate_inventory_items(self):
        """Validates inventory items presence on the page."""
        if not self.find_elements(self.inventory_items):
            raise ValueError("No inventory items found. Please check if you're on the correct page.")

    def add_to_cart_by_index(self, item_index):
        """Adds an item to cart using its index."""
        inventory_items = self.find_elements(self.inventory_items)
        if not inventory_items:
            raise ValueError("No inventory items found on the page")
        
        if not (0 <= item_index < len(inventory_items)):
            raise IndexError(f"Item index {item_index} is out of range.")

        item_add_to_cart_button = (
            By.XPATH,
            f"(//div[contains(@class, 'inventory_item')])[{item_index + 1}]//button[text()='Add to cart']"
        )
        
        if not self.find_elements(item_add_to_cart_button):
            raise ValueError(
                f"Add to cart button not found for item #{item_index + 1}. "
                "Item might be already in cart."
            )
            
        self.click(item_add_to_cart_button)

    def add_to_cart_by_name(self, product_name):
        """Adds an item to cart using its name."""
        self._validate_inventory_items()
            
        formatted_name = product_name.lower().replace(" ", "-")
        item_add_to_cart_button = (
            By.CSS_SELECTOR,
            f'[data-test="add-to-cart-{formatted_name}"]'
        )
        
        if not self.find_elements(item_add_to_cart_button):
            raise ValueError(
                f"Add to cart button not found for '{product_name}'. "
                "Item might be already in cart."
            )
            
        self.click(item_add_to_cart_button)

    def click_cart_link(self):
        """Navigates to cart page."""
        if not self.find_elements(self.cart_link):
            raise ValueError("Cart link is not accessible. Please check if you're logged in.")
            
        self.click(self.cart_link)

    def is_inventory_displayed(self):
        """Checks if inventory items are visible."""
        return len(self.find_elements(self.inventory_items)) > 0

    def is_page_loaded(self):
        """Verifies if inventory page is loaded."""
        return (
            self.get_text(self.products_title) == self.PRODUCTS_TITLE
            and self.INVENTORY_PATH in self.driver.current_url
        )