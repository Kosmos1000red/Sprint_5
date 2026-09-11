import pytest
from data import Data
from locators import Locators as L
from helpers import login, wait_logged_in


@pytest.mark.login
class TestLogin:

    def test_login_via_main_button(self, driver):
        driver.get(Data.APP_URL)
        driver.find_element(*L.MAIN_ACCOUNT_BUTTON).click()
        login(driver)

        assert wait_logged_in(driver), \
            "Вход через кнопку 'Войти в аккаунт' не удался."

    def test_login_via_account_button(self, driver):
        driver.get(Data.APP_URL)
        driver.find_element(*L.MAIN_PROFILE_BUTTON).click()
        login(driver)

        assert wait_logged_in(driver), \
            "Вход через кнопку 'Личный кабинет' не удался."

    def test_login_via_registration_link(self, driver):
        driver.get(Data.REG_URL)
        driver.find_element(*L.REG_LOGIN_LINK).click()
        login(driver)

        assert wait_logged_in(driver), \
            "Вход через форму регистрации не удался."

    def test_login_via_forgot_pass_form(self, driver):
        driver.get(Data.PWD_RECOVERY_URL)
        driver.find_element(*L.RECOVERY_PAGE_LOGIN_LINK).click()
        login(driver)

        assert wait_logged_in(driver), \
            "Вход через форму восстановления пароля не удался."