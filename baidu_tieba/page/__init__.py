'''
    此页面用于存放部分配置信息
'''
# 导包
from selenium.webdriver.common.by import By

# 请求url
url = 'https://www.baidu.com'

# 贴吧入口
loc_forum = By.XPATH, '//*[@id="s-top-left"]/a[4]'

# 登录账户
loc_login = By.XPATH, '//*[@id="com_userbar"]/ul/li[4]/div/a'

# 使用用户名登录
loc_login_user = By.XPATH, '//*[@id="TANGRAM__PSP_4__footerULoginBtn"]'

# 手机号/用户名/邮箱输入框及输入内容
loc_login_username = By.XPATH, '//*[@id="TANGRAM__PSP_4__userName"]'

# 密码框及密码内容
loc_login_password = By.XPATH, '//*[@id="TANGRAM__PSP_4__password"]'

# 登录页面的登录按钮
loc_login_button = By.XPATH, '//*[@id="TANGRAM__PSP_4__submit"]'

# 用户名或密码错误提示
loc_login_password_error = By.XPATH, '//*[@id="TANGRAM__PSP_4__error"]/a'

# 体育类的NBA按钮
loc_sports_nba = By.XPATH, '//*[@id="f-d-w"]/div[2]/div/div[2]/a[3]'

# 湖人吧
loc_lakers = By.XPATH, '//*[@id="ba_list"]/div[3]/a/div/p[3]'

# 发帖页面
loc_publish_page = By.XPATH, '/html/body/ul/li[3]/a'

# 帖子标题
loc_publish_title = By.XPATH, '//*[@id="tb_rich_poster"]/div[3]/div[1]/div[2]/input'

# 帖子内容
loc_publish_text = By.XPATH, '//*[@id="ueditor_replace"]'

# 发表帖子
loc_publish_click = By.XPATH, '//*[@id="tb_rich_poster"]/div[3]/div[5]/div/button[1]'

# 发表结果
loc_publish_success = By.XPATH, '//*[@id="tb_rich_poster"]/div[3]/div[2]/div[4]/div[1]/div[1]'

# # 我的贴吧
# loc_my_tb = By.XPATH, '//*[@id="j_u_username"]/div[2]/div/div[1]/ul/li[1]/a'
#
# # 我的帖子
# loc_my_tz = By.XPATH, '//*[@id="ihome_nav_wrap"]/ul/li[5]/div/p/a'
#
# # 我的帖子标题
# loc_my_tz_title = By.XPATH, '//*[@id="content"]/div[3]/ul/li[1]/div[1]/table/tbody/tr/td[2]/a'


