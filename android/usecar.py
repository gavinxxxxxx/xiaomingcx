# coding=utf-8

# 租车还车

from android import keys, ann
import time
from selenium.common.exceptions import NoSuchElementException


# 立即用车
def start_use(driver):
    ann.sleep()
    print('--【立即用车】--')
    driver.find_element_by_id('com.xm.xmapp:id/iv_use_car').click()  # 点击首页的立即用车
    ann.sleep()
    driver.tap([(500, 900)])  # 选择车辆
    ann.sleep()
    driver.find_element_by_id('com.xm.xmapp:id/tv_use_car').click()  # 点击车辆详情的“立即用车”
    # ann.sleep()
    # driver.find_element_by_id('com.xm.xmapp:id/inputView').send_keys(u"123456")
    ann.sleep()
    driver.keyevent(keys.KEYCODE_1)
    time.sleep(1)
    driver.keyevent(keys.KEYCODE_2)
    time.sleep(1)
    driver.keyevent(keys.KEYCODE_3)
    time.sleep(1)
    driver.keyevent(keys.KEYCODE_4)
    time.sleep(1)
    driver.keyevent(keys.KEYCODE_5)
    time.sleep(1)
    driver.keyevent(keys.KEYCODE_6)
    return


# 结束用车
def end_use(driver):
    ann.sleep_long()
    print('--【结束用车】-- START --')
    driver.find_element_by_id('com.xm.xmapp:id/tv_finish_using').click()  # 点结束用车
    ann.sleep()
    # 判断是否有还车提醒
    # if driver.find_element_by_xpath('//android.widget.TextView[contains(@text,"还车提醒")]') is not None:
    #     driver.find_element_by_id('com.xm.xmapp:id/chongzhi').click()  # 点下一步
    #     ann.wait(driver)
    # driver.find_element_by_id('com.xm.xmapp:id/et_remark').send_keys(u"车位号")  # 输入车位号
    # ann.sleep()
    # driver.find_element_by_id('com.xm.xmapp:id/chongzhi').click()  # 点确定
    # 判断是否有还车提醒
    try:
        driver.find_element_by_xpath('//android.widget.TextView[contains(@text,"还车提醒")]')
    except NoSuchElementException:
        print('没有还车提醒')
    else:
        driver.find_element_by_id('com.xm.xmapp:id/chongzhi').click()  # 点下一步
        ann.wait(driver)
    # 判断是否有车位号
    try:
        driver.find_element_by_xpath('//android.widget.TextView[contains(@text,"拍照上传")]')
    except NoSuchElementException:
        print('无需拍照上传停车位')
    else:
        driver.find_element_by_id('com.xm.xmapp:id/et_remark').send_keys(u"车位号")  # 输入车位号
        ann.sleep()
        driver.find_element_by_id('com.xm.xmapp:id/chongzhi').click()  # 点确定:
    # ann.sleep()
    # driver.find_element_by_id('com.xm.xmapp:id/btn_get_verify_1').click()  # 点选择优惠券
    # ann.sleep()
    # driver.find_element_by_xpath('//android.widget.ImageView[1]').click()  # 选择优惠券
    ann.sleep()
    driver.find_element_by_id('com.xm.xmapp:id/tv_button_1').click()  # 点结算
    ann.sleep()
    # 判断是否有使用优惠券弹窗
    try:
        driver.find_element_by_id('com.xm.xmapp:id/iv_return_icon_nouse')
    except NoSuchElementException:
        print('没有使用优惠券弹窗')
    else:
        driver.find_element_by_id('com.xm.xmapp:id/iv_return_icon_nouse').click()  # 点暂不使用
        ann.sleep()
        driver.find_element_by_id('com.xm.xmapp:id/tv_button_1').click()  # 点结算
    ann.sleep()
    driver.find_element_by_id('com.xm.xmapp:id/right').click()  # 点确定
    driver.find_element_by_id('com.xm.xmapp:id/pay').click()  # 点立即支付
    print('--【结束用车】-- END --')