import pytest
from playwright.sync_api import Page, Playwright
import allure
from pages.authentication.registration_page import RegistrationPage
from _pytest.fixtures import SubRequest


@pytest.fixture
def chromium_page(request: SubRequest, playwright: Playwright) -> Page:
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    context.tracing.start(screenshots=True, snapshots=True, sources=True)

    yield context.new_page()

    context.tracing.stop(path=f"./tracing/{request.node.name}.zip") #request.node.name в нем хранится имя текущего теста
    browser.close()

    allure.attach.file(f"./tracing/{request.node.name}.zip", name="trace", extension='zip')

@pytest.fixture(scope="session")
def initialize_browser_state(playwright: Playwright): #почитал про анатации, говорят Page не нужно, т.к. функция тут ничего не возвращает
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()

    registration_page = RegistrationPage(page=page)
    registration_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')
    registration_page.registration_form.fill(email='user.name@gmail.com', username='username', password='password')
    registration_page.registration_button.click()

    page.wait_for_timeout(2000)

    context.storage_state(path="browser-state.json")
    browser.close()

@pytest.fixture(scope="function")
def chromium_page_with_state(request: SubRequest, initialize_browser_state, playwright: Playwright) -> Page:
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context(storage_state='browser-state.json')
    context.tracing.start(screenshots=True, snapshots=True, sources=True)

    yield context.new_page()

    context.tracing.stop(path=f"./tracing/{request.node.name}.zip") #request.node.name в нем хранится имя текущего теста
    browser.close()

    allure.attach.file(f"./tracing/{request.node.name}.zip", name="trace", extension='zip')


@pytest.fixture(scope="function")
def logit_test_custom(playwright: Playwright) -> Page:
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    yield page
    browser.close()