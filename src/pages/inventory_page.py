from selenium.webdriver.common.by import By
from src.core.base_page import BasePage

class InventoryPage(BasePage):
    TITLE = (By.CSS_SELECTOR, "span.title")
    CART_BADGE = (By.CSS_SELECTOR, ".shopping_cart_badge")
    CART_LINK = (By.CSS_SELECTOR, "a.shopping_cart_link")
    INVENTORY_ITEMS = (By.CSS_SELECTOR, ".inventory_item")
    ITEM_NAMES = (By.CSS_SELECTOR, ".inventory_item_name")
    ITEM_PRICES = (By.CSS_SELECTOR, ".inventory_item_price")
    SORT_SELECT = (By.CSS_SELECTOR, ".product_sort_container")

    def cart_count(self) -> int:
        return int(self.get_text(self.CART_BADGE)) if self.is_visible(self.CART_BADGE) else 0

    def add_to_cart_buttons(self):
        return self.get_elements((By.XPATH, "//button[contains(@id,'add-to-cart-')]") )

    def remove_buttons(self):
        return self.get_elements((By.XPATH, "//button[contains(@id,'remove-')]") )

    def product_cards(self):
        return self.get_elements(self.INVENTORY_ITEMS)

    def product_list(self):
        names = [e.text.strip() for e in self.get_elements(self.ITEM_NAMES)]
        prices = [float(e.text.replace("$", "")) for e in self.get_elements(self.ITEM_PRICES)]
        return list(zip(names, prices))

    def open_cart(self):
        self.click(self.CART_LINK)

    def sort_by(self, visible_text: str):
        from selenium.webdriver.support.ui import Select
        Select(self.wait.visible(self.SORT_SELECT)).select_by_visible_text(visible_text)
