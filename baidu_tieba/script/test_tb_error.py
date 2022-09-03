# 导包
import random
import unittest
from time import sleep

from parameterized import parameterized
from base.get_driver import GetDriver
from base.get_logger import GetLogger
from base.read_json import read_json
from page.page_tieba import Page

# 初始化log对象
# log = GetLogger.tb_logging()


# 定义读取测试数据方法(登录失败，密码错误)
def get_data_error():
    datas = read_json('tb_error.json')

    # 定义空列表
    list_data2 = []
    # 循环遍历字典，并将获取到的值写入列表中
    for i in datas.values():
        list_data2.append((i['username'], i['password']))

    # 返回列表
    return list_data2


class TestTb(unittest.TestCase):
    # 设置类属性为空
    tb = None
    driver = None

    # 定义用例执行前的方法
    @classmethod
    def setUpClass(cls) -> None:
        try:
            # 初始化driver对象
            cls.driver = GetDriver.get_driver()
            # 初始化页面对象
            cls.tb = Page(cls.driver)
            # 进入登录页面
            cls.tb.page2()
        except Exception as e:
            print(e)

    # 定义用例执行之后的方法
    @classmethod
    def tearDownClass(cls) -> None:
        GetDriver.quit_driver()

    # 定义测试方法(登录失败)
    @parameterized.expand(get_data_error())
    def test_02(self, username, password):
        # 输入用户名和密码并点击登录
        self.tb.page3(username, password)
        # 随机8到9秒休眠时间
        sleep(float("%.3f" % (random.uniform(8, 9))))
        # 捕获异常
        try:
            # 获取实际结果
            msg = self.tb.page_login_password_error()
            # 断言
            self.assertEqual('找回密码', str(msg))
        except AssertionError:
            # 错误截图
            self.tb.base_screen()
            raise
        # 截图
        self.tb.page_screenshot()
