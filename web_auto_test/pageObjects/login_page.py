#coding:utf-8
#author:suner
#time:2021/9/1 15:37

# 页面对象继承basepage，直接使用basepage中的方法对元素操作

from common.basepage import BasePage
from pageLocators.login_page_locators import LoginPageLocator

class LoginPage(BasePage):

    # 登录操作
    def login(self, username, pwd):
        # 调用我们封装好的方法，输入用户名、密码，点击登录
        doc = "登录页面_登录功能"
        self.input_text(username, LoginPageLocator.username_loc, img_doc=doc)
        self.input_text(pwd, LoginPageLocator.pwd_loc, img_doc=doc)
        self.click_button(LoginPageLocator.login_button_loc, img_doc=doc)

    # 登录失败是否有弹框
    def login_failure_alert(self):
        doc = "登录页面_登录失败弹框"
        text = self.get_alert_text(img_doc=doc)
        if text:
            return text
        else:
            return False




