import pytest 
from locators import Locators as L
from data import Data


@pytest.fixture()
def auth_fixture(authenticated_driver):
    return authenticated_driver


@pytest.mark.logout
def test_logout(auth_fixture):  
    driver = auth_fixture

    driver.get(Data.PROFILE_URL)

    driver.implicitly_wait(1)

    logout_btn = driver.find_element(*L.PROFILE_LOGOUT_LINK).click()

    login_field = driver.find_elements(*L.LOGIN_EMAIL_INPUT)
    assert len(login_field) > 0, "Форма входа не открылась после выхода."