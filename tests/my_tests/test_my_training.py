from playwright.sync_api import sync_playwright, expect
import pytest

@pytest.mark.training
def test_my_training():
    with sync_playwright() as playwright:

        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

        email_registration = page.locator('//div[@data-testid="registration-form-email-input"]//input')
        email_registration.fill("QwertyFire@gmail.com")

        username_registration = page.get_by_test_id('registration-form-username-input').locator('input')
        username_registration.fill("Fire")

        password_registration = page.get_by_test_id('registration-form-password-input').locator('input')
        password_registration.fill("1223_5678")

        button_registration = page.locator('//button[@id="registration-page-registration-button"]')
        button_registration.click()

        context.storage_state(path="training.json")

        # page.wait_for_timeout(2000)

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)

        context = browser.new_context(storage_state="training.json")
        page = context.new_page()
        page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard')

        title_page_dashboard = page.locator('//h6[text() ="Dashboard"]')
        expect(title_page_dashboard).to_be_visible()
        expect(title_page_dashboard).to_have_text("Dashboard")

        context.close()






