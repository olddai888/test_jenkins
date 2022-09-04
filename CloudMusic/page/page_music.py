import random
from time import sleep

from selenium.webdriver.common.by import By

import page
from base.base_music import Base_music


class Page_music(Base_music):
    # 点击同意按钮
    def page_click_agree(self):
        sleep(float("%.3f" % (random.uniform(2, 3))))
        self.base_click(page.loc_agree)

    # 点击允许（第一次）
    def page_click_permit1(self):
        sleep(float("%.3f" % (random.uniform(2, 3))))
        self.base_click(page.loc_permit1)

    # 点击允许（第一次）
    def page_click_permit2(self):
        sleep(float("%.3f" % (random.uniform(2, 3))))
        self.base_click(page.loc_permit2)

    # 点击其他登录方式
    def page_click_another_login(self):
        sleep(float("%.3f" % (random.uniform(2, 3))))
        self.base_click(page.loc_another_login)

    # 点击网易邮箱图标
    def page_click_wy_email(self):
        sleep(float("%.3f" % (random.uniform(2, 3))))
        self.base_click(page.loc_login_wy_email)

    # 点击同意并继续
    def page_click_agree_and_continue(self):
        sleep(float("%.3f" % (random.uniform(2, 3))))
        self.base_click(page.loc_agree_and_continue)

    # 输入邮箱
    def page_input_email(self, email):
        sleep(float("%.3f" % (random.uniform(2, 3))))
        self.base_send_keys(page.loc_email, email)

    # 输入密码
    def page_input_password(self, password):
        sleep(float("%.3f" % (random.uniform(2, 3))))
        self.base_send_keys(page.loc_password, password)

    # 点击登录
    def page_click_login_button(self):
        sleep(float("%.3f" % (random.uniform(2, 3))))
        self.base_click(page.loc_login_button)

    # 点击搜索框按钮
    def page_click_find_button(self):
        sleep(float("%.3f" % (random.uniform(2, 3))))
        self.base_click(page.loc_find_song)

    # 在顶部搜索框中输入歌曲名
    def page_input_song_name(self, song_name):
        sleep(float("%.3f" % (random.uniform(2, 3))))
        self.base_send_keys(page.loc_find_song_after, song_name)

    # 点击搜索
    def page_click_find(self):
        sleep(float("%.3f" % (random.uniform(2, 3))))
        self.base_click(page.loc_find_button)

    # 点击播放全部
    def page_click_first_record(self):
        sleep(float("%.3f" % (random.uniform(2, 3))))
        self.base_click(page.loc_broadcast_all)

    # 添加到我喜欢
    def page_click_add_like(self):
        sleep(float("%.3f" % (random.uniform(2, 3))))
        self.base_click(page.loc_add_like)

    # 跳转到我喜欢的音乐
    # def page_jump_to_my_music(self):
    #     sleep(float("%.3f" % (random.uniform(2, 3))))
    #     self.base_jump_to_activity(activity=page.loc_like_activity)

    # 按下返回键
    def page_press_keycode(self):
        sleep(float("%.3f" % (random.uniform(2, 3))))
        self.base_press_keycode(4)

    # 点击我的
    def page_click_my(self):
        sleep(float("%.3f" % (random.uniform(2, 3))))
        # 点击返回的列表中下标为2的元素
        self.base_click(page.loc_my)

    # 点击我喜欢的音乐
    def page_click_music_of_my_like(self):
        sleep(float("%.3f" % (random.uniform(8, 9))))
        self.base_click(page.loc_music_of_my_like)

    # 查找刚添加的歌曲
    def page_slither_to_center(self, name):
        sleep(float("%.3f" % (random.uniform(2, 3))))
        # 列表中的第一首歌曲
        first_song_name = self.base_find_element(page.loc_first_song_name)
        # 刚添加的歌曲
        add_song_name = self.base_find_element((By.XPATH, f'//*[@text="{name}"]'))
        # print(name)
        # 捕获异常
        try:
            # 如果第一首歌曲的名字和刚添加的歌曲名字不相同，则滑动，直到刚添加的歌曲替换第一首歌曲位置
            if first_song_name.text != name:
                self.base_slither(first_song_name, add_song_name)
            # 截图
            self.base_screen_shot()
        # 打印错误信息
        except Exception as e:
            print(e)

    # 封装方法
    def page1(self, email, password, name):
        # 点击同意
        self.page_click_agree()
        # 点击允许（第一次）
        self.page_click_permit1()
        # 点击允许（第二次）
        self.page_click_permit2()
        # 点击其他登录方式
        self.page_click_another_login()
        # 点击网易邮箱图标
        self.page_click_wy_email()
        # 点击同意并继续
        self.page_click_agree_and_continue()
        # 输入邮箱
        self.page_input_email(email)
        # 输入密码
        self.page_input_password(password)
        # 点击登录
        self.page_click_login_button()
        # 点击搜索框按钮
        self.page_click_find_button()
        # 在顶部搜索框中输入歌曲名
        self.page_input_song_name(name)
        # 点击搜索
        self.page_click_find()
        # 点击第一条搜索记录
        self.page_click_first_record()
        # 添加到我喜欢
        self.page_click_add_like()
        # 跳转到我喜欢的音乐
        # self.page_jump_to_my_music()
        # 按下三次返回键
        self.page_press_keycode()
        self.page_press_keycode()
        self.page_press_keycode()
        # 点击我的
        self.page_click_my()
        # 点击我喜欢的音乐
        self.page_click_music_of_my_like()
        # 查找刚添加的歌曲
        self.page_slither_to_center(name)

