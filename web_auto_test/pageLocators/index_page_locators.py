#coding:utf-8
#author:suner
#time:2021/9/1 15:32

from selenium.webdriver.common.by import By

class IndexPageLocator:

    # 登录成功后首页“退出”loc
    logout_loc = (By.XPATH, '//a[text()="退出"]')

