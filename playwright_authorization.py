from sys import exec_prefix

from playwright.sync_api import sync_playwright, expect


with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")

    email_input = page.get_by_test_id("login-form-email-input").locator("input")
    email_input.fill('user.name@gmail.com')

    pass_input = page.get_by_test_id('login-form-password-input').locator("input")
    pass_input.fill('password')

    login_button = page.get_by_test_id("login-page-login-button")
    login_button.click()

    button_registration = page.locator("//div//a[@data-testid='login-page-registration-link']")
    expect(button_registration).to_be_visible()
    expect(button_registration).to_have_text("Registration")

    wrong_alert = page.get_by_test_id("login-page-wrong-email-or-password-alert")
    expect(wrong_alert).to_be_visible()
    expect(wrong_alert).to_have_text('Wrong email or password')

    page.wait_for_timeout(1000)