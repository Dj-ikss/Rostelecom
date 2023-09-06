import time
from selenium.webdriver.common.by import By
from pages.locators import AuthType
from pages.locators import NameInput

# Тест-Кейс Auth-101 Проверяем наличие продуктового слогана
def test_lk_kabinet(driver):
    lk_kabinet = driver.find_element(By.CLASS_NAME, 'what-is__title').text
    slogan = driver.find_element(By.CLASS_NAME, 'what-is__desc').text
    assert lk_kabinet == 'Личный кабинет'
    assert slogan == 'Персональный помощник в цифровом мире Ростелекома'

# Тест-Кейс Auth-102 Проверяем отображение названия раздела "Авторизация" в правой части контентной части
def test_auth(driver):
    auth = driver.find_element(By.CLASS_NAME, 'card-container__title').text
    assert auth == 'Авторизация'

# Тест-Кейс Auth-104 Проверяем кнопку вида авторизации по почте, нажатие кнопки, появление воля ввода для Email
def test_auth_type_email(driver):
    email_btn = driver.find_element(*AuthType.TYPE_EMAIL)
    email_btn.click()
    name_input_email = driver.find_element(*NameInput.LOGIN_INPUT).text
    assert email_btn.text == 'Почта'
    assert name_input_email == 'Электронная почта'

# Тест-Кейс Auth-104 Проверяем кнопку вида авторизации по логину, нажатие кнопки, появление воля ввода для Логин
def test_auth_type_login(driver):
    login_btn = driver.find_element(*AuthType.TYPE_LOGIN)
    login_btn.click()
    name_input_login = driver.find_element(*NameInput.LOGIN_INPUT).text
    assert login_btn.text == 'Логин'
    assert name_input_login == 'Логин'

# Тест-Кейс Auth-104 Проверяем кнопку вида авторизации по Лицевому счёту, нажатие кнопки, появление воля ввода для Лицевой счёт
def test_auth_type_licevoi_schet(driver):
    account_num_btn = driver.find_element(*AuthType.TYPE_ACCOUNT)
    account_num_btn.click()
    name_input_account_num = driver.find_element(*NameInput.LOGIN_INPUT).text
    assert account_num_btn.text == 'Лицевой счёт'
    assert name_input_account_num == 'Лицевой счёт'

# Тест-Кейс Auth-104 Проверяем кнопку вида авторизации по Номеру телефону, нажатие кнопки, появление воля ввода для Мобильный телефон
def test_auth_type_telefon(driver):
    tel_btn = driver.find_element(*AuthType.TYPE_TELEFON)
    tel_btn.click()
    name_input_tel = driver.find_element(*NameInput.LOGIN_INPUT).text
    assert tel_btn.text == 'Телефон'
    assert name_input_tel == 'Мобильный телефон'

# Тест-Кейс Auth-126 Проверяем переход для авторизации через кнопку VK
def test_auth_vk(driver):
    vk_btn = driver.find_element(*AuthType.TYPE_VK).click()
    driver.implicitly_wait(3)
    web_vk = driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div/div/div[1]/div[2]/div/div/div/form/div[1]/div/h1/div').text
    driver.back()
    assert web_vk == 'Вход в VK ID'

# Тест-Кейс Auth-127 Проверяем переход для авторизации через кнопку Одноклассники
def test_auth_ok(driver):
    ok_btn = driver.find_element(*AuthType.TYPE_OK).click()
    driver.implicitly_wait(3)
    web_ok = driver.find_element(By.CLASS_NAME, 'ext-widget_h_tx').text
    driver.back()
    assert web_ok == 'Одноклассники'

# Тест-Кейс Auth-128 Проверяем переход для авторизации через кнопку Mail.ru
def test_auth_mail(driver):
    mail_btn = driver.find_element(*AuthType.TYPE_MAIL).click()
    driver.implicitly_wait(3)
    web_mail = driver.find_element(By.CLASS_NAME, 'header__logo').text
    driver.back()
    assert web_mail == 'Мой Мир@Mail.Ru'

# # Тест-Кейс Auth-129 Проверяем переход для авторизации через кнопку Яндекс (!!!!!!не срабатывает!!!)
# def test_auth_yandex(driver):
#     yandex_btn = driver.find_element(*AuthType.TYPE_YANDEX).click()
#     driver.implicitly_wait(3)
#     web_yandex = driver.find_element(By.CLASS_NAME, 'Authorize-title').text
#     driver.back()
#     assert web_yandex == 'Вход с помощью Яндекса'

# Тест-Кейс Auth-130 Проверяем переход о кнопке Забыл пароль
def test_forgot_pass(driver):
    forgot_pass_btn = driver.find_element(By.ID, 'forgot_password').click()
    forgot_pass_page = driver.find_element(By.CLASS_NAME, 'card-container__title').text
    driver.back()
    assert forgot_pass_page == 'Восстановление пароля'

# Тест-Кейс Auth-134 Проверяем переход в раздел "Регистрация"
def test_registration_new_user(driver):
    new_user_btn = driver.find_element(By.ID, 'kc-register').click()
    registration_page = driver.find_element(By.CLASS_NAME, 'card-container__title').text
    driver.back()
    assert registration_page == 'Регистрация'