import os
import yaml
import pytest
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

from tools.env import BASE_URL, BROWSER, HEADLESS, WINDOW_SIZE
from src.core.logger import get_logger

log = get_logger("conftest")

def _make_driver():
    width, height = [int(x) for x in WINDOW_SIZE.split(",")]
    if BROWSER == "firefox":
        opts = FirefoxOptions()
        if HEADLESS:
            opts.add_argument("-headless")
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=opts)
    else:
        opts = ChromeOptions()
        if HEADLESS:
            opts.add_argument("--headless=new")
        opts.add_argument(f"--window-size={width},{height}")
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=opts)
    driver.set_page_load_timeout(30)
    driver.implicitly_wait(0)
    return driver

@pytest.fixture(scope="session")
def base_url():
    return BASE_URL

@pytest.fixture(scope="session")
def user_data():
    with open(os.path.join("data", "users.yaml"), "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

@pytest.fixture(scope="session")
def testdata():
    import yaml
    with open(os.path.join("data", "testdata.yaml"), "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

@pytest.fixture()
def driver():
    driver = _make_driver()
    yield driver
    driver.quit()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)

def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get("driver")
        if driver:
            os.makedirs("screenshots", exist_ok=True)
            path = os.path.join("screenshots", f"FAILED_{item.name}.png")
            driver.save_screenshot(path)
            log.info(f"Saved failure screenshot: {path}")
