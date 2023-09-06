import time
from selenium.webdriver.common.by import By
import pytest
from pages.locators import AuthLocators
from pages.locators import AuthType
from pages.locators import NameInput
from settings import actual_tel, actual_mail, actual_login, actual_account, actual_pass, notactual_account, notactual_tel, notactual_login, notactual_pass, notactual_mail

# Тест-Кейс Auth-111 Проверяем авторизацию по email действующего пользователя, проверяем в личном кабинете количество символов "имя + фамилия" больше 4 символов
def test_auth_mail_actual(driver):
    email_btn = driver.find_element(*AuthType.TYPE_EMAIL).click()
    driver.find_element(*AuthType.TYPE_SAVE_ME).click() #отключаем режим "Запомнить меня"
    input_mail = driver.find_element(*AuthLocators.AUTH_LOGIN).send_keys(actual_mail)
    input_pass = driver.find_element(*AuthLocators.AUTH_PASS).send_keys(actual_pass)
    driver.find_element(*AuthLocators.AUTH_ENTER).click()   # Кнопка ВОЙТИ
    driver.implicitly_wait(2)
    try:
        driver.find_element(By.CLASS_NAME, 'main-header__left')             # ищем лого в хэдере, если вход не выполнен и лого не обнаружено - делаем скрин
    except:
        driver.save_screenshot('error auth.png')
    time.sleep(1)
    lk = driver.find_element(By.XPATH, '//*[@id="app"]/main/div/div[2]/div[1]/div[1]/div[1]/h2').text
    out_btn = driver.find_element(By.ID, 'logout-btn').click()  # Кнопка ВЫЙТИ
    assert len(lk) > 4

# Тест-Кейс Auth-113 Проверяем авторизацию недействующего пользователя, получаем ошибку неверный логин или пароль
def test_auth_mail_notactual(driver):
    email_btn = driver.find_element(*AuthType.TYPE_EMAIL).click()
    driver.find_element(*AuthType.TYPE_SAVE_ME).click() #отключаем режим "Запомнить меня"
    input_mail = driver.find_element(*AuthLocators.AUTH_LOGIN).send_keys(notactual_mail)
    input_pass = driver.find_element(*AuthLocators.AUTH_PASS).send_keys(notactual_pass)
    driver.find_element(*AuthLocators.AUTH_ENTER).click()   # Кнопка ВОЙТИ
    driver.implicitly_wait(3)
    auth_error = driver.find_element(By.ID, 'form-error-message').text
    driver.back()
    assert auth_error =='Неверный логин или пароль'

# Тест-Кейс Auth-114 Проверяем поле ввода mail невалидными значениями
@pytest.mark.parametrize("mail_notvalid", ['test@test', 'test.ru', 'test test.ru', 'test@.ru', '123456', '!@#$%^&*()'])
def test_auth_mail_input_notvalid(driver, mail_notvalid):
    email_btn = driver.find_element(*AuthType.TYPE_EMAIL).click()
    driver.find_element(*AuthType.TYPE_SAVE_ME).click() #отключаем режим "Запомнить меня"
    input_mail = driver.find_element(*AuthLocators.AUTH_LOGIN).send_keys(mail_notvalid)
    input_pass = driver.find_element(*AuthLocators.AUTH_PASS).click()
    input_login = driver.find_element(*NameInput.LOGIN_INPUT).text
    assert input_login == 'Логин'

# Тест-Кейс Auth-115 Проверяем поле ввода mail пустым значением
def test_auth_mail_input_empty(driver):
    email_btn = driver.find_element(*AuthType.TYPE_EMAIL).click()
    input_pass = driver.find_element(*AuthLocators.AUTH_PASS).send_keys(notactual_pass)
    driver.find_element(*AuthLocators.AUTH_ENTER).click()  # Кнопка ВОЙТИ
    auth_error_remind = driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/span').text
    assert auth_error_remind == 'Введите адрес, указанный при регистрации'

# Тест-Кейс Auth-116 Проверяем авторизацию через Логин, действующий пользователь
def test_auth_login_actual(driver):
    login_btn = driver.find_element(*AuthType.TYPE_LOGIN).click()
    driver.find_element(*AuthType.TYPE_SAVE_ME).click() #отключаем режим "Запомнить меня"
    input_login = driver.find_element(*AuthLocators.AUTH_LOGIN).send_keys(actual_login)
    input_pass = driver.find_element(*AuthLocators.AUTH_PASS).send_keys(actual_pass)
    driver.find_element(*AuthLocators.AUTH_ENTER).click()   # Кнопка ВОЙТИ
    driver.implicitly_wait(3)
    try:
        driver.find_element(By.CLASS_NAME, 'main-header__left')             # ищем лого в хэдере, если вход не выполнен и лого не обнаружено - делаем скрин
    except:
        driver.save_screenshot('error auth.png')
    driver.implicitly_wait(3)
    lk = driver.find_element(By.XPATH, '//*[@id="app"]/main/div/div[2]/div[1]/div[1]/div[1]/h2').text
    out_btn = driver.find_element(By.ID, 'logout-btn').click()  # Кнопка ВЫЙТИ
    assert len(lk) > 4

# Тест-Кейс Auth-117 Проверяем авторизацию через Логин, недействующий пользователь, сообщение о неверном логине или пароле
def test_auth_login_notactual(driver):
    login_btn = driver.find_element(*AuthType.TYPE_LOGIN).click()
    driver.find_element(*AuthType.TYPE_SAVE_ME).click() #отключаем режим "Запомнить меня"
    input_login = driver.find_element(*AuthLocators.AUTH_LOGIN).send_keys(notactual_login)
    input_pass = driver.find_element(*AuthLocators.AUTH_PASS).send_keys(notactual_pass)
    driver.find_element(*AuthLocators.AUTH_ENTER).click()  # Кнопка ВОЙТИ
    login_error = driver.find_element(By.ID, 'form-error-message').text
    assert login_error == 'Неверный логин или пароль'

# Тест-Кейс Auth-118 и Auth-119 Проверяем авторизацию через Логин, 1) поле ввода оставляем пустым и нажимаем войти - получаем сообщение о необходимости
       # ввести логин или пороль. 2) в поле ввода Логин вводим спец символы, , проверяем, что сообщение об ошибке - пропало и новое не появилось.
def test_auth_login_input_notvalid(driver):
    login_btn = driver.find_element(*AuthType.TYPE_LOGIN).click()
    driver.find_element(*AuthType.TYPE_SAVE_ME).click() #отключаем режим "Запомнить меня"
    input_pass = driver.find_element(*AuthLocators.AUTH_PASS).send_keys(notactual_pass)
    driver.find_element(*AuthLocators.AUTH_ENTER).click()  # Кнопка ВОЙТИ
    login_error = driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/span').text
    input_login = driver.find_element(*AuthLocators.AUTH_LOGIN).send_keys('!"№;%:?*()/\{}][')   #вводим в поле ввода Логин - спецсимволы
    driver.find_element(By.CLASS_NAME, 'card-container__title').click() # Нажимаем мышкой в пустое место страницы
    try:
        driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/span')
        print('Поле вводе не приняло спец.символы, появляется ошибка о неверном вводе')
        error = True
    except:
        print('спец.символы приняты в поле ввода Логин, ошибки нет')
        error = False
    assert error == False
    assert login_error == 'Введите логин, указанный при регистрации'

# Тест-Кейс Auth-120 Проверяем авторизацию через Лицевой счёт, действующего пользователя, проверяем в личном кабинете количество символов "имя + фамилия" больше 4 символов
def test_auth_num_account_actual(driver):
    account_btn = driver.find_element(*AuthType.TYPE_ACCOUNT).click()
    driver.find_element(*AuthType.TYPE_SAVE_ME).click()  # отключаем режим "Запомнить меня"
    input_account = driver.find_element(*AuthLocators.AUTH_LOGIN).send_keys(actual_account)
    input_pass = driver.find_element(*AuthLocators.AUTH_PASS).send_keys(actual_pass)
    driver.find_element(*AuthLocators.AUTH_ENTER).click()   # Кнопка ВОЙТИ
    driver.implicitly_wait(3)
    try:
        driver.find_element(By.CLASS_NAME, 'main-header__left')             # ищем лого в хэдере, если вход не выполнен и лого не обнаружено - делаем скрин
    except:
        driver.save_screenshot('error auth.png')
    driver.implicitly_wait(3)
    lk = driver.find_element(By.XPATH, '//*[@id="app"]/main/div/div[2]/div[1]/div[1]/div[1]/h2').text
    out_btn = driver.find_element(By.ID, 'logout-btn').click()  # Кнопка ВЫЙТИ
    assert len(lk) > 4

# Тест-Кейс Auth-121 Проверяем авторизацию через Лицевой счёт, недействующего пользователя, появление ошибки о неверном логине или пароле
def test_auth_num_account_notactual(driver):
    account_btn = driver.find_element(*AuthType.TYPE_ACCOUNT).click()
    driver.find_element(*AuthType.TYPE_SAVE_ME).click()  # отключаем режим "Запомнить меня"
    input_account = driver.find_element(*AuthLocators.AUTH_LOGIN).send_keys(notactual_account)
    input_pass = driver.find_element(*AuthLocators.AUTH_PASS).send_keys(notactual_pass)
    driver.find_element(*AuthLocators.AUTH_ENTER).click()   # Кнопка ВОЙТИ
    account_error = driver.find_element(By.ID, 'form-error-message').text
    driver.back()
    assert account_error == 'Неверный логин или пароль'

# Тест-Кейс Auth-122 Проверяем маску ввода под 12 символов нижнего подчёркивания в поле ввода номер лицевого счёта
def test_auth_num_account_input_maska(driver):
    account_btn = driver.find_element(*AuthType.TYPE_ACCOUNT).click()
    input_account = driver.find_element(*AuthLocators.AUTH_LOGIN).click()
    input_maska = driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/div/span[1]/span[2]').text
    assert input_maska == '____________'

# Тест-Кейс Auth-123 Проверяем поле ввода Лицевой счёт на появление ошибки при вводе пустого значения и неполного лицевого счёта
@pytest.mark.parametrize("account", ['', '1'], ids=["empty", "one value"])
def test_auth_num_account_input(driver, account):
    account_btn = driver.find_element(*AuthType.TYPE_ACCOUNT).click()
    driver.find_element(*AuthType.TYPE_SAVE_ME).click()  # отключаем режим "Запомнить меня"
    input_account = driver.find_element(*AuthLocators.AUTH_LOGIN).send_keys(account)
    input_pass = driver.find_element(*AuthLocators.AUTH_PASS).send_keys(notactual_pass)
    driver.find_element(*AuthLocators.AUTH_ENTER).click()  # Кнопка ВОЙТИ
    account_error = driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/span').text
    driver.refresh()
    assert len(account_error) > 34

# Тест-Кейс Auth-124 Проверяем поле ввода Лицевой счёт на появление ошибки при вводе невалидных значений
@pytest.mark.parametrize("account", ['abcd', 'абвг', '!@#$%^&*()'], ids=["latin", "cyrillic", "special characters"])
def test_auth_num_account_input_notvalid(driver, account):
    account_btn = driver.find_element(*AuthType.TYPE_ACCOUNT).click()
    driver.find_element(*AuthType.TYPE_SAVE_ME).click()  # отключаем режим "Запомнить меня"
    input_account = driver.find_element(*AuthLocators.AUTH_LOGIN).send_keys(account)
    driver.find_element(*AuthLocators.AUTH_ENTER).click()  # Кнопка ВОЙТИ
    account_error = driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/span').text
    assert account_error == 'Введите номер вашего лицевого счета'
    input_account = driver.find_element(*AuthLocators.AUTH_LOGIN).text
    assert len(input_account) == 0

# Тест-Кейс Auth-106 Проверяем авторизацию по номеру телефона действующего пользователя, проверяем в личном кабинете количество символов "имя + фамилия" больше 4 символов
def test_auth_tel_actual(driver):
    tel_btn = driver.find_element(*AuthType.TYPE_TELEFON).click()
    driver.find_element(*AuthType.TYPE_SAVE_ME).click()  # отключаем режим "Запомнить меня"
    input_tel = driver.find_element(*AuthLocators.AUTH_LOGIN).send_keys(actual_tel)
    input_pass = driver.find_element(*AuthLocators.AUTH_PASS).send_keys(actual_pass)
    driver.find_element(*AuthLocators.AUTH_ENTER).click()   # Кнопка ВОЙТИ
    driver.implicitly_wait(3)
    try:
        driver.find_element(By.CLASS_NAME, 'main-header__left')             # ищем лого в хэдере, если вход не выполнен и лого не обнаружено - делаем скрин
    except:
        driver.save_screenshot('error auth.png')
    driver.implicitly_wait(5)
    lk = driver.find_element(By.XPATH, '//*[@id="app"]/main/div/div[2]/div[1]/div[1]/div[1]/h2').text
    out_btn = driver.find_element(By.ID, 'logout-btn').click()  # Кнопка ВЫЙТИ
    assert len(lk) > 4

# Тест-Кейс Auth-107 Проверяем авторизацию по номеру телефона недействующего пользователя, появление ошибки о неверном логине или пароле
def test_auth_tel_notactual(driver):
    tel_btn = driver.find_element(*AuthType.TYPE_TELEFON).click()
    driver.find_element(*AuthType.TYPE_SAVE_ME).click()  # отключаем режим "Запомнить меня"
    input_tel = driver.find_element(*AuthLocators.AUTH_LOGIN).send_keys(notactual_tel)
    input_pass = driver.find_element(*AuthLocators.AUTH_PASS).send_keys(notactual_pass)
    driver.find_element(*AuthLocators.AUTH_ENTER).click()   # Кнопка ВОЙТИ
    tel_error = driver.find_element(By.ID, 'form-error-message').text
    assert tel_error == 'Неверный логин или пароль'

# Тест-Кейс Auth-108 Проверяем маску поля ввода телефон, конвертация 8 в +7 и появление маски для 10 символов
def test_auth_tel_maska(driver):
    tel_btn = driver.find_element(*AuthType.TYPE_TELEFON).click()
    input_tel = driver.find_element(*AuthLocators.AUTH_LOGIN).send_keys('8')
    tel_maska_kod = driver.find_element(By.CLASS_NAME, 'rt-input__mask-start').text
    tel_maska = driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/div/span[1]/span[2]').text
    assert tel_maska_kod == '+7'
    assert tel_maska == '___ ___-__-__'

# Тест-Кейс Auth-109 Проверяем поле ввода телефон на вывод сообщение о неверном вводе и проверка ограничения ввода в 11 символов
def test_auth_tel_input_info_error(driver):
    driver.refresh()
    driver.find_element(*AuthType.TYPE_SAVE_ME).click()  # отключаем режим "Запомнить меня"
    input_pass = driver.find_element(*AuthLocators.AUTH_PASS).send_keys(notactual_pass)
    driver.find_element(*AuthLocators.AUTH_ENTER).click()  # Кнопка ВОЙТИ
    tel_error1 = driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/span').text
    input_tel = driver.find_element(*AuthLocators.AUTH_LOGIN).send_keys('8902')
    driver.find_element(*AuthLocators.AUTH_ENTER).click()  # Кнопка ВОЙТИ
    tel_error2 = driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/span').text
    input_tel = driver.find_element(*AuthLocators.AUTH_LOGIN).send_keys('123456789')
    tel_test = driver.find_element(By.NAME, 'username').get_attribute("value")
    assert tel_error1 == 'Введите номер телефона'
    assert tel_error2 == 'Неверный формат телефона'
    assert len(tel_test) == 11        # проверяем количество символов, принятых полем ввода телефон

# Тест-Кейс Auth-110 Проверяем поле ввода телефон на буквы и спец.символы, происходит переключения вида авторизации с "телефон" на вид "логин"
@pytest.mark.parametrize("tel", ['TestТест', '!@#$%^&*()'])
def test_auth_tel_input_notactual(driver, tel):
    tel_btn = driver.find_element(*AuthType.TYPE_TELEFON).click()
    input_tel = driver.find_element(*AuthLocators.AUTH_LOGIN).send_keys(tel)
    input_pass = driver.find_element(*AuthLocators.AUTH_PASS).click()
    input_change = driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/div/span[2]').text
    assert input_change == 'Логин'

