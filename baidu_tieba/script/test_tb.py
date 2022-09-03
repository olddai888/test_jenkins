# 导包
import unittest
from parameterized import parameterized
from base.get_driver import GetDriver
from base.get_logger import GetLogger
from base.read_json import read_json
from page.page_tieba import Page

# 初始化log对象
# log = GetLogger.tb_logging()


# 定义读取测试数据方法(发布成功)
def get_data_publish_success():
    datas = read_json('tb.json')

    # 定义空列表
    list_data1 = []
    # 循环遍历字典，并将获取到的值写入列表中
    for i in datas.values():
        list_data1.append((i['username'], i['password'], i['title'], i['text']))

    # 返回列表
    return list_data1


class TestTb(unittest.TestCase):
    # 设置driver为空
    driver = None

    # 定义用例执行前的方法
    @classmethod
    def setUpClass(cls) -> None:
        try:
            # 初始化driver对象
            cls.driver = GetDriver.get_driver()
            # 初始化页面对象
            cls.tb = Page(cls.driver)
        except Exception as e:
            print(e)

    # 定义用例执行之后的方法
    @classmethod
    def tearDownClass(cls) -> None:
        GetDriver.quit_driver()

    # 定义测试方法(发帖成功)
    @parameterized.expand(get_data_publish_success())
    def test_01(self, username, password, title, text):
        # 调用封装方法1（发布帖子成功）
        self.tb.page1(username, password, title, text)
        try:
            msg = self.tb.page_publish_success()
            self.assertEqual('发表成功！', str(msg))
        except AssertionError:
            self.tb.base_screen()
            raise
        # 截图
        self.tb.page_screenshot()




