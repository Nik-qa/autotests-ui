from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto('https://news.mail.ru/')

    search_frame = page.frame_locator('//iframe[@class="fc1b9f573b"]')
    yandex_input = search_frame.locator("//body//input[@name='text']")
    yandex_input.focus()

    for char in 'Яблоко':
        yandex_input.type(char, delay=500)

    page.wait_for_timeout(1000)

    for _ in range(3):
        yandex_input.press('Backspace')
        page.wait_for_timeout(500)

    # delete_button = search_frame.locator("//div[@class='arrow__clear mini-suggest__input-clear']")
    # delete_button.click()

    page.wait_for_timeout(3000)