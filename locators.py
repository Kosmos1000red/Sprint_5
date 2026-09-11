from selenium.webdriver.common.by import By

class Locators:
    REG_NAME_INPUT = (By.XPATH, "//label[text()='Имя']/following-sibling::input")
    REG_EMAIL_INPUT = (By.XPATH,"//label[text()='Email']/following-sibling::input")
    REG_PWD_INPUT = (By.XPATH,"//input[@type='password']")
    REG_REG_BUTTON = (By.XPATH,"//button[text()='Зарегистрироваться']")
    REG_BAD_PWD_MESSAGE = (By.XPATH, "//p[text()='Некорректный пароль']")
    REG_LOGIN_LINK = (By.XPATH, "//a[@href='/login']")
    
    MAIN_ACCOUNT_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")
    MAIN_PROFILE_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']")
    MAIN_ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")
    MAIN_COMBINE_TEXT = (By.XPATH, "//h1[text()='Соберите бургер']")

    LOGIN_EMAIL_INPUT = (By.XPATH, "//input[@name='name']")
    LOGIN_PASSWORD_INPUT = (By.XPATH, "//input[@name='Пароль']")
    LOGIN_LOGIN_BUTTON = (By.XPATH,"//button[text()='Войти']")

    RECOVERY_PAGE_LOGIN_LINK = (By.XPATH, "//a[@href='/login']")

    PROFILE_CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")
    PROFILE_LOGO = (By.CLASS_NAME, "AppHeader_header__logo__2D0X2")
    PROFILE_LOGOUT_LINK = (By.XPATH, "//button[text()='Выход']")

    CONSTRUCTOR_SAUCES_BUTTON = (By.XPATH, "//span[text()='Соусы']/parent::div")
    CONSTRUCTOR_BUNS_BUTTON = (By.XPATH, "//span[text()='Булки']/parent::div")
    CONSTRUCTOR_INGR_BUTTON = (By.XPATH, "//span[text()='Начинки']/parent::div")