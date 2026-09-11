from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from data import Data
from locators import Locators as L


def login(driver, email=Data.EMAIL, password=Data.PASSWORD, timeout=10):
    """Заполняет форму логина и нажимает 'Войти'."""
    WebDriverWait(driver, timeout).until(
        EC.visibility_of_element_located(L.LOGIN_EMAIL_INPUT)
    )
    driver.find_element(*L.LOGIN_EMAIL_INPUT).send_keys(email)
    driver.find_element(*L.LOGIN_PASSWORD_INPUT).send_keys(password)
    driver.find_element(*L.LOGIN_LOGIN_BUTTON).click()


def wait_logged_in(driver, timeout=10):
    """Ждёт маркер авторизованного пользователя и возвращает WebElement."""
    return WebDriverWait(driver, timeout).until(
        EC.visibility_of_element_located(L.MAIN_ORDER_BUTTON)
    )


def click_tab_and_wait_active(driver, locator, timeout=10):
    """Кликает по вкладке конструктора и ждёт её активации (JS-клик + проверка класса)."""
    tab = WebDriverWait(driver, timeout).until(
        lambda d: d.find_element(*locator)
    )
    driver.execute_script("arguments[0].click();", tab)

    WebDriverWait(driver, timeout).until(
        lambda d: "tab_type_current"
        in d.find_element(*locator).get_attribute("class")
    )