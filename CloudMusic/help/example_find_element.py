from time import sleep

from appium import webdriver
from selenium.webdriver.common.by import By

import page

desired_caps = {
    # 操作系统名称
    'platformName': 'Android',

    # 操作系统版本
    'platformVersion': '7.1.2',

    # 设备名称（随意）
    'deviceName': 'android 7.1.2',

    # 要打开的应用程序的包名
    'appPackage': 'com.netease.cloudmusic',

    # 要打开的界面
    'appActivity': '.module.login.LoginActivity',

    # 设置支持中文的输入格式
    'unicodeKeyboard': True,

    'resetKeyboard': True,

    # 保持登录状态
    # 'noReset': True

}

loc_email = By.XPATH, '//*[@text="请输入邮箱账号"]'

# 初始化加载对象
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

# 设置隐式等待
driver.implicitly_wait(60)

driver.find_element(By.ID, 'com.netease.cloudmusic:id/email').send_keys('c9033902weiquan@163.com')

sleep(3)

driver.quit()