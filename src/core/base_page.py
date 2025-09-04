from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from .wait import Wait
from .logger import get_logger

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = Wait(driver)
        self.log = get_logger(self.__class__.__name__)

    def open(self, url: str):
        self.log.info(f"Opening URL: {url}")
        self.driver.get(url)

    def type(self, locator, text: str):
        el = self.wait.visible(locator)
        el.clear()
        el.send_keys(text)

    def click(self, locator):
        self.wait.clickable(locator).click()

    def get_text(self, locator) -> str:
        return self.wait.visible(locator).text.strip()

    def is_visible(self, locator) -> bool:
        try:
            self.wait.visible(locator)
            return True
        except TimeoutException:
            return False

    def get_elements(self, locator):
        return self.wait.all_present(locator)

    def take_screenshot(self, path: str):
        self.driver.save_screenshot(path)
        self.log.info(f"Saved screenshot to {path}")
