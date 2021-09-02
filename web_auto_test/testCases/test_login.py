#coding:utf-8
#author:suner
#time:2021/9/1 16:16

import allure
import pytest
from pageObjects.index_page import IndexPage
from pageObjects.login_page import LoginPage
from testDatas.login_datas import *

@allure.feature("测试登录功能")
@pytest.mark.usefixtures("access_web")
@pytest.mark.usefixtures("refresh_page")
class TestLogin:

    # 登录失败的用例 ，参数化获取用户名和密码
    @allure.story("异常登录测试")
    @pytest.mark.parametrize("invalid_datas", login_invalid_datas)
    def test_login_00_failure(self, invalid_datas, access_web):  # access_web是有返回值的fixture，这里直接当参数传入
        # 前置：浏览器已打开
        # 操作：调用登录方法，传入username、pwd
        LoginPage(access_web).login(invalid_datas["username"], invalid_datas["pwd"])
        # 断言：alert弹框存在
        assert LoginPage(access_web).login_failure_alert()

    @allure.story("正常登录测试")
    def test_login_01_success(self, access_web):
        # 前置：浏览器已打开
        # 操作：调用登录方法，传入username、pwd
        LoginPage(access_web).login(login_valid_data["username"], login_valid_data["pwd"])
        # 断言：调用首页“退出”存在
        assert IndexPage(access_web).isExist_exit_ele()

