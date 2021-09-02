#coding:utf-8
#author:suner
#time:2021/9/1 10:14

import allure
import time
import datetime
from selenium import webdriver
from common.dir_config import *
from common.do_log import MyLog
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:

    """BasePage类，针对pageObjects类的二次封装"""
    def __init__(self, driver):
        self.driver = driver

    def wait_element_to_be_visible(self, loc, img_doc, timeout=20, frequency=0.5):
        """
        等待元素可见
        :param loc: 元素定位方式和定位元素的元组表达式
        :param img_doc: 截图说明
        :param timeout: 等待的超时时间
        :param frequency: 频率
        :return:
        """
        try:
            MyLog().info("开始等待页面元素<{0}>是否可见".format(loc))
            start_time = time.time()
            WebDriverWait(self.driver, timeout, frequency).until(EC.visibility_of_element_located(loc))
        except Exception as e:
            MyLog().error("页面元素<{}>等待可见失败".format(loc))
            self.save_screenshot(img_doc)
            raise e
        else:
            end_time = time.time()
            MyLog().info("页面元素<{}>等待可见，等待时间为：{}秒".format(loc, round(end_time-start_time, 2)))

    def wait_element_to_be_click(self, loc, img_doc, timeout=20, frequency=0.5):
        """
        等待元素可点击
        :param loc: 元素定位方式和定位元素的元组表达式
        :param img_doc: 截图说明
        :param timeout: 等待的超时时间
        :param frequency: 频率
        :return:
        """
        try:
            MyLog().info("开始等待页面元素<{0}>是否可见".format(loc))
            start_time = time.time()
            WebDriverWait(self.driver, timeout, frequency).until(EC.visibility_of_element_located(loc))
        except Exception as e:
            MyLog().error("页面元素<{}>等待可见失败".format(loc))
            self.save_screenshot(img_doc)
            raise e
        else:
            end_time = time.time()
            MyLog().info("页面元素<{}>等待可见，等待时间为：{}秒".format(loc, round(end_time-start_time, 2)))


    def wait_element_to_be_exist(self, loc, img_doc, timeout=20, frequency=0.5):
        """
        等待元素存在
        :param loc: 元素定位方式和定位元素的元组表达式
        :param img_doc: 截图说明
        :param timeout: 等待的超时时间
        :param frequency: 频率
        :return:
        """
        try:
            MyLog().info("开始等待页面元素<{0}>是否可见".format(loc))
            start_time = time.time()
            WebDriverWait(self.driver, timeout, frequency).until(EC.visibility_of_element_located(loc))
        except Exception as e:
            MyLog().error("页面元素<{}>等待可见失败".format(loc))
            self.save_screenshot(img_doc)
            raise e
        else:
            end_time = time.time()
            MyLog().info("页面元素<{}>等待可见，等待时间为：{}秒".format(loc, round(end_time-start_time, 2)))

    def save_screenshot(self, img_doc):
        """
        页面截屏保存截图
        :param img_doc:截图说明
        :return:
        """
        t = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())
        filename = screenshots_path + "\{0}_{1}.png".format(t, img_doc)
        MyLog().info("页面截图文件保存在：{}".format(filename))
        # print(filename)
        try:
            self.driver.save_screenshot(filename)
            # with open(filename, mode="rb") as f:
            #     file = f.read()
            # allure.attach(file, img_doc, allure.attachment_type.PNG)
            MyLog().info("页面截图文件保存在：{}".format(filename))
        except Exception as e:
            MyLog().error("截图失败")
            # raise e

    def get_element(self, loc, img_doc):
        """
        获取页面中的元素
        :param loc: 元素定位方式和定位元素的元组表达式
        :param img_doc: 截图说明
        :return:WebElement对象
        """
        MyLog().info("在{}中查找元素<{}>".format(img_doc, loc))
        try:
            ele = self.driver.find_element(*loc)
        except Exception as e:
            MyLog().error("在{}中查找元素<{}>失败".format(img_doc, loc))
            self.save_screenshot(img_doc)
            raise e
        else:
            return ele

    def get_elements(self, loc, img_doc):
        """
        获取页面中的所有元素
        :param loc: 元素定位方式和定位元素的元组表达式
        :param img_doc: 截图说明
        :return: WebElement对象（一组）
        """
        MyLog().info("在{}中查找所有元素<{}>".format(img_doc, loc))
        try:
            eles = self.driver.find_elements(*loc)
        except Exception as e:
            MyLog().error("在{}中查找所有元素<{}>失败".format(img_doc, loc))
            self.save_screenshot(img_doc)
            raise e
        else:
            return eles

    def input_text(self, text, loc, img_doc, timeout=20, frequency=0.5):
        """
        对输入框输入文本内容
        :param text: 输入的文本内容
        :param loc: 元素定位方式和定位元素的元组表达式
        :param img_doc: 截图说明
        :param timeout: 等待的超时时间
        :param frequency: 频率
        :return:
        """
        MyLog().info("在元素<{0}>中输入内容<{1}>".format(loc, text))
        try:
            self.wait_element_to_be_visible(loc, img_doc, timeout, frequency)
            self.get_element(loc, img_doc).send_keys(text)
        except Exception as e:
            MyLog().error("在元素<{0}>中输入内容<{1}>失败".format(loc, text))
            self.save_screenshot(img_doc)
            raise e

    def clear_text(self, loc, img_doc, timeout=20, frequency=0.5):
        """
        清除文本框的内容
        :param loc: 元素定位方式和定位元素的元组表达式
        :param img_doc: 截图说明
        :param timeout: 等待的超时时间
        :param frequency: 频率
        :return:
        """
        MyLog().info("在{}中清除元素<{}>的文本内容".format(img_doc, loc))
        try:
            self.wait_element_to_be_click(loc, img_doc, timeout, frequency)
            self.get_element(loc, img_doc).clear()
        except Exception as e:
            MyLog().error("在{}中清除元素<{}>的文本内容失败".format(img_doc, loc))
            self.save_screenshot(img_doc)
            raise e

    def click_button(self, loc, img_doc, timeout=20, frequency=0.5):
        """
        点击按钮
        :param loc: 元素定位方式和定位元素的元组表达式
        :param img_doc: 截图说明
        :param timeout: 等待的超时时间
        :param frequency: 频率
        :return:
        """
        MyLog().info("在{}中点击元素<{}>".format(img_doc, loc))
        try:
            self.wait_element_to_be_click(loc, img_doc, timeout, frequency)
            self.get_element(loc, img_doc).click()
        except Exception as e:
            MyLog().error("在{}中点击元素<{}>".format(img_doc, loc))
            self.save_screenshot(img_doc)
            raise e


    def get_element_text(self, loc, img_doc, timeout=20, frequency=0.5):
        """
        获取WebElement对象的文本值
        :param loc: 元素定位方式和定位元素的元组表达式
        :param img_doc: 截图说明
        :param timeout: 等待的超时时间
        :param frequency: 频率
        :return:WebElement对象的文本值
        """
        MyLog().info("在{}中获取元素<{}>的文本值".format(img_doc, loc))
        try:
            self.wait_element_to_be_visible(loc, img_doc, timeout, frequency)
            text = self.get_element(loc, img_doc).text
        except Exception as e:
            MyLog().error("在{}中获取元素<{}>的文本值".format(img_doc, loc))
            self.save_screenshot(img_doc)
            raise e
        else:
            MyLog().info("获取到的元素文本值为：{}".format(text))
            return text


    def get_elements_text(self, loc, img_doc, timeout=20, frequency=0.5):
        """
        获取WebElement对象的所有文本值【一组】
        :param loc: 元素定位方式和定位元素的元组表达式
        :param img_doc: 截图说明
        :param timeout: 等待的超时时间
        :param frequency: 频率
        :return: WebElement对象的文本值列表
        """
        MyLog().info("在{}中获取元素<{}>的所有文本值".format(img_doc, loc))
        try:
            self.wait_element_to_be_visible(loc, img_doc, timeout, frequency)
            eles = self.get_elements(loc, img_doc)
            text_list= []
            for ele in eles:
                text_list.append(ele.text)
        except Exception as e:
            MyLog().error("在{}中获取元素<{}>的所有文本值失败".format(img_doc, loc))
            self.save_screenshot(img_doc)
            raise e
        else:
            MyLog().info("获取到的元素文本值列表为：{}".format(text_list))
            return text_list

    def get_element_attr(self, attr_name, loc, img_doc, timeout=20, frequency=0.5):
        """
        获取WebElement对象的属性值
        :param attr_name: 属性名称
        :param loc: 元素定位方式和定位元素的元组表达式
        :param img_doc: 截图说明
        :param timeout: 等待的超时时间
        :param frequency: 频率
        :return: WebElement对象的属性值
        """
        MyLog().info("在{}中获取元素<{}>的{}属性值".format(img_doc, loc, attr_name))
        try:
            self.wait_element_to_be_exist(loc, img_doc, timeout, frequency)
            value = self.get_element(loc, img_doc).get_attribute(attr_name)
        except Exception as e:
            MyLog().error("在{}中获取元素<{}>的{}属性值失败".format(img_doc, loc, attr_name))
            self.save_screenshot(img_doc)
            raise e
        else:
            MyLog().info("获取到的元素{}属性值为{}".format(loc, value))
            return value

    def switch_to_frame(self, loc, img_doc, timeout=20, frequency=0.5):
        """
        切换iframe页面
        :param loc: 元素定位方式和定位元素的元组表达式
        :param img_doc: 截图说明
        :param timeout: 等待的超时时间
        :param frequency: 频率
        :return:
        """
        MyLog().info("在{}中根据元素<{}>进行iframe切换".format(img_doc, loc))
        try:
            WebDriverWait(self.driver, timeout, frequency).until(EC.frame_to_be_available_and_switch_to_it(loc))
        except Exception as e:
            MyLog().error("在{}中根据元素<{}>进行iframe切换失败".format(img_doc, loc))
            self.save_screenshot(img_doc)
            raise e


    def switch_to_default_content(self, img_doc):
        """
        切换iframe到main页面
        :param img_doc: 截图说明
        :return:
        """
        MyLog().info("切换iframe到main页面")
        try:
            self.driver.switch_to.default_content()
        except Exception as e:
            MyLog().error("切换iframe到main页面失败")
            self.save_screenshot(img_doc)
            raise e


    def switch_to_parent(self, img_doc):
        """
        切换iframe到上一层页面
        :param img_doc: 截图说明
        :return:
        """
        MyLog().info("切换iframe到上一层页面")
        try:
            self.driver.switch_to.parent_frame()
        except Exception as e:
            MyLog().error("切换iframe到上一层页面失败")
            self.save_screenshot(img_doc)
            raise e

    def switch_to_windows(self, loc, img_doc):
        """
        窗口切换
        :param loc: 元素定位方式和定位元素的元组表达式
        :param img_doc: 截图说明
        :return:
        """
        MyLog().info("在{}中根据元素<{}>进行窗口切换".format(img_doc, loc))
        all_handles = self.driver.window_handles
        try:
            self.driver.switch_to.window(all_handles[-1])
        except Exception as e:
            MyLog().error("在{}中根据元素<{}>进行窗口切换失败".format(img_doc, loc))


    def upload_file(self, filename, img_doc, browser_type="chrome"):
        """
        非input标签的文件上传
        :param filename: 文件名（绝对路径）
        :param img_doc: 截图说明
        :param browser_type: 浏览器类型
        :return:
        """
        pass

    def suspend_mouse(self, loc, img_doc, timeout=20, frequency=0.5):
        """
        鼠标悬浮
        :param loc: 元素定位方式和定位元素的元组表达式
        :param img_doc: 截图说明
        :param timeout: 等待的超时时间
        :param frequency: 频率
        :return:
        """
        MyLog().info("在{}上根据元素<{}>进行悬浮".format(img_doc, loc))
        try:
            self.wait_element_to_be_click(loc, img_doc, timeout, frequency)
            ele = self.get_element(loc, img_doc)
            ActionChains(self.driver).move_to_element(ele).perform()
        except Exception as e:
            MyLog().error("在{}上根据元素<{}>进行悬浮".format(img_doc, loc))
            self.save_screenshot(img_doc)
            raise e


    # def get_alert_text(self, img_doc, timeout=20, frequency=0.5):
    #     """
    #     获取alert、confirm弹框的文本值，并关闭弹框
    #     :param loc: 元素定位方式和定位元素的元组表达式
    #     :param img_doc: 截图说明
    #     :param timeout: 等待的超时时间
    #     :param frequency: 频率
    #     :return: alert弹框的文本值
    #     """
    #     MyLog().info("获取alert文本")
    #     try:
    #         WebDriverWait(self.driver, timeout, frequency).until(EC.alert_is_present)
    #         alert = self.driver.switch_to.alert
    #         alert_text = alert.text
    #         alert.accept()
    #     except Exception as e:
    #         MyLog().error("获取alert文本失败")
    #         self.save_screenshot(img_doc)
    #         raise e
    #     else:
    #         return alert_text

    def get_alert_text(self, img_doc, timeout=20, frequency=0.5):
        """
        获取alert、confirm弹框的文本值，并关闭弹框
        :param loc: 元素定位方式和定位元素的元组表达式
        :param img_doc: 截图说明
        :param timeout: 等待的超时时间
        :param frequency: 频率
        :return: alert弹框的文本值
        """
        MyLog().info("获取alert文本")
        try:
            alert = self.driver.switch_to.alert
            # alert_text = alert.text
            # alert.accept()
            return alert.text

        except Exception as e:
            MyLog().error("获取alert文本失败")
            self.save_screenshot(img_doc)
            raise e
        finally:
            alert.accept()


    def get_prompt_text(self, loc, img_doc, timeout=20, frequency=0.5):
        """
        获取prompt弹框的文本值，并关闭弹框
        :param loc: 元素定位方式和定位元素的元组表达式
        :param img_doc: 截图说明
        :param timeout: 等待的超时时间
        :param frequency: 频率
        :return: prompt弹框的文本值
        """

    def select_action_by_index(self, index, loc, img_doc, timeout=20, frequency=0.5):
        """
        Select操作，按索引值选择
        :param index_num: 输入索引值，从0开始
        :param loc: 元素定位方式和定位元素的元组表达式
        :param img_doc: 截图说明
        :param timeout: 等待的超时时间
        :param frequency: 频率
        :return:
        """
        MyLog().info("在{}上根据元素<{}>以index方式进行下拉选择".format(img_doc, loc))
        try:
            self.wait_element_to_be_click(loc, img_doc, timeout, frequency)
            ele = self.get_element(loc, img_doc)
            Select(ele).select_by_index(index)
        except Exception as e:
            MyLog().error("在{}上根据元素<{}>以index方式进行下拉选择失败".format(img_doc, loc))
            self.save_screenshot(img_doc)
            raise e

    def select_action_by_value(self, value, loc, img_doc, timeout=20, frequency=0.5):
        """
        Select操作，按value值选择
        :param value: 输入value值
        :param loc: 元素定位方式和定位元素的元组表达式
        :param img_doc: 截图说明
        :param timeout: 等待的超时时间
        :param frequency: 频率
        :return:
        """
        MyLog().info("在{}上根据元素<{}>以value方式进行下拉选择".format(img_doc, loc))
        try:
            self.wait_element_to_be_click(loc, img_doc, timeout, frequency)
            ele = self.get_element(loc, img_doc)
            Select(ele).select_by_value(value)
        except Exception as e:
            MyLog().error("在{}上根据元素<{}>以value方式进行下拉选择失败".format(img_doc, loc))
            self.save_screenshot(img_doc)
            raise e

    def select_action_by_content(self, content, loc, img_doc, timeout=20, frequency=0.5):
        """
        Select操作，按文本内容选择
        :param content:文本内容
        :param loc: 元素定位方式和定位元素的元组表达式
        :param img_doc: 截图说明
        :param timeout: 等待的超时时间
        :param frequency: 频率
        :return:
        """
        MyLog().info("在{}上根据元素<{}>以文本内容方式进行下拉选择".format(img_doc, loc))
        try:
            self.wait_element_to_be_click(loc, img_doc, timeout, frequency)
            ele = self.get_element(loc, img_doc)
            Select(ele).select_by_visible_text(content)
        except Exception as e:
            MyLog().error("在{}上根据元素<{}>以文本内容方式进行下拉选择失败".format(img_doc, loc))
            self.save_screenshot(img_doc)
            raise e








if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get("http://39.105.174.161/zentao/user-login.html")
    driver.find_element_by_xpath('//input[@id="account"]').send_keys("admin1")
    driver.find_element_by_xpath('//input[@name="password"]').send_keys("admin@123456")
    driver.find_element_by_xpath('//button[@id="submit"]').click()
    # driver.save_screenshot("sss.png")
    driver.save_screenshot(r".\sss.png")
