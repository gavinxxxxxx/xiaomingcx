# coding=utf-8

# 个人中心

from appium import webdriver

import ann
import keys


# 设置

#  常见问题
def common_problems(driver: webdriver):
    ann.sleep()
    driver.find_element_by_id('com.xm.xmapp:id/iv_person').click()  # 点个人中心
    ann.sleep()
    print('--【设置】--')
    driver.find_element_by_id('com.xm.xmapp:id/tv_setting').click()  # 点设置
    ann.sleep()
    print('--【常见问题】--')
    driver.find_elements_by_id('com.xm.xmapp:id/rel')[3].click()  # 点常见问题
    print('--【常见问题页面正常】--')
    ann.sleep()
    driver.keyevent(keys.KEYCODE_BACK)  # 点返回键
    print('--【用户协议】--')
    ann.sleep()
    driver.find_elements_by_id('com.xm.xmapp:id/rel')[4].click()  # 点用户协议
    print('--【用户协议页面正常】--')
    ann.sleep()
    driver.keyevent(keys.KEYCODE_BACK)  # 点返回键
    print('--【车辆指引】--')
    ann.sleep()
    driver.find_elements_by_id('com.xm.xmapp:id/rel')[5].click()  # 点车辆指引
    print('--【车辆指引页面正常】--')
    ann.sleep()
    driver.keyevent(keys.KEYCODE_BACK)  # 点返回键
    print('--【关于我们】--')
    ann.sleep()
    driver.find_elements_by_id('com.xm.xmapp:id/rel')[7].click()  # 点关于我们
    ann.sleep()
    driver.find_elements_by_id('com.xm.xmapp:id/rel')[1].click()  # 检查版本更新
    print('--【关于页面正常】--')
    ann.sleep()
    driver.keyevent(keys.KEYCODE_BACK)  # 点返回键
