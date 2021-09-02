#coding:utf-8
#author:suner
#time:2021/9/1 16:16

import pytest
from selenium import webdriver
from testDatas import common_datas as CD
from common.do_log import MyLog

driver = None
# 声明他是一个fixture，作用于class
@pytest.fixture(scope="class")
def access_web():
    # 前置操作，所有用例都只需要打开一次浏览器
    global driver
    MyLog().info("==================测试登录功能开始啦：打开浏览器=================")
    driver = webdriver.Chrome()
    driver.get(CD.web_login_url)
    # yield是个关键字，前面的是前置条件，后面的后置条件
    # yield也相当于return，返回值
    yield driver
    # 后置操作  关闭浏览器
    MyLog().info("==================测试登录功能结束啦：关闭浏览器=================")
    driver.quit()

@pytest.fixture # 不传参默认scope=function，作用于方法
def refresh_page():
    global driver
    # 前置操作
    yield
    # 后置操作刷新浏览器，每条用例执行后刷新一次
    MyLog().info("==================这条测试用例执行结束啦：刷新一下浏览器=================")
    driver.refresh()




