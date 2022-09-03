# 导包
import random
from time import sleep

from base.base_tieba import Base
import page


# 定义页面类并继承基类
class Page(Base):
    # 查找贴吧入口并点击
    def page_forum_click(self):
        # 随机生成2-3秒休眠时间，保留3位小数
        sleep(float("%.3f" % (random.uniform(2, 3))))
        self.base_click(page.loc_forum)

    # 切换到当前窗口
    def page_switch_to_window_now(self):
        # 随机生成2-3秒休眠时间，保留3位小数
        sleep(float("%.3f" % (random.uniform(2, 3))))
        self.base_switch_window()

    # 点击登录方法（可能因为令牌原因找不到按钮）
    def page_login(self):
        # 随机生成2-3秒休眠时间，保留3位小数
        sleep(float("%.3f" % (random.uniform(2, 3))))
        self.base_click(page.loc_login)

    # 点击用户名登录方法
    def page_login_user(self):
        # 随机生成2-3秒休眠时间，保留3位小数
        sleep(float("%.3f" % (random.uniform(2, 3))))
        self.base_click(page.loc_login_user)

    # 在手机号/用户名/邮箱输入框中输入内容
    def page_login_username(self, username):
        # 随机生成2-3秒休眠时间，保留3位小数
        sleep(float("%.3f" % (random.uniform(2, 3))))
        self.base_write(page.loc_login_username, username)

    # 在密码框中输入内容
    def page_login_password(self, password):
        # 随机生成2-3秒休眠时间，保留3位小数
        sleep(float("%.3f" % (random.uniform(2, 3))))
        self.base_write(page.loc_login_password, password)

    # 点击登录页面的登录按钮
    def page_login_button(self):
        # 随机生成2-3秒休眠时间，保留3位小数
        sleep(float("%.3f" % (random.uniform(2, 3))))
        self.base_click(page.loc_login_button)

    # 点击体育分类的NBA按钮
    def page_sports_nba(self):
        # 随机生成2-3秒休眠时间，保留3位小数
        sleep(float("%.3f" % (random.uniform(18, 19))))
        self.base_click(page.loc_sports_nba)

    # 点击湖人吧
    def page_lakers(self):
        # 随机生成2-3秒休眠时间，保留3位小数
        sleep(float("%.3f" % (random.uniform(2, 3))))
        self.base_click(page.loc_lakers)

    # 点击发帖
    def page_publish_click_page(self):
        # 随机生成2-3秒休眠时间，保留3位小数
        sleep(float("%.3f" % (random.uniform(2, 3))))
        self.base_click(page.loc_publish_page)

    # 输入标题
    def page_publish_title(self, title):
        # 随机生成2-3秒休眠时间，保留3位小数
        sleep(float("%.3f" % (random.uniform(2, 3))))
        self.base_write(page.loc_publish_title, title)

    # 在手机号/用户名/邮箱输入框中输入内容
    def page_publish_tz_text(self, text):
        # 随机生成2-3秒休眠时间，保留3位小数
        sleep(float("%.3f" % (random.uniform(2, 3))))
        self.base_write(page.loc_publish_text, text)

    # 点击发表帖子
    def page_publish_click_button(self):
        # 随机生成2-3秒休眠时间，保留3位小数
        sleep(float("%.3f" % (random.uniform(2, 3))))
        self.base_click(page.loc_publish_click)

    # 刷新
    # def page_refresh(self):
    #     self.driver.refresh()

    # 点击右上角用户名导航栏下面的我的贴吧
    # def page_my_tb(self):
    #     self.base_click(page.loc_my_tb)

    # 点击我的帖子
    # def page_my_tz(self):
    #     self.base_click(page.loc_my_tz)

    # 查看我的帖子标题并返回标题内容
    # def page_find_my_tz_title(self):
    #     return self.base_find_element(page.loc_my_tz_title).text
    # 获取密码错误结果信息
    def page_login_password_error(self):
        return self.base_get_attribute(page.loc_login_password_error)

    # 获取发布结果信息
    def page_publish_success(self):
        return self.base_get_attribute(page.loc_publish_success)

    # 截图
    def page_screenshot(self):
        self.base_screen()

    # 封装方法1(发布帖子成功)
    def page1(self, username, password, title, text):
        # 点击贴吧
        self.page_forum_click()
        # 切换窗口
        self.page_switch_to_window_now()
        # 点击登录（贴吧）
        self.page_login()
        # 点击用户名登录
        self.page_login_user()
        # 输入用户名
        self.page_login_username(username)
        # 输入密码
        self.page_login_password(password)
        # 点击登录（用户名登录）
        self.page_login_button()
        # 点击体育分类下的NBA
        self.page_sports_nba()
        # 切换窗口
        self.page_switch_to_window_now()
        # 点击洛杉矶湖人吧
        self.page_lakers()
        # 切换窗口
        self.page_switch_to_window_now()
        # 点击右侧发帖按钮
        self.page_publish_click_page()
        # 输入帖子标题
        self.page_publish_title(title)
        # 输入帖子内容（选填）
        self.page_publish_tz_text(text)
        # 点击发表
        self.page_publish_click_button()
        # self.page_find_my_tz_title()

    # 封装方法2(进入登录界面)
    def page2(self):
        # 点击贴吧
        self.page_forum_click()
        # 切换窗口
        self.page_switch_to_window_now()
        # 点击登录（贴吧）
        self.page_login()
        # 点击用户名登录
        self.page_login_user()

    # 封装方法3（输入用户名和密码并点击登录）
    def page3(self, username, password):
        # 输入用户名
        self.page_login_username(username)
        # 输入密码
        self.page_login_password(password)
        # 点击登录（用户名登录）
        self.page_login_button()
