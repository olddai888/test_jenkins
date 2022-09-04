'''
    定义字典
'''

# 导包
import random
from time import sleep

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By

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
    'appActivity': '.activity.LoadingActivity',

    # 设置支持中文的输入格式
    'unicodeKeyboard': True,

    'resetKeyboard': True,

    # 保持登录状态
    # 'noReset': True

}

# 初始化加载对象
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

# 设置隐式等待
driver.implicitly_wait(20)

# 随机2-3秒暂停时间
sleep(float("%.3f" % (random.uniform(2, 3))))

# 点击‘同意’按钮
driver.find_element(By.XPATH, '//*[@text="同意"]').click()

# 随机2-3秒暂停时间
sleep(float("%.3f" % (random.uniform(2, 3))))

# 点击‘允许’进行授权
driver.find_element(By.XPATH, '//*[@text="允许"]').click()

# 随机2-3秒暂停时间
sleep(float("%.3f" % (random.uniform(2, 3))))

# 再次点击‘允许’进行授权
driver.find_element(By.XPATH, '//*[@text="允许"]').click()

# 随机2-3秒暂停时间
sleep(float("%.3f" % (random.uniform(2, 3))))

# 点击‘其他登录方式’进入登录页面
driver.find_element(By.XPATH, '//*[@text="其他登录方式"]').click()

# 随机2-3秒暂停时间
sleep(float("%.3f" % (random.uniform(2, 3))))

# 选择网易邮箱登录
driver.find_element(By.ID, 'com.netease.cloudmusic:id/mail').click()

# 随机2-3秒暂停时间
sleep(float("%.3f" % (random.uniform(2, 3))))

# 点击‘同意并继续’按钮
driver.find_element(By.XPATH, '//*[@text="同意并继续"]').click()

# 随机2-3秒暂停时间
sleep(float("%.3f" % (random.uniform(2, 3))))

# 输入邮箱
driver.find_element(By.XPATH, '//*[@text="请输入邮箱账号"]').send_keys('123')

# 随机2-3秒暂停时间
sleep(float("%.3f" % (random.uniform(2, 3))))

# 输入密码
driver.find_element(By.XPATH, '//*[@text="请输入密码"]').send_keys('123')

# 随机2-3秒暂停时间
sleep(float("%.3f" % (random.uniform(2, 3))))

driver.tap([])

# driver.get_screenshot_as_file()

driver.start_activity(app_package='com.netease.cloudmusic', app_activity='.activity.PlayListActivity')

'com.netease.cloudmusic/.activity.PlayListActivity'

driver.press_keycode()

# ---------------------------------------------------
# driver.drag_and_drop(a1, b2)





























# 关闭驱动
driver.quit()