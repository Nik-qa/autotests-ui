import pytest

@pytest.mark.xfail(reason="Известная ошибка, исправление в следующем релизе")
def test_with_bug():
    assert 1 == 2

@pytest.mark.xfail(reason="Баг уже исправлен, но на тест все еще висит маркировка xfail")
def test_without_bug():
    pass