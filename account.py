# coding=utf-8

# 账号相关

from selenium.common.exceptions import NoSuchElementException

import ann
import keys


# 登录
def login(driver):
    # ann.sleep_long()
    # driver.find_element_by_id('com.xm.xmapp:id/iv_person').click()
    ann.sleep()
    driver.find_element_by_id('com.xm.xmapp:id/et_phone').send_keys(u"13689521331")
    ann.sleep()
    driver.find_element_by_id('com.xm.xmapp:id/et_password').send_keys(u"123456")
    ann.sleep()
    driver.find_element_by_id('com.xm.xmapp:id/tv_login').click()
    ann.wait(driver)


# 验证是否登录
def login_first(driver):  # 进入应用首页后，如果没登录，先登录
    ann.wait(driver)
    driver.find_element_by_id('com.xm.xmapp:id/iv_person').click()  # 点个人中心
    ann.sleep()
    try:
        driver.find_element_by_id('com.xm.xmapp:id/tv_login')  # 尝试找登录页面的登录按钮
    except NoSuchElementException:
        driver.keyevent(keys.KEYCODE_BACK)  # 没找到的话点返回键
    else:
        login(driver)  # 登录


def logout(driver):
    # 退出登录
    ann.sleep()
    driver.find_element_by_id('com.xm.xmapp:id/iv_person').click()  # 点个人中心
    ann.sleep()
    driver.find_element_by_id('com.xm.xmapp:id/tv_setting').click()  # 点设置
    ann.sleep()
    driver.find_element_by_id('com.xm.xmapp:id/tv_exit').click()  # 点退出
    ann.sleep()
    driver.find_element_by_id('com.xm.xmapp:id/tv_exit').click()  # 点确定
