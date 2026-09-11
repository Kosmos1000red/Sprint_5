import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import Data
from locators import Locators as L


@pytest.mark.logout
class TestLogout:

    def test_logout(self, authenticated_driver):
        driver = authenticated_driver
        driver.get(Data.PROFILE_URL)
        driver.find_element(*L.PROFILE_LOGOUT_LINK).click()

        assert WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(L.LOGIN_EMAIL_INPUT)
        ), "Форма входа не открылась после выхода."