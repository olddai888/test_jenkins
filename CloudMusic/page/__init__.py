# 此页面用于存放部分配置信息
from selenium.webdriver.common.by import By

desired_caps = {
    # 操作系统名称
    'platformName': 'Android',

    # 操作系统版本
    'platformVersion': '7.1.2',

    # 设备名称（随意）
    'deviceName': 'android 7.1.2',

    # 要打开的应用程序的包名
    'appPackage': 'com.netease.cloudmusic',

    # 要打开的界面
    'appActivity': '.activity.LoadingActivity',

    # 设置支持中文的输入格式
    'unicodeKeyboard': True,

    'resetKeyboard': True,

    # 保持登录状态
    # 'noReset': True

}

# 同意按钮（授权页面）
loc_agree = By.XPATH, '//*[@text="同意"]'

# 允许按钮（第一次）
loc_permit1 = By.XPATH, '//*[@text="允许"]'

# 允许按钮（第二次）
loc_permit2 = By.XPATH, '//*[@text="允许"]'

# 其他登录方式按钮
loc_another_login = By.XPATH, '//*[@text="其他登录方式"]'

# 网易邮箱登录选项
loc_login_wy_email = By.ID, 'com.netease.cloudmusic:id/mail'

# 同意并继续按钮
loc_agree_and_continue = By.XPATH, '//*[@text="同意并继续"]'

# 邮箱输入框
loc_email = By.ID, 'com.netease.cloudmusic:id/email'

# 密码输入框
loc_password = By.ID, 'com.netease.cloudmusic:id/password'

# 登录按钮
loc_login_button = By.XPATH, '//*[@text="登录"]'

# 搜索框
loc_find_song = By.ID, 'com.netease.cloudmusic:id/searchBar'

# 聚焦后的搜索框
loc_find_song_after = By.ID, 'com.netease.cloudmusic:id/search_src_text'

# 搜索按钮
loc_find_button = By.ID, 'com.netease.cloudmusic:id/toSearch'

# 播放全部
loc_broadcast_all = By.XPATH, '//*[@text="播放全部"]'

# 添加到我喜欢
loc_add_like = By.ID, 'com.netease.cloudmusic:id/likeBtn'

# ‘我的’按钮
# loc_my = By.ID, 'com.netease.cloudmusic:id/icon'
loc_my = By.XPATH, '//*[@text="我的"]'

# 我喜欢的音乐
loc_music_of_my_like = By.ID, 'com.netease.cloudmusic:id/name'

# 目标曲目
# loc_check_song = By.XPATH, '//*[@text="素颜"]'

# 我喜欢的音乐
# 包名
loc_like_package = 'com.netease.cloudmusic'
# 界面名
loc_like_activity = '.activity.PlayListActivity'

# 我喜欢的音乐第一首歌名字
loc_first_song_name = By.ID, 'com.netease.cloudmusic:id/songName'

# 长按时长
loc_long_press_time = 2134
