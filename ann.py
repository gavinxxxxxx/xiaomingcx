# coding=utf-8

import time

from appium import webdriver


def init():
    desired_caps = {
        'platformName': 'Android',
        'deviceName': '127.0.0.1:62001',
        'platformVersion': '4.4',
        'appPackage': 'com.xm.xmapp',
        'appActivity': 'com.xm.xmapp.activity.StartActivity',
        # 'appWaitActivity': "",
        'unicodeKeyboard': True,
        'resetKeyboard': True
    }
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    return driver


def sleep():
    time.sleep(3)


def sleep_long():
    time.sleep(10)


def wait(driver):
    driver.implicitly_wait(10)


def quit(driver):
    time.sleep(8)
    driver.quit()  # 退出当前操作