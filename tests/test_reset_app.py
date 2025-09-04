from src.keywords.web_keywords import WebKeywords
from src.pages.inventory_page import InventoryPage

def test_reset_app_state(driver, base_url):
    kw = WebKeywords(driver, base_url)
    kw.login("standard_user", "secret_sauce")
    inv = InventoryPage(driver)

    driver.find_element("xpath", "//button[contains(@id,'add-to-cart-')]").click()
    assert inv.cart_count() == 1

    kw.reset_app_state()
    assert inv.cart_count() == 0
