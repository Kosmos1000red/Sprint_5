import pytest
from locators import Locators as L
from data import Data


@pytest.fixture()
def auth_fixture(authenticated_driver):
    return authenticated_driver


@pytest.mark.profile
def test_go_to_profile_from_home(auth_fixture): 
    
    driver = auth_fixture

    driver.get(Data.APP_URL)

    account_btn = driver.find_element(*L.MAIN_PROFILE_BUTTON)
    account_btn.click()

    login_field = driver.find_elements(*L.LOGIN_EMAIL_INPUT)
    assert len(login_field) > 0, \
        "Кнопка 'Личный кабинет' не привела к форме входа."

    logout_btn = driver.find_elements(*L.PROFILE_LOGOUT_LINK)
    assert len(logout_btn) > 0, "Авторизация после нажатия кнопки ЛК не сработала."


@pytest.mark.profile
def test_go_to_constructor_from_profile(auth_fixture):
    
    driver = auth_fixture

    driver.get(Data.PROFILE_URL)

    constructor_link = driver.find_element(*L.PROFILE_CONSTRUCTOR_BUTTON)
    constructor_link.click()

    title = driver.find_elements(*L.MAIN_COMBINE_TEXT)
    assert len(title) > 0, "Заголовок конструктора не найден."


@pytest.mark.profile
def test_go_to_home_from_profile(auth_fixture):
    
    driver = auth_fixture

    driver.get(Data.PROFILE_URL)

    logo = driver.find_element(*L.PROFILE_LOGO)
    logo.click()

    combine_text = driver.find_elements(*L.MAIN_COMBINE_TEXT)
    assert len(combine_text) > 0, "Логотип не вернул на главную страницу."