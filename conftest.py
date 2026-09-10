import pytest
from selenium import webdriver
from data import Data 
from locators import Locators as L 


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture()
def authenticated_driver(driver):
    driver.get(Data.APP_URL)  
    driver.find_element(*L.MAIN_ACCOUNT_BUTTON).click() 
    driver.find_element(*L.LOGIN_EMAIL_INPUT).send_keys(Data.EMAIL)
    driver.find_element(*L.LOGIN_PASSWORD_INPUT).send_keys(Data.PASSWORD)
    driver.find_element(*L.LOGIN_LOGIN_BUTTON).click()

    return driver