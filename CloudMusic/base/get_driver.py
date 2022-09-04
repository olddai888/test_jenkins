# 导包
from appium import webdriver

import page


# 获取driver类
class GetDriver:
    # 设置类属性为空
    driver = None

    # 初始化driver对象
    @classmethod
    def get_driver(cls):
        # 判断driver为空
        if cls.driver is None:
            cls.driver = webdriver.Remote('http://localhost:4723/wd/hub', page.desired_caps)
        # 返回driver
        return cls.driver

    # 关闭方法
    @classmethod
    def quit_driver(cls):
        # 判断driver不为空
        if cls.driver:  # ==> cls.driver is not None
            # 关闭驱动
            cls.driver.quit()
            # 置空
            cls.driver = None
