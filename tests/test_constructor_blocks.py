import pytest
from locators import Locators as L
from data import Data
from selenium.webdriver.common.by import By


@pytest.fixture()
def open_constructor(driver):
    driver.get(Data.APP_URL)


@pytest.mark.constructor
def test_tab_buns(open_constructor, driver):

    tab = driver.find_element(*L.CONSTRUCTOR_BUNS_BUTTON)

    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", tab) 

    tab.click()  

    active_class = tab.get_attribute("class")
    assert "tab_type_current" in active_class, \
        "Вкладка Булки не стала активной."


@pytest.mark.constructor
def test_tab_sauces(open_constructor, driver):
    tab = driver.find_element(*L.CONSTRUCTOR_SAUCES_BUTTON)
    
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", tab)

    tab.click()

    active_class = tab.get_attribute("class")
    assert "tab_type_current" in active_class, \
        "Вкладка Соусы не стала активной."


@pytest.mark.constructor
def test_tab_fillings(open_constructor, driver):

    parent_block = driver.find_element(
        By.XPATH,
        "//div[@class='tab_tab__1PsGy tab_tab_type_current']"
    )

    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", parent_block)

    inner_text = parent_block.find_element(By.XPATH, ".//span").text.strip()
    assert inner_text == "Начинки", "Активна неверная вкладка."