from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)

    context = browser.new_context()
    page = context.new_page()

    page.goto('https://news.mail.ru/')

    iframe = page.frame_locator('//iframe[@class="fc1b9f573b"]')
    input_iframe = iframe.locator('//input[@name="text"]')
    input_iframe.focus()

    for char in "apple":
        input_iframe.type(char)

    button_find = page.locator('//button[text()="Найти"]')

    with context.expect_page() as page_info:
        button_find.click()

    new_page = page_info.value
    new_page.wait_for_load_state()

    new_iframe = new_page.frame_locator('//iframe[@class="f8930fa321"]')
    tab1 = new_iframe.locator('//nav/div/a//span[text()="Поиск"][1]')
    expect(tab1).to_be_visible()

    navigation_element_picture = new_iframe.locator('//nav/div/a//span[text()="Картинки"]')
    navigation_element_picture.hover()
    expect(navigation_element_picture).to_be_visible()

    page.wait_for_timeout(1000)