# 定义切换到当前窗口的方法
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


def base_switch_window():
    driver = webdriver.Chrome()
    driver.get('http://www.baidu.com')
    driver.implicitly_wait(30)
    driver.find_element(By.XPATH, '//*[@id="s-top-left"]/a[4]').click()
    # 获取当前窗口句柄
    handle = driver.current_window_handle
    # 获取所有窗口句柄
    handles = driver.window_handles
    for h in handles:
        if h != handle:
            # 利用句柄将焦点切换到当前窗口
            driver.switch_to_window(h)
    driver.find_element(By.XPATH, '//*[@id="com_userbar"]/ul/li[4]/div/a').click()
    # driver.close(handle)
    sleep(5)
    driver.quit()


base_switch_window()
