import pytest
from locators import Locators as L


@pytest.mark.constructor
class TestConstructor:

    def test_tab_buns(self, open_constructor):
        driver = open_constructor
        tab = driver.find_element(*L.CONSTRUCTOR_BUNS_BUTTON)
        driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});", tab
        )
        tab.click()

        assert "tab_type_current" in tab.get_attribute("class"), \
            "Вкладка 'Булки' не стала активной."

    def test_tab_sauces(self, open_constructor):
        driver = open_constructor
        tab = driver.find_element(*L.CONSTRUCTOR_SAUCES_BUTTON)
        driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});", tab
        )
        tab.click()

        assert "tab_type_current" in tab.get_attribute("class"), \
            "Вкладка 'Соусы' не стала активной."

    def test_tab_fillings(self, open_constructor):
        driver = open_constructor
        tab = driver.find_element(*L.CONSTRUCTOR_INGR_BUTTON)
        driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});", tab
        )
        tab.click()

        assert "tab_type_current" in tab.get_attribute("class"), \
            "Вкладка 'Начинки' не стала активной."