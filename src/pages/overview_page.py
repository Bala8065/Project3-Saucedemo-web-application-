from selenium.webdriver.common.by import By
from src.core.base_page import BasePage

class OverviewPage(BasePage):
    SUMMARY = (By.CSS_SELECTOR, ".summary_info")
    FINISH = (By.ID, "finish")

    def summary_text(self) -> str:
        return self.get_text(self.SUMMARY)

    def finish(self):
        self.click(self.FINISH)
