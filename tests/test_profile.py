import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import Data
from locators import Locators as L


@pytest.mark.profile
class TestProfile:

    def test_go_to_profile_from_home(self, authenticated_driver):
        driver = authenticated_driver
        driver.get(Data.APP_URL)
        driver.find_element(*L.MAIN_PROFILE_BUTTON).click()

        assert WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(L.PROFILE_LOGOUT_LINK)
        ), "Переход в личный кабинет не удался."

    def test_go_to_constructor_from_profile(self, authenticated_driver):
        driver = authenticated_driver
        driver.get(Data.PROFILE_URL)
        driver.find_element(*L.PROFILE_CONSTRUCTOR_BUTTON).click()

        assert WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(L.MAIN_COMBINE_TEXT)
        ), "Заголовок конструктора не найден после перехода из ЛК."

    def test_go_to_home_from_profile_by_logo(self, authenticated_driver):
        driver = authenticated_driver
        driver.get(Data.PROFILE_URL)
        driver.find_element(*L.PROFILE_LOGO).click()

        assert WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(L.MAIN_COMBINE_TEXT)
        ), "Логотип не вернул на главную страницу."