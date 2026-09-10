import pytest
from data import Data
from locators import Locators as L
from generators import generate_password

@pytest.mark.registration
def test_successful_registration(driver):
    driver.get(Data.BURGERS_URL)
    
    enter_button = driver.find_element(*L.MAIN_ACCOUNT_BUTTON).click()
    driver.find_element(*L.REG_LOGIN_LINK).click()

    pwd = generate_password(length=8)  
    email = f"test_user_{pwd[:5]}@example.com"

    driver.find_element(*L.REG_NAME_INPUT).send_keys('Марина')
    driver.find_element(*L.REG_EMAIL_INPUT).send_keys(email)
    driver.find_element(*L.REG_PWD_INPUT).send_keys(pwd)
    driver.find_element(*L.REG_REG_BUTTON).click()

    assert driver.current_url.startswith(Data.PROFILE_URL), \
        'После успешной регистрации пользователь не попал в Профиль'


@pytest.mark.registration
def test_short_password(driver):
    driver.get(Data.REG_URL)

    name_input = driver.find_element(*L.REG_NAME_INPUT).send_keys('Иван')
    email_input = driver.find_element(*L.REG_EMAIL_INPUT).send_keys(f'ivan{generate_password(4)}@example.com')
    password_input = driver.find_element(*L.REG_PWD_INPUT).send_keys('1234')

    driver.find_element(*L.REG_REG_BUTTON).click()

    error_message = driver.find_elements(*L.REG_BAD_PWD_MESSAGE)
    assert len(error_message) > 0, 'Не появилось сообщение о коротком пароле.'