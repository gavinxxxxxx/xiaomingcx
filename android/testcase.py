# coding=utf-8

from android import person_center, ann, account

driver = ann.init()
account.login_first(driver)
# usecar.start_use(driver)  # 立即用车
# time.sleep(60)  # 等待一分钟
# usecar.end_use(driver)  # 结束用车
person_center.common_problems(driver)

ann.quit(driver)




