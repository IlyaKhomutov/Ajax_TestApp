import time
from loguru import logger

from selenium.webdriver.common.by import By

logger.add("debug.log", format="{time} {level} {message}",
           level="DEBUG", rotation="10KB", compression="zip")

elems = ('com.ajaxsystems:id/cancel_button', 'com.ajaxsystems:id/menuDrawer', 'com.ajaxsystems:id/addHub',
         'com.ajaxsystems:id/backButton', 'com.ajaxsystems:id/menuDrawer', 'com.ajaxsystems:id/settings',
         'com.ajaxsystems:id/back', 'com.ajaxsystems:id/menuDrawer', 'com.ajaxsystems:id/help',
         'com.ajaxsystems:id/back', 'com.ajaxsystems:id/menuDrawer', 'com.ajaxsystems:id/logs',
         'com.ajaxsystems:id/athenaButton', 'com.ajaxsystems:id/menuDrawer', 'com.ajaxsystems:id/camera',
         'com.ajaxsystems:id/back')


def test_side_bar(login_preset_driver):
    def find_elem_by_id(element_id):
        assert login_preset_driver.find_element(By.ID, element_id).click() is None

    try:
        time.sleep(5)
        for elem in elems:
            find_elem_by_id(elem)
    except Exception as ex:
        logger.error("The app doesn't work correctly, sidebar test failed")
        raise ex
    else:
        logger.info("SideBar test was successful")
    finally:
        login_preset_driver.quit()
