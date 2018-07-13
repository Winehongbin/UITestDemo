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
        try:
            # self.driver.switch_to.window(self.driver.window_handles[-1])  不要加这句话，在进入问卷的时候一句切换过句柄，再次切换回导致按钮点击不了，应该是句柄不对了
            self.deprint("开始点击管理题库")
            time.sleep(3)
            self.wait_is_visible('x', '/html/body/div[1]/div[2]/main/div/div[1]/div/div[2]/div/div[1]/a')  # 点击管理题库的按钮
            self.deprint("点击管理题库按钮成功")
        except:
            try:
                # self.driver.switch_to.window(self.driver.window_handles[-1])  不要加这句话，在进入问卷的时候一句切换过句柄，再次切换回导致按钮点击不了，应该是句柄不对了
                self.deprint("开始点击管理题库")
                time.sleep(3)
                self.wait_is_visible('x', '/html/body/div[1]/div[2]/main/div/div[1]/div/div[2]/div/div[1]/a')  # 点击管理题库的按钮
                self.deprint("点击管理题库按钮成功")
            except:
                self.deprint("点击管理题库按钮失败")



    #打开新建问卷
    def open_create_questionnaire(self):
        # self.driver.switch_to.window(self.driver.window_handles[-1]) #不要加这句话，在进入问卷的时候一句切换过句柄，再次切换回导致按钮点击不了，应该是句柄不对了
        try:
            self.deprint("开始点击新建问卷")
            time.sleep(2)
            self.wait_is_visible('x', '/html/body/div[1]/div[2]/main/div/div[1]/div/div[2]/div/div[2]/a') #点击新建问卷的按钮
            self.deprint("点击新建问卷按钮成功")
        except:
            try:
                self.deprint("开始点击新建问卷")
                time.sleep(2)
                self.wait_is_visible('x', '/html/body/div[1]/div[2]/main/div/div[1]/div/div[2]/div/div[2]/a') #点击新建问卷的按钮
                self.deprint("点击新建问卷按钮成功")
            except:
                self.deprint("点击新建问卷按钮失败")




if __name__ == '__main__':
        self.driver = brower()
        object = LoginPage(self.driver)
        object.login()
        object = ChoosePage(self.driver)
        object.click_menu_bt('11')