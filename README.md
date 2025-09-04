# SauceDemo Selenium + Pytest POM Framework

This framework automates core flows of the demo e-commerce site https://www.saucedemo.com/ using Selenium 4, Pytest, and the Page Object Model (POM).

## Features
- ✅ POM with modular pages and a shared BasePage
- ✅ Data-driven tests via YAML (users, checkout data)
- ✅ Keyword layer (WebKeywords) for reusable business steps
- ✅ Smart explicit waits (no flaky implicit waits)
- ✅ Deterministic + random product selection scenarios
- ✅ Screenshots on failure and order summary capture
- ✅ HTML/Allure reporting
- ✅ Cross-browser: Chrome/Firefox; headless via `.env`

## Quickstart
1. Create virtualenv and activate:
   ```bash
   python -m venv .venv
   source .venv/bin/activate   # Windows: .venv\Scripts\activate
   pip install -r requirements.txt
   ```
2. Optionally copy `.env.example` to `.env` and adjust.
3. Run tests:
   ```bash
   pytest -q --html=reports/report.html --self-contained-html
   ```

