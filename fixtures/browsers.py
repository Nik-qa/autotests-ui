import pytest
from playwright.sync_api import Page, Playwright
from pages.authentication.registration_page import RegistrationPage
from _pytest.fixtures import SubRequest
from tools.playwright.pages import initialize_playwright_page
from config import settings
from tools.routes import AppRoute


@pytest.fixture
def chromium_page(request: SubRequest, playwright: Playwright) -> Page:
    yield from initialize_playwright_page(playwright, test_name=request.node.name)

@pytest.fixture(scope="session")
def initialize_browser_state(playwright: Playwright): #почитал про анатации, говорят Page не нужно, т.к. функция тут ничего не возвращает
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context(base_url=settings.get_base_url())
    page = context.new_page()

    registration_page = RegistrationPage(page=page)
    registration_page.visit(AppRoute.REGISTRATION)
    registration_page.registration_form.fill(
        email=settings.test_user.email,
        username=settings.test_user.username,
        password=settings.test_user.password,)
    registration_page.registration_button.click()

    page.wait_for_timeout(2000)

    context.storage_state(path=settings.browser_state_file)
    browser.close()

@pytest.fixture
def chromium_page_with_state(initialize_browser_state, request: SubRequest, playwright: Playwright) -> Page:
    yield from initialize_playwright_page(
        playwright,
        test_name=request.node.name,
        storage_state=settings.browser_state_file
    )

@pytest.fixture(scope="function")
def logit_test_custom(playwright: Playwright) -> Page:
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    yield page
    browser.close()