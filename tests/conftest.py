from webbrowser import Chrome

import pytest
from playwright.sync_api import Page, Playwright

@pytest.fixture
def chromium_page(playwright: Playwright) -> Page:
        browser = playwright.chromium.launch(headless=False)
        yield browser.new_page()
        browser.close()

@pytest.fixture(scope="session")
def initialize_browser_state():
    ...