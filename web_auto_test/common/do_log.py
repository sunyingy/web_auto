#coding:utf-8
#author:suner
#time:2021/8/29 18:23
import logging
from common import dir_config

log_path = dir_config.log_path

class MyLog:

    """生成日志"""

    def my_log(self, msg, level):
        # 定义一个日志收集器 my_logger
        my_logger = logging.getLogger()

        # 设置级别
        my_logger.setLevel(level)

        # 创建一个我们自己输出的渠道
        fh = logging.FileHandler(log_path, encoding="utf-8")
        # fh.setLevel(level)
        formatter = logging.Formatter(
            "%(asctime)s %(filename)s %(funcName)s  %(module)s %(levelno)s %(levelname)s %(message)s")
        fh.setFormatter(formatter)
        # 两者对接
        my_logger.addHandler(fh)

        # 收集日志
        if level == "DEBUG":
            my_logger.debug(msg)
        elif level == "INFO":
            my_logger.info(msg)
        elif level == "WARNING":
            my_logger.warning(msg)
        elif level == "CRITICAL":
            my_logger.critical(msg)
        elif level == "ERROR":
            my_logger.error(msg)

        # 关闭渠道
        my_logger.removeHandler(fh)

    def debug(self, msg):
        self.my_log(msg, "DEBUG")

    def info(self, msg):
        self.my_log(msg, "INFO")

    def warning(self, msg):
        self.my_log(msg, "WARNING")

    def error(self, msg):
        self.my_log(msg, "ERROR")

    def critical(self, msg):
        self.my_log(msg, "CRITICAL")