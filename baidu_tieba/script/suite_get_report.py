# 导包
import unittest

from tools.HTMLTestRunner import HTMLTestRunner
# 定义测试套件
suite = unittest.defaultTestLoader.discover('', pattern='test*.py')

# 实例化HTMLTestRunner类，并调用run方法执行测试套件
with open('../report/tb_test.html', 'wb') as f:
    HTMLTestRunner(stream=f, title='百度贴吧发帖测试报告').run(suite)
