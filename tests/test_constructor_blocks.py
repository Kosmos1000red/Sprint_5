import pytest
from locators import Locators as L
from helpers import click_tab_and_wait_active


@pytest.mark.constructor
class TestConstructor:

    def test_tab_buns(self, open_constructor):
        driver = open_constructor
        # Сначала уходим на «Соусы», чтобы смена вкладки была заметной
        click_tab_and_wait_active(driver, L.CONSTRUCTOR_SAUCES_BUTTON)
        click_tab_and_wait_active(driver, L.CONSTRUCTOR_BUNS_BUTTON)

        assert "tab_type_current" in driver.find_element(
            *L.CONSTRUCTOR_BUNS_BUTTON
        ).get_attribute("class"), "Вкладка 'Булки' не стала активной."

    def test_tab_sauces(self, open_constructor):
        driver = open_constructor
        click_tab_and_wait_active(driver, L.CONSTRUCTOR_SAUCES_BUTTON)

        assert "tab_type_current" in driver.find_element(
            *L.CONSTRUCTOR_SAUCES_BUTTON
        ).get_attribute("class"), "Вкладка 'Соусы' не стала активной."

    def test_tab_fillings(self, open_constructor):
        driver = open_constructor
        click_tab_and_wait_active(driver, L.CONSTRUCTOR_INGR_BUTTON)

        assert "tab_type_current" in driver.find_element(
            *L.CONSTRUCTOR_INGR_BUTTON
        ).get_attribute("class"), "Вкладка 'Начинки' не стала активной."