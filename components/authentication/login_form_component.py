from components.base_component import BaseComponent
from playwright.sync_api import Page, expect


class LoginFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.email = page.get_by_test_id("login-form-email-input").locator("input")
        self.password = page.get_by_test_id('login-form-password-input').locator("input")

    def fill(self, email: str, password: str):
        self.email.fill(email)
        self.password.fill(password)

    def check_visible(self, email: str, password: str):
        expect(self.email).to_be_visible()
        expect(self.email).to_have_value(email)

        expect(self.password).to_be_visible()
        expect(self.password).to_have_value(password)
