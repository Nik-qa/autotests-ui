import pytest

@pytest.fixture(scope="function")
def clean_book_database() -> None:
    print("[FIXTURE] Удаляем все данные из базы данных")

@pytest.fixture(scope="function")
def fill_book_database() -> None:
    print("[FIXTURE] Создаем новые данные в базе данных")

@pytest.mark.usefixtures("fill_book_database")
def test_read_all_books_in_library():
    print("Riding all books")

@pytest.mark.usefixtures(
    "clean_book_database",
    "fill_book_database",
)
class TestLibrary:
    def test_read_book_from_library(self):
        ...

    def test_delete_book_from_library(self):
        ...