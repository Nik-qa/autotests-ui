import pytest
from playwright.sync_api import sync_playwright

@pytest.mark.testing
def test_test_1():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://www.google.com")

        # locator_1 = page.locator()