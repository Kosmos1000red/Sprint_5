import pytest
from locators import Locators as L
from data import Data
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


@pytest.fixture()
def auth_fixture(authenticated_driver):
    return authenticated_driver


@pytest.mark.login
def test_login_via_main_button(driver):
    
    driver.get(Data.APP_URL)

    enter_btn = driver.find_element(*L.MAIN_ACCOUNT_BUTTON) 
    enter_btn.click()

    login_field = driver.find_elements(*L.LOGIN_EMAIL_INPUT)
    assert len(login_field) > 0, "Форма входа не открылась."


@pytest.mark.login
def test_login_via_account_button(auth_fixture): 

    driver = auth_fixture

    driver.get(Data.APP_URL)

    account_btn = driver.find_element(*L.MAIN_PROFILE_BUTTON)
    account_btn.click()

    login_field = driver.find_elements(*L.LOGIN_EMAIL_INPUT)
    assert len(login_field) > 0, \
        "Кнопка 'Личный кабинет' не привела к форме входа."

    logout_btn = driver.find_elements(*L.PROFILE_LOGOUT_LINK)
    assert len(logout_btn) > 0, "Авторизация после нажатия кнопки ЛК не сработала."


@pytest.mark.login
def test_login_via_registration_link(driver):
    
    driver.get(Data.REG_URL)

    back_to_login_link = driver.find_element(
        By.XPATH,
        "//a[@href='/login']"
    )
    back_to_login_link.click()

    email_input = driver.find_elements(*L.LOGIN_EMAIL_INPUT)
    assert len(email_input) > 0, "Ссылка 'Войти' не привела к форме входа."


@pytest.mark.login
def test_login_via_forgot_pass_form(driver):

    driver.get(Data.BURGERS_URL)

    enter_btn = driver.find_element(*L.MAIN_ACCOUNT_BUTTON).click()

    forgot_link = driver.find_element(
        By.XPATH,
        "//a[contains(@href, '/forgot-password')]"
    ).click()

    back_to_login_link = driver.find_element(*L.RECOVERY_PAGE_LOGIN_LINK).click()

    email_input = driver.find_elements(*L.LOGIN_EMAIL_INPUT)
    assert len(email_input) > 0, "Не удалось вернуться на форму входа."

    WebDriverWait(driver, 5).until(  
        lambda d: d.current_url.startswith(Data.PROFILE_URL),
        message='После авторизации пользователь не попал в Профиль'
    )