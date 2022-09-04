import time

from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.wait import WebDriverWait


class Base_music:
    def __init__(self, driver):
        self.driver = driver

    # 查找单个元素
    def base_find_element(self, loc, timeout=60, poll=0.5):
        return WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll).until(lambda x: x.find_element(*loc))

    # 查找一组元素
    def base_find_elements(self, loc, timeout=60, poll=0.5):
        return WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll).until(
            lambda x: x.find_elements(*loc))

    # 点击（短按）
    def base_click(self, loc):
        self.base_find_element(loc).click()

    # 长按
    def base_presses_long(self, loc, long_press_time):
        TouchAction.long_press(self.base_find_element(loc), duration=long_press_time)

    # 输入
    def base_send_keys(self, loc, value):
        self.base_find_element(loc).send_keys(value)

    # 跳转到指定界面
    def base_jump_to_activity(self, activity):
        # self.driver.start_activity(app_package=package, app_activity=activity)
        self.driver.start_activity(app_activity=activity)

    # 从某个元素滑动到另一个元素（）
    def base_slither(self, loc1, loc2):
        self.driver.drag_and_drop(loc1, loc2)

    # 按下按键
    def base_press_keycode(self, number):
        self.driver.press_keycode(number)

    # 截图
    def base_screen_shot(self):
        self.driver.get_screenshot_as_file(f'../image/{time.strftime("%Y_%m_%d %H_%M_%S")}.png')
