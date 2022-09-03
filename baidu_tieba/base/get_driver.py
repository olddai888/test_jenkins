# 导包
from selenium import webdriver

# 创建获取driver类
from page import url


class GetDriver:
    # 定义类属性driver为空
    driver = None

    # 定义类方法获取driver
    @classmethod
    def get_driver(cls):
        # 判断driver的值是否为空 若为否，则跳过
        if cls.driver is None:
            # 创建driver对象
            cls.driver = webdriver.Chrome()
            # 获取请求url
            cls.driver.get(url)
            # 最大化浏览器窗口
            cls.driver.maximize_window()
        # 返回driver对象
        return cls.driver

    # 定义关闭驱动类方法
    @classmethod
    def quit_driver(cls):
        # 判断cls.driver不为空
        if cls.driver:  # ==> cls.driver is not None
            # 关闭驱动
            cls.driver.quit()
            # 置空
            cls.driver = None
