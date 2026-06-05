from playwright.sync_api import sync_playwright, expect, Request, Response

# Логирование запросов
def log_request(request: Request):
    print(f"Request: {request.url}")
# Логирование ответов
def log_response(response: Response):
    print(f"Response: {response.url}, {response.status}")

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login')

    # Добавляем обработчики событий
    page.on("request", log_request)  # Запрос отправлен
    # page.remove_listener("request", log_request)
    page.on("response", log_response)  # Ответ получен

    page.wait_for_timeout(1000)