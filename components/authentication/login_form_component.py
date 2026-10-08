from components.base_component import BaseComponent
from playwright.sync_api import Page, expect

from elements.input import Input
import allure


class LoginFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.email = Input(page, "login-form-email-input", "Email Input")
        self.password = Input(page, 'login-form-password-input', 'Password Input')

    @allure.step("Fill login form")
    def fill(self, email: str, password: str):
        self.email.fill(email)
        self.password.fill(password)

    @allure.step("Check visible login form")
    def check_visible(self, email: str, password: str):
        self.email.check_visible()
        self.email.check_have_value(email)

        self.password.check_visible()
        self.password.check_have_value(password)
