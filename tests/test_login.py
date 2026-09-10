import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import Data
from locators import Locators as L


@pytest.mark.login
class TestLogin:

    def _login(self, driver):
        driver.find_element(*L.LOGIN_EMAIL_INPUT).send_keys(Data.EMAIL)
        driver.find_element(*L.LOGIN_PASSWORD_INPUT).send_keys(Data.PASSWORD)
        driver.find_element(*L.LOGIN_LOGIN_BUTTON).click()

    def test_login_via_main_button(self, driver):
        driver.get(Data.APP_URL)
        driver.find_element(*L.MAIN_ACCOUNT_BUTTON).click()
        self._login(driver)

        assert WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(L.MAIN_ORDER_BUTTON)
        ), "Вход через кнопку 'Войти в аккаунт' не удался."

    def test_login_via_account_button(self, driver):
        driver.get(Data.APP_URL)
        driver.find_element(*L.MAIN_PROFILE_BUTTON).click()
        self._login(driver)

        assert WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(L.MAIN_ORDER_BUTTON)
        ), "Вход через кнопку 'Личный кабинет' не удался."

    def test_login_via_registration_link(self, driver):
        driver.get(Data.REG_URL)
        driver.find_element(*L.REG_LOGIN_LINK).click()
        self._login(driver)

        assert WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(L.MAIN_ORDER_BUTTON)
        ), "Вход через ссылку на форме регистрации не удался."

    def test_login_via_forgot_pass_form(self, driver):
        driver.get(Data.PWD_RECOVERY_URL)
        driver.find_element(*L.RECOVERY_PAGE_LOGIN_LINK).click()
        self._login(driver)

        assert WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(L.MAIN_ORDER_BUTTON)
        ), "Вход через форму восстановления пароля не удался."