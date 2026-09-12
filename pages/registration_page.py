from playwright.sync_api import Page

from elements.button import Button
from elements.link import Link
from pages.base_page import BasePage
from components.authentication.registration_form_component import RegistrationFormComponent


class RegistrationPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.registration_form = RegistrationFormComponent(page)

        self.login_link = Link(page,'registration-page-login-link', "Login link")
        self.registration_button = Button(page,'registration-page-registration-button', "Login button")

    def click_login_link(self):
        self.login_link.click()

    def click_registration_button(self):
        self.registration_button.click()
