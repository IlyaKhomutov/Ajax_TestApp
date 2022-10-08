from loguru import logger
import time
from utils.android_utils import android_get_desired_capabilities
from appium import webdriver
from selenium.webdriver.common.by import By
import pytest

logger.add("debug.log", format="{time} {level} {message}",
           level="DEBUG", rotation="10KB", compression="zip")


class TestLogin:
    emails = [
        'wdqqffqwfqwfqf',
        'qa.ajax.app.automation@gmail.com'
    ]

    @pytest.mark.parametrize('email', emails)
    def test_user_login(self, email):
        self.driver = webdriver.Remote('http://0.0.0.0:4723/wd/hub',
                                       desired_capabilities=android_get_desired_capabilities())

        self.driver.implicitly_wait(5)

        self.driver.find_element(By.ID, 'com.ajaxsystems:id/login').click()

        password_field = self.driver.find_element(By.ID, 'com.ajaxsystems:id/password')
        password_field.clear()
        password_field.send_keys('qa_automation_password')

        email_field = self.driver.find_element(By.ID, 'com.ajaxsystems:id/login')
        email_field.clear()
        email_field.send_keys(email)
        self.driver.find_element(By.ID, 'com.ajaxsystems:id/next').click()
        time.sleep(7)
        try:
            if email == 'qa.ajax.app.automation@gmail.com':
                assert "com.ajaxsystems:id/loading" in self.driver.page_source
            else:
                assert "com.ajaxsystems:id/loading" not in self.driver.page_source
        except Exception as ex:
            logger.error("Something went wrong")
            raise ex
        else:
            logger.info(f"The app works correctly with email {email}")
        finally:
            self.driver.quit()
