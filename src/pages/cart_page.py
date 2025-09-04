from selenium.webdriver.common.by import By
from src.core.base_page import BasePage

class CartPage(BasePage):
    CART_ITEMS = (By.CSS_SELECTOR, ".cart_item")
    ITEM_NAME = (By.CSS_SELECTOR, ".inventory_item_name")
    ITEM_PRICE = (By.CSS_SELECTOR, ".inventory_item_price")
    CHECKOUT_BTN = (By.ID, "checkout")

    def items(self):
        elements = self.get_elements(self.CART_ITEMS)
        data = []
        for el in elements:
            name = el.find_element(*self.ITEM_NAME).text.strip()
            price = float(el.find_element(*self.ITEM_PRICE).text.replace("$", ""))
            data.append((name, price))
        return data

    def checkout(self):
        self.click(self.CHECKOUT_BTN)
