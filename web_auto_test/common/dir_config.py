#coding:utf-8
#author:suner
#time:2021/9/1 12:00

"""专门来读取路径的值"""

import os
import time
now = time.strftime("%Y_%m_%d_%H_%M_%S")


project_path = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]

# 存储日志文件的路径
log_path = os.path.join(project_path, "outPuts", "logs", now+"test_web_log.txt")
print(log_path)

# 存储截图文件的路径
screenshots_path = os.path.join(project_path, "outPuts", "screenshots")
print(screenshots_path)


# 存放测试报告的路径
report_path = os.path.join(project_path, "outPuts", "report")