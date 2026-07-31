import pytest
from playwright.sync_api import Page, Playwright

from pages.login_page import LoginPage
from pages.registration_page import RegistrationPge


@pytest.fixture
def login_page(chromium_page: Page) -> LoginPage:
    return LoginPage(page=chromium_page)

@pytest.fixture
def registration_page(chromium_page: Page) -> RegistrationPge:
    return RegistrationPge(page=chromium_page)