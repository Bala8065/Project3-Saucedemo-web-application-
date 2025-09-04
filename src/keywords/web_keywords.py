from src.pages.login_page import LoginPage
from src.pages.inventory_page import InventoryPage
from src.pages.cart_page import CartPage
from src.pages.checkout_page import CheckoutPage
from src.pages.overview_page import OverviewPage
from src.pages.complete_page import CompletePage
from src.pages.components.menu import Menu

class WebKeywords:
    def __init__(self, driver, base_url):
        self.login_page = LoginPage(driver)
        self.inventory = InventoryPage(driver)
        self.cart = CartPage(driver)
        self.checkout_page = CheckoutPage(driver)
        self.overview = OverviewPage(driver)
        self.complete = CompletePage(driver)
        self.menu = Menu(driver)
        self.base_url = base_url

    def login(self, username, password):
        self.login_page.load(self.base_url).login(username, password)

    def logout(self):
        self.menu.logout()

    def reset_app_state(self):
        self.menu.reset_app_state()
