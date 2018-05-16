# -*- coding: utf-8 -*-
from pages.common_pages.base import BasePage
import time
import os
import sys
from pages.common_pages.choose_page import ChoosePage
from pages.common_pages.driver import brower
curPath = os.path.abspath(os.path.dirname(__file__)) #os.path.basename(path):返回所给路径path的最底层路径名或者是文件名；
# #os.path.dirname(__file__):返回脚本的路径
rootPath = os.path.split(curPath)[0]  #os.path.split(curPath)[0]:path分割成目录
sys.path.append(rootPath)

class QuestionnaireListPage(BasePage):

    #打开管理题库
    def open_questionBank(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])  # 获取下一个窗口句柄，跳转
        self.deprint("点击管理题库")
        time.sleep(2)
        # self.find_element_click('css','body > div.g-container-box > div.m-container.ng-scope > div.m-bar.ng-scope > div.pull-right > a.u-mr10')#点击管理题库的按钮
        self.find_element_click('x','/html/body/div[1]/div[2]/div[2]/div[4]/a[1]')#点击管理题库的按钮

    #打开新建问卷
    def open_create_questionnaire(self):
        self.driver.switch_to.window(self.driver.window_handles[-1]) #获取下一个窗口句柄，跳转
        self.deprint("点击新建问卷")
        time.sleep(2)
        self.find_element_click('css','body > div.g-container-box > div.m-container.ng-scope > div.m-bar.ng-scope > div.pull-right > a.btn.r-btn.ng-scope') #点击新建问卷的按钮


if __name__ == '__main__':
    pass