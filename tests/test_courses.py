from playwright.sync_api import sync_playwright, expect

def test_empty_courses_list():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

        email_input = page.get_by_test_id('registration-form-email-input').locator('input')
        email_input.fill('user.name@gmail.com')

        username_input = page.get_by_test_id('registration-form-username-input').locator('input')
        username_input.fill('username')

        password_input = page.get_by_test_id('registration-form-password-input').locator('input')
        password_input.fill('password')

        button = page.get_by_test_id('registration-page-registration-button')
        button.click()

        page.wait_for_timeout(2000)

        context.storage_state(path="registration-form.json")

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context(storage_state='registration-form.json')
        page = context.new_page()
        page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')

        dashboard_title = page.get_by_test_id('courses-list-toolbar-title-text')
        expect(dashboard_title).to_be_visible()
        expect(dashboard_title).to_have_text('Courses')

        icon_folder = page.get_by_test_id('courses-list-empty-view-icon')
        expect(icon_folder).to_be_visible()

        text_block = page.get_by_test_id('courses-list-empty-view-title-text')
        expect(text_block).to_be_visible()
        expect(text_block).to_have_text('There is no results')

        description_block = page.get_by_test_id('courses-list-empty-view-description-text')
        expect(description_block).to_be_visible()
        expect(description_block).to_have_text('Results from the load test pipeline will be displayed here')

        # page.wait_for_timeout(2000)




