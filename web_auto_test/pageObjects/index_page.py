#coding:utf-8
#author:suner
#time:2021/9/1 15:38

from pageLocators.index_page_locators import IndexPageLocator
from common.basepage import BasePage

class IndexPage(BasePage):

    # 用于登录成功后退出按钮校验
    def isExist_exit_ele(self):
        doc = "首页_退出"
        try:
            self.wait_element_to_be_visible(IndexPageLocator.logout_loc, img_doc=doc)
            return True
        except:
            return False



