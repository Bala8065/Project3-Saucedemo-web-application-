import random
from src.keywords.web_keywords import WebKeywords
from src.pages.inventory_page import InventoryPage
from src.pages.cart_page import CartPage

def login(driver, base_url):
    WebKeywords(driver, base_url).login("standard_user", "secret_sauce")

def test_cart_icon_visible(driver, base_url):
    login(driver, base_url)
    inv = InventoryPage(driver)
    assert inv.is_visible(InventoryPage.CART_LINK)

def test_random_select_add_and_validate_cart(driver, base_url):
    login(driver, base_url)
    inv = InventoryPage(driver)

    products = inv.product_list()
    chosen = random.sample(products, 4)

    for name, _ in chosen:
        driver.find_element("xpath", f"//div[@class='inventory_item_name' and text()='{name}']/ancestor::div[@class='inventory_item']//button").click()

    assert inv.cart_count() == 4

    inv.open_cart()
    cart = CartPage(driver)
    cart_items = cart.items()
    assert sorted(cart_items) == sorted(chosen)

def test_sorting_functionality(driver, base_url):
    login(driver, base_url)
    inv = InventoryPage(driver)

    inv.sort_by("Price (low to high)")
    prices = [p for _, p in inv.product_list()]
    assert prices == sorted(prices)

    inv.sort_by("Name (Z to A)")
    names = [n for n, _ in inv.product_list()]
    assert names == sorted(names, reverse=True)
