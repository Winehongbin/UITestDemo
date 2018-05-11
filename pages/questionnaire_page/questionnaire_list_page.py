# -*- coding: utf-8 -*-
from pages.common_pages.base import BasePage
from pages.common_pages.login_page import LoginPage
import time
from pages.common_pages.choose_page import ChoosePage
from pages.common_pages.driver import brower
class QuestionnaireListPage(BasePage):

    #打开管理题库
    def open_questionBank(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])  # 获取下一个窗口句柄，跳转
        self.deprint("点击管理题库")
        time.sleep(2)
        self.find_element_click('css','body > div.g-container-box > div.m-container.ng-scope > div.m-bar.ng-scope > div.pull-right > a.u-mr10')#点击管理题库的按钮


if __name__ == '__main__':
    pass