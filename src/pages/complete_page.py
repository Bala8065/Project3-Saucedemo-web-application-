from selenium.webdriver.common.by import By
from src.core.base_page import BasePage

class CompletePage(BasePage):
    HEADER = (By.CSS_SELECTOR, "h2.complete-header")

    def confirmation_message(self) -> str:
        return self.get_text(self.HEADER)
