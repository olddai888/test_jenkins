import unittest

from parameterized import parameterized

from base.get_driver import GetDriver
from base.read_json import read_json
from page.page_music import Page_music


# 读取数据
def get_data():
    # 使用变量保存数据
    datas = read_json('login.json')
    # 定义空列表
    list_data1 = []
    # 循环遍历数据
    for i in datas.values():
        # 添加数据到列表
        list_data1.append((i['email'], i['password'], i['name']))
    # 返回列表
    return list_data1


# 测试类
class Test_music(unittest.TestCase):
    # 类属性为空
    driver = None

    # 前置类方法
    @classmethod
    def setUpClass(cls) -> None:
        # 捕获异常
        try:
            # 初始化driver对象
            cls.driver = GetDriver.get_driver()
            # 初始化页面对象
            cls.pg = Page_music(cls.driver)
        except Exception as e:
            # 打印异常信息
            print(e)

    # 后置类方法
    @classmethod
    def tearDownClass(cls) -> None:
        # 关闭驱动
        GetDriver.quit_driver()

    # 数据驱动
    @parameterized.expand(get_data())
    def test_01(self, email, password, name):
        # print(email, password, name)
        # 调用封装方法
        self.pg.page1(email, password, name)

