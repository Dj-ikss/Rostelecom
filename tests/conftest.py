import time

from selenium import webdriver
import pytest



@pytest.fixture(scope="session")
def driver():
    chrome_driver = webdriver.Chrome()
    link = 'https://b2c.passport.rt.ru/'
    chrome_driver.get(link)
    chrome_driver.maximize_window()  # макс размер экрана
    time.sleep(3)
    return chrome_driver
