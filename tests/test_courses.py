from playwright.sync_api import expect, Page
import pytest

@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(chromium_page_with_state: Page):
    chromium_page_with_state.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

    dashboard_title = chromium_page_with_state.get_by_test_id('courses-list-toolbar-title-text')
    expect(dashboard_title).to_be_visible()
    expect(dashboard_title).to_have_text('Courses')

    icon_folder = chromium_page_with_state.get_by_test_id('courses-list-empty-view-icon')
    expect(icon_folder).to_be_visible()

    text_block = chromium_page_with_state.get_by_test_id('courses-list-empty-view-title-text')
    expect(text_block).to_be_visible()
    expect(text_block).to_have_text('There is no results')

    description_block = chromium_page_with_state.get_by_test_id('courses-list-empty-view-description-text')
    expect(description_block).to_be_visible()
    expect(description_block).to_have_text('Results from the load test pipeline will be displayed here')

