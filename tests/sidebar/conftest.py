import time
from utils.android_utils import android_get_desired_capabilities
from appium import webdriver
from selenium.webdriver.common.by import By
import pytest


@pytest.fixture
def login_preset_driver():
    driver = webdriver.Remote('http://0.0.0.0:4723/wd/hub',
                              desired_capabilities=android_get_desired_capabilities())

    driver.implicitly_wait(5)
    driver.find_element(By.ID, 'com.ajaxsystems:id/login').click()
    password_field = driver.find_element(By.ID, 'com.ajaxsystems:id/password')
    password_field.clear()
    password_field.send_keys('qa_automation_password')

    email_field = driver.find_element(By.ID, 'com.ajaxsystems:id/login')
    email_field.clear()
    email_field.send_keys('qa.ajax.app.automation@gmail.com')

    driver.find_element(By.ID, 'com.ajaxsystems:id/next').click()
    time.sleep(2)
    return driver
