import time
from selenium.webdriver.common.by import By


# Тест кейс Auth-201 Футер, проверяем наличие информации о возрастном ограничении
def test_limit_age(driver):
    limit_age = driver.find_element(By.XPATH, '//*[@id="app-footer"]/div[1]/div[1]').text
    # print(limit_age)
    assert limit_age == '© 2023 ПАО «Ростелеком». 18+'

# Тест-Кейс Auth-203 Футер, проверяем всплывающее окно "Мы используем Cookie"
def test_cookies_info(driver):
    cookies_btn = driver.find_element(By.ID, 'cookies-tip-open').click()
    about_cookies = driver.find_element(By.CLASS_NAME, 'rt-tooltip__title').text
    assert about_cookies == 'Мы используем Cookie'

# Тест кейс Auth-204 Футер, проверяем открытие политики конфидециальности в новой вкладке
# Тест кейс Auth-205 Футер, проверяем открытие пользовательского соглашения в новой вкладке
def test_agreement_info(driver):
    driver.find_element(By.CSS_SELECTOR, '#rt-footer-agreement-link > span:nth-child(1)').click()
    driver.find_element(By.CSS_SELECTOR, '#rt-footer-agreement-link > span:nth-child(2)').click()
    driver.switch_to.window(driver.window_handles[1])
    agreement1 = driver.find_element(By.CLASS_NAME, 'offer-title').text
    driver.switch_to.window(driver.window_handles[2])
    agreement2 = driver.find_element(By.CLASS_NAME, 'offer-title').text
    driver.switch_to.window(driver.window_handles[0])
    assert agreement1 == 'Публичная оферта о заключении Пользовательского соглашения на использование Сервиса «Ростелеком ID»'
    assert agreement2 == 'Публичная оферта о заключении Пользовательского соглашения на использование Сервиса «Ростелеком ID»'

# Тест кейс Auth-206 Футер, проверяем наличие и соответствие номера тел. тех.поддержки
def test_support_tel(driver):
    num_tel = driver.find_element(By.CLASS_NAME, 'rt-footer-right__support-phone').text
    assert num_tel == '8 800 100 0 800'