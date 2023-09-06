import time
from selenium.webdriver.common.by import By



class AuthLocators:
    AUTH_LOGIN = (By.ID, 'username')  # Поле ввода: Телефон, Email, Логин, Лицевой счёт
    AUTH_PASS = (By.ID, 'password')  # Поле ввода: ПАРОЛЬ
    AUTH_ENTER = (By.ID, 'kc-login')  # Кнопка: ВОЙТИ


class AuthType:
    TYPE_EMAIL = (By.ID, 't-btn-tab-mail')  # Тип авторизации по Email
    TYPE_LOGIN = (By.ID, 't-btn-tab-login')  # Тип авторизации по ЛОГИН
    TYPE_ACCOUNT = (By.ID, 't-btn-tab-ls')  # Тип авторизации по Лицевой Счёт
    TYPE_TELEFON = (By.ID, 't-btn-tab-phone')  # Тип авторизации по Номеру Телефона
    TYPE_VK = (By.ID, 'oidc_vk')  # Тип авторизации через ВК
    TYPE_OK = (By.ID, 'oidc_ok')  # Тип авторизации через OK
    TYPE_MAIL = (By.ID, 'oidc_mail')  # Тип авторизации через MAIL.ru
    TYPE_YANDEX = (By.ID, 'oidc_ya')  # Тип авторизации через YANDEX
    TYPE_SAVE_ME = (By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[3]/div/span[1]')  # ЧекБокс "Запомнить меня"


class NameInput:
    LOGIN_INPUT = (
    By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/div/span[2]')  # Название поля ввода Логин
