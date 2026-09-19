import pytest

@pytest.fixture(autouse=True)
def send_analytics_date():
    print("[AUTOUSE] Отправляем данные в сервис аналаитики")

@pytest.fixture(scope="session")
def settings():
    print("[SESSION] Инициализируем настройки автотетстов")

@pytest.fixture(scope="class")
def user():
    print("[CLASS] Создаем данные пользователя один раз на тестовый класс")

@pytest.fixture(scope="function")
def browser():
    print("[FUNCTION] Открываем браузер на кажлый автотест")


class TestUserFlow:
    def test_user_login(self, settings, user, browser):
        ...
    def test_user_can_create_courses(self, settings, user, browser):
        ...

class TestAccountFlow:
    def test_user_account(self, settings, user, browser):
        ...