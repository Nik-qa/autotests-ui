from playwright.sync_api import sync_playwright, expect, Page
import pytest

def test_search_google_page(chromium_page: Page):
        chromium_page.goto("https://www.google.com")


