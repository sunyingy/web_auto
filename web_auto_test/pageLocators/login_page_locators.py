#coding:utf-8
#author:suner
#time:2021/9/1 15:32
from selenium.webdriver.common.by import By

class LoginPageLocator:

    # 登录页面的用户名输入框loc
    username_loc = (By.XPATH, '//input[@id="account"]')
    # 登录页面的密码输入框loc
    pwd_loc = (By.XPATH, '//input[@name="password"]')
    # 登录页面的登录按钮loc
    login_button_loc = (By.XPATH, '//button[@id="submit"]')





