from selenium.webdriver.common.by import By
from src.core.base_page import BasePage

class CheckoutPage(BasePage):
    FIRST = (By.ID, "first-name")
    LAST = (By.ID, "last-name")
    POSTAL = (By.ID, "postal-code")
    CONTINUE = (By.ID, "continue")

    def fill_and_continue(self, first: str, last: str, postal: str):
        self.type(self.FIRST, first)
        self.type(self.LAST, last)
        self.type(self.POSTAL, postal)
        self.click(self.CONTINUE)
