import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

import pytest


@pytest.fixture()
def driver():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    browser = webdriver.Chrome(options=options)
    return browser


def test_sale(driver):
    driver.get('https://staging.extra.ge/')

    userName = driver.find_element(By.ID, 'username')
    userName.send_keys('scByKxLa36Wcypju')

    password = driver.find_element(By.ID, 'password')
    password.send_keys('DbeGwVkuLee9Zjvf')

    driver.find_element(By.XPATH, "//button[contains(text(), ' Sign In ')]").click()
    time.sleep(1.0)
    driver.close()

# //button//i[contains(@class, "_x_icon-user-profile-1")]
