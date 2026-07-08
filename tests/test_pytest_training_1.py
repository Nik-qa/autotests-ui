from playwright.sync_api import sync_playwright, expect
import pytest

@pytest.fixture(scope='function')
def chromium():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        yield page
        context.close()
        browser.close()

def test_training_fixture(chromium):
    chromium.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

    email = chromium.get_by_test_id('registration-form-email-input').locator('input')
    email.fill('qw12eqwrqw@gmail.com')

    username = chromium.locator('//div[@data-testid="registration-form-username-input"]//input')
    username.fill('qNikk')

    password = chromium.get_by_test_id('registration-form-password-input').locator('input')
    password.fill('qweqweqwe123qwe')

    button = chromium.locator('//div//button[text()="Registration"]')
    button.click()

    chromium.context.storage_state(path='fixture_training.json')

    chromium.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard')
    title = chromium.get_by_test_id('dashboard-toolbar-title-text')
    expect(title).to_have_text('Dashboard')
