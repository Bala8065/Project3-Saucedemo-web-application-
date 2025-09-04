import os
from src.keywords.web_keywords import WebKeywords
from src.pages.inventory_page import InventoryPage
from src.pages.cart_page import CartPage
from src.pages.checkout_page import CheckoutPage
from src.pages.overview_page import OverviewPage
from src.pages.complete_page import CompletePage

def test_complete_checkout_and_validate(driver, base_url, testdata, tmp_path):
    WebKeywords(driver, base_url).login("standard_user", "secret_sauce")
    inv = InventoryPage(driver)

    for name in ["Sauce Labs Backpack", "Sauce Labs Bike Light"]:
        driver.find_element("xpath", f"//div[@class='inventory_item_name' and text()='{name}']/ancestor::div[@class='inventory_item']//button").click()

    inv.open_cart()
    assert inv.cart_count() == 2

    cart = CartPage(driver)
    items_before = cart.items()

    cart.checkout()
    co = CheckoutPage(driver)
    co.fill_and_continue(str(testdata['checkout']['first_name']), str(testdata['checkout']['last_name']), str(testdata['checkout']['postal_code']))

    overview = OverviewPage(driver)
    summary = overview.summary_text()

    os.makedirs("screenshots", exist_ok=True)
    shot = os.path.join("screenshots", "order_summary.png")
    driver.save_screenshot(shot)

    overview.finish()
    complete = CompletePage(driver)
    msg = complete.confirmation_message()

    for name, _ in items_before:
        assert name in summary
    assert "THANK YOU" in msg.upper()
