from selenium.webdriver.common.by import By
from src.core.base_page import BasePage

class Menu(BasePage):
    BURGER = (By.ID, "react-burger-menu-btn")
    LOGOUT = (By.ID, "logout_sidebar_link")
    RESET = (By.ID, "reset_sidebar_link")

    def open_menu(self):
        self.click(self.BURGER)

    def logout(self):
        self.open_menu()
        self.click(self.LOGOUT)

    def reset_app_state(self):
        self.open_menu()
        self.click(self.RESET)
