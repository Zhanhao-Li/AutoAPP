import time
from appium import webdriver


class BaseDriver:
    __driver = None
    __switch = False

    @classmethod
    def get_driver(cls,switch):
        cls.__switch = switch
        if not cls.__driver and not cls.__switch:
            desired_caps = dict()
            desired_caps["platformName"] = "android"
            desired_caps["platformVersion"] = "5.1"
            desired_caps["deviceName"] = "127.0.0.1:62001"
            desired_caps["appPackage"] = "com.android.settings"
            desired_caps["appActivity"] = ".Settings"
            desired_caps["unicodeKeyboard"] = True
            desired_caps["resetKeyboard"] = True
            desired_caps["automationName"] = "Uiautomator2"
            cls.__driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
            return cls.__driver

    @classmethod
    def quit_driver(cls,switch):
        cls.__switch = switch
        if cls.__driver and cls.__switch:
            time.sleep(3)
            cls.__driver.quit()
            cls.__driver = None
