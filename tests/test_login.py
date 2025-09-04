import pytest
from src.keywords.web_keywords import WebKeywords
from src.pages.inventory_page import InventoryPage
from src.pages.login_page import LoginPage

@pytest.mark.parametrize("username,password", [
    ("standard_user", "secret_sauce"),
    ("performance_glitch_user", "secret_sauce"),
    ("problem_user", "secret_sauce"),
    ("error_user", "secret_sauce"),
    ("visual_user", "secret_sauce"),
])
def test_login_various_users(driver, base_url, username, password):
    kw = WebKeywords(driver, base_url)
    kw.login(username, password)
    assert InventoryPage(driver).is_visible(InventoryPage.TITLE)

@pytest.mark.parametrize("username,password", [
    ("", ""),
    ("random", "bad"),
    ("locked_out_user", "secret_sauce"),
])
def test_login_invalid(driver, base_url, username, password):
    lp = LoginPage(driver).load(base_url)
    lp.login(username, password)
    assert lp.is_visible(LoginPage.ERROR_MSG)

def test_logout(driver, base_url):
    kw = WebKeywords(driver, base_url)
    kw.login("standard_user", "secret_sauce")
    kw.logout()
    assert LoginPage(driver).is_visible(LoginPage.LOGIN_BTN)
