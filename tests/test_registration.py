import pytest
from data import Data
from locators import Locators as L
from generators import generate_email, generate_password


@pytest.mark.registration
class TestRegistration:

    def test_successful_registration(self, driver):
        driver.get(Data.REG_URL)

        email = generate_email("Marina", "Bobkova", 42)
        pwd = generate_password(length=8)

        driver.find_element(*L.REG_NAME_INPUT).send_keys('Марина')
        driver.find_element(*L.REG_EMAIL_INPUT).send_keys(email)
        driver.find_element(*L.REG_PWD_INPUT).send_keys(pwd)
        driver.find_element(*L.REG_REG_BUTTON).click()

        assert driver.current_url.startswith(Data.PROFILE_URL), \
            'После успешной регистрации пользователь не попал в Профиль'

    def test_short_password_error(self, driver):
        driver.get(Data.REG_URL)

        email = generate_email("Ivan", "Ivanov", 1)

        driver.find_element(*L.REG_NAME_INPUT).send_keys('Иван')
        driver.find_element(*L.REG_EMAIL_INPUT).send_keys(email)
        driver.find_element(*L.REG_PWD_INPUT).send_keys('1234')
        driver.find_element(*L.REG_REG_BUTTON).click()

        assert driver.find_elements(*L.REG_BAD_PWD_MESSAGE), \
            'Не появилось сообщение о некорректном пароле.'