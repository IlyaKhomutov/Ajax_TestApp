import serial.tools.list_ports


def phone_id():
    for i in serial.tools.list_ports.comports():
        ser = i.hwid.split(' ')[2][4:]
        return ser


def android_get_desired_capabilities():
    return {
        'autoGrantPermissions': True,
        'automationName': 'uiautomator2',
        'newCommandTimeout': 500,
        'noSign': True,
        'platformName': 'Android',
        'platformVersion': '11',
        'resetKeyboard': True,
        'systemPort': 8210,
        'takesScreenshot': True,
        'udid': phone_id(),
        'appPackage': 'com.ajaxsystems',
        'appActivity': 'com.ajaxsystems.ui.activity.LauncherActivity'
    }
