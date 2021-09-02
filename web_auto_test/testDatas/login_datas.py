#coding:utf-8
#author:suner
#time:2021/9/1 15:42

# 正常用例测试数据
login_valid_data = {"username": "admin", "pwd": "admin@123456"}

# 异常用例测试数据
login_invalid_datas = [
    {"username": "admin111", "pwd": "admin@123456", "exp": "登录失败"},
    {"username": "admin", "pwd": "", "exp": "登录失败"},
    {"username": "", "pwd": "admin@123456", "exp": "登录失败"},
    {"username": "admin", "pwd": "admin", "exp": "登录失败"}
]








