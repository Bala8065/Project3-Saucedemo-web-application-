import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("BASE_URL", "https://www.saucedemo.com/")
BROWSER = os.getenv("BROWSER", "chrome").lower()
HEADLESS = os.getenv("HEADLESS", "true").lower() == "true"
WINDOW_SIZE = os.getenv("WINDOW_SIZE", "1440,900")
