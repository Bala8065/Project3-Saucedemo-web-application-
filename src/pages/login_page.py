from selenium.webdriver.common.by import By
from src.core.base_page import BasePage

class LoginPage(BasePage):
    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BTN = (By.ID, "login-button")
    ERROR_MSG = (By.CSS_SELECTOR, "h3[data-test='error']")

    def load(self, base_url: str):
        self.open(base_url)
        return self

    def login(self, username: str, password: str):
        self.type(self.USERNAME, username)
        self.type(self.PASSWORD, password)
        self.click(self.LOGIN_BTN)

    def error_text(self) -> str:
        return self.get_text(self.ERROR_MSG)
