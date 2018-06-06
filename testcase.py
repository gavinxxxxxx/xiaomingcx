# coding=utf-8

import ann
import account
import time
import usecar
import person_center

driver = ann.init()
account.login_first(driver)
# usecar.start_use(driver)  # 立即用车
# time.sleep(60)  # 等待一分钟
# usecar.end_use(driver)  # 结束用车
person_center.common_problems(driver)

ann.quit(driver)




