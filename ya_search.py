from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto('https://ya.ru')

    ya_page_input = page.locator("//textarea[@id='text']")
    ya_page_input.fill('Вконтакте')

    ya_page_button = page.locator("//button[@type='submit']")
    ya_page_button.click()

    ya_search_element = page.locator("//ul[@aria-label='Результаты поиска']/li[2]/div/div[1]//a/div")
    expect(ya_search_element).to_be_visible()

    # page.wait_for_timeout(1000)