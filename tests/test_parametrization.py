import pytest
from _pytest.fixtures import SubRequest

@pytest.mark.parametrize('number', [1, 2, 3, -1])
def test_number(number: int):
    print(f"Number: {number}")
    assert number > 0

@pytest.mark.parametrize('number, expected', [(1, 1),(2, 4), (3, 9)])
def test_several_number(number: int, expected: int):
    print(f"Number: {number ** 2}")
    assert number ** 2 == expected

@pytest.mark.parametrize('browser', ['chrome', 'firefox', 'safari'])
@pytest.mark.parametrize('os', ['macOs','windows','linux', 'debian'])
def test_multiplication_of_numbers(browser: str, os: str):
    assert len(os + browser) > 0

@pytest.fixture(params = ['chrome', 'firefox', 'safari'])
def browser(request: SubRequest):
    return request.param

def test_open_browser(browser: str):
    print(f"Running test on browser: {browser}")

@pytest.mark.parametrize("user", ["Alice", "Zara"])
class TestOperations:
    @pytest.mark.parametrize("account", ["Credit card", "Debit card"])
    def test_user_with_operations(self, user: str, account: str):
        print(f"User with operations: {user}")

    def test_user_without_operations(self, user: str):
        print(f"User without operations: {user}")

users = {
    "+70000000011": "User with money on bank account",
    "+70000000022": "User without money on bank account",
    "+70000000033": "User with operations on bank account"
}

@pytest.mark.parametrize(
    "phone_number",
    users.keys(),
    ids=lambda phone_number: f"{phone_number}: {users[phone_number]}"
)
def test_identifiers(phone_number: str):
    ...