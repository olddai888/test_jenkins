# 导包
import time

# 创建基类
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait


class Base:
    # 初始化方法
    def __init__(self, driver):
        self.driver = driver

    # 定义查找元素方法
    def base_find_element(self, loc, timeout=30, poll=0.5):
        # 设置显示等待
        return WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll).until(lambda x: x.find_element(*loc))

    # 定义点击方法
    def base_click(self, loc):
        self.base_find_element(loc).click()

    # 定义输入方法
    def base_write(self, loc, text):
        # 查找元素并使用变量保存
        el = self.base_find_element(loc)
        # 清空搜索框
        el.clear()
        # 输入内容
        el.send_keys(text)

    # 定义切换到当前窗口的方法
    def base_switch_window(self):
        # 获取当前窗口句柄
        # handle = self.driver.current_window_handle
        # 获取所有窗口句柄
        handles = self.driver.window_handles
        # 切换到最后一个窗口
        self.driver.switch_to.window(handles[-1])
        # 循环遍历所有窗口句柄
        # for h in handles:
        #     # 判断句柄非当前窗口句柄
        #     if h != handle:
        #         # 利用句柄将焦点切换到当前窗口
        #         self.driver.switch_to_window(h)

    # 滚动方法
    # def base_drag_and_drop(self, loc1, loc2):
    #     # 创建鼠标对象
    #     mouse = ActionChains(self.driver)
    #     # 定义两个元素
    #     el1 = self.base_find_element(loc1)
    #     el2 = self.base_find_element(loc2)
    #     # 从第一个元素滚动到第二个元素
    #     mouse.drag_and_drop(el1, el2).perform()

    # 定义获取提示框信息方法
    def base_get_attribute(self, loc):
        # 获取提示框文本信息
        return self.base_find_element(loc).text

    # 定义截图方法
    def base_screen(self):
        self.driver.get_screenshot_as_file(f'../image/{time.strftime("%Y_%m_%d %H_%M_%S")}.png')
