from playwright.sync_api import sync_playwright, expect, Page
import pytest

@pytest.mark.test1234
@pytest.mark.flaky(reruns=1, delay_reruns=1)
@pytest.mark.parametrize('email, username, password', [
    ('qatestiiiing@gmail.com', 'testing_testing', 'wewer24241')
])
def test_today_training(logit_test_custom: Page, email: str, username: str, password: str):
    logit_test_custom.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

    email_input = logit_test_custom.get_by_test_id('registration-form-email-input').locator('input')
    email_input.fill(email)

    username_input = logit_test_custom.locator('//div[@data-testid="registration-form-username-input"]//input')
    username_input.fill(username)

    password_input = logit_test_custom.get_by_test_id('registration-form-password-input').locator('input')
    password_input.fill(password)

    button_registration = logit_test_custom.locator('//button[@data-testid="registration-page-registration-button"]')
    button_registration.click()

    logit_test_custom.context.storage_state(path="browser-state-1.json")
