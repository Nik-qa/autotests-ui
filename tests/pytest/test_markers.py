from unittest import TestSuite

import allure
import pytest
from tools.allure.testing_tag import Enum, AllureTraining


@pytest.mark.smoke
@allure.epic(AllureTraining.TRAINING)
class TestTraining:
    def test_smoke_case(self):
        ...
    @pytest.mark.regression
    def test_regression_case(self):
        ...

@pytest.mark.smoke
class TestSuite:
    def test_case1(self):
        ...
    def test_case2(self):
        ...

@pytest.mark.regression
@allure.epic(AllureTraining.TRAINING)
class TestUserAuthentication:
    @pytest.mark.smoke
    def test_login(self):
        ...
    @pytest.mark.slow
    def test_password_reset(self):
        ...
    def test_logout(self):
        ...

@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.critical
@allure.epic(AllureTraining.TRAINING)
def test_critical_login():
    ...

@pytest.mark.ui
@allure.epic(AllureTraining.TRAINING)
class TestUserInterface:
    @pytest.mark.smoke
    @pytest.mark.critical
    def test_login_button(self):
        pass

    @pytest.mark.regression
    def test_forgot_password_link(self):
        pass

    @pytest.mark.smoke
    def test_signup_form(self):
        pass