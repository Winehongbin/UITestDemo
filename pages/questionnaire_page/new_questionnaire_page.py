# -*- coding: utf-8 -*-

import time
from datetime import datetime
from pages.common_pages.base import BasePage
from pages.common_pages.login_page import LoginPage
from pages.common_pages.choose_page import ChoosePage
from pages.common_pages.driver import brower
from pages.questionnaire_page.questionnaire_list_page import QuestionnaireListPage
from pages.off_line_meeting_pages.index_details_meeting import IndexDetailsOfMeeting
# from pages.off_line_meeting_pages.interaction_manage_page import InteractionPage_Manage
from pages.off_line_meeting_pages.index_page import IndexPage


class  NewQuestionnairePage(BasePage):

    # 创建常规问卷，并设置长期有效
    def creat_new_questionnaire(self):
        try:
            self.deprint('开始创建问卷')
            self.element_value_input('css', '#questionaireTitle', u"问题一")  # 填写问卷标题
            self.driver.implicitly_wait(30)
        except:
            try:
                self.deprint('开始创建问卷')
                self.element_value_input('css', '#questionaireTitle', u"问题一")  # 填写问卷标题
                self.driver.implicitly_wait(30)
            except:
                self.deprint("用例执行失败")
        self.scrollbar('bottom')
        self.find_element_click('x','/html/body/div[1]/div[2]/main/div/div/div[2]/div/p/a')   #点击保存，进入编辑题目
        time.sleep(1)
        self.find_element_click('x','//*[@id="alertCommon"]/div/div/div[3]/button')  #点击确定按钮
        self.driver.implicitly_wait(30)

    # 创建常规问卷，并设置有效时间
    def creat_new_questionnaire_with_time(self):
        try:
            self.deprint('开始创建问卷')
            self.element_value_input('css', '#questionaireTitle', u"问题一")  # 填写问卷标题
            self.driver.implicitly_wait(30)

            self.find_element_click('x',
                                    '/html/body/div[1]/div[2]/main/div/div/div[2]/div/div[7]/div/div[2]/label/ins')  # 点击开始时间
            self.find_element_click('x',
                                    '/html/body/div[1]/div[2]/main/div/div/div[2]/div/div[7]/div/div[3]/div/div/span')  # 点击设置日期的图标

            self.select_value('/html/body/div[5]/div[2]/div[2]/select[1]', '0')  # 设置开始时间的时
            self.select_value('/html/body/div[5]/div[2]/div[2]/select[2]', '0')  # 设置开始时间的分

            self.select_value('/html/body/div[5]/div[1]/div[2]/select[1]', '23')  # 设置结束时间的时
            self.select_value('/html/body/div[5]/div[1]/div[2]/select[2]', '59')  # 设置结束 时间的分

            self.find_element_click('x', '/html/body/div[5]/div[3]/div/button[1]')  # 点击确定按钮

            self.scrollbar('bottom')
            self.find_element_click('x', '/html/body/div[1]/div[2]/main/div/div/div[2]/div/p/a')  # 点击保存，进入编辑题目
            time.sleep(1)
            self.find_element_click('x', '//*[@id="alertCommon"]/div/div/div[3]/button')  # 点击确定按钮
            self.driver.implicitly_wait(30)
        except:
            try:
                self.deprint('开始创建问卷')
                self.element_value_input('css', '#questionaireTitle', u"问题一")  # 填写问卷标题
                self.driver.implicitly_wait(30)

                self.find_element_click('x',
                                        '/html/body/div[1]/div[2]/main/div/div/div[2]/div/div[7]/div/div[2]/label/ins')  # 点击开始时间
                self.find_element_click('x',
                                        '/html/body/div[1]/div[2]/main/div/div/div[2]/div/div[7]/div/div[3]/div/div/span')  # 点击设置日期的图标

                self.select_value('/html/body/div[5]/div[2]/div[2]/select[1]', '0')  # 设置开始时间的时
                self.select_value('/html/body/div[5]/div[2]/div[2]/select[2]', '0')  # 设置开始时间的分

                self.select_value('/html/body/div[5]/div[1]/div[2]/select[1]', '23')  # 设置结束时间的时
                self.select_value('/html/body/div[5]/div[1]/div[2]/select[2]', '59')  # 设置结束 时间的分

                self.find_element_click('x', '/html/body/div[5]/div[3]/div/button[1]')  # 点击确定按钮

                self.scrollbar('bottom')
                self.find_element_click('x', '/html/body/div[1]/div[2]/main/div/div/div[2]/div/p/a')  # 点击保存，进入编辑题目
                time.sleep(1)
                self.find_element_click('x', '//*[@id="alertCommon"]/div/div/div[3]/button')  # 点击确定按钮
                self.driver.implicitly_wait(30)
            except:
                self.deprint("用例执行失败")


    #编辑问卷题目
    def edit_questionnaire_subject(self):
        text=""
        try:
            self.deprint('编辑问卷题目')
            time.sleep(6)
            self.wait_is_visible('x', '//*[@id="left-menu"]/ul/li[1]/ul/li[1]/a')  # 点击用户信息一 中的姓名
            self.find_element_click('x', '/html/body/div[1]/div[2]/main/div/div/div[2]/div/div/div[2]/ng-form/p/input')  # 点击保存问卷
            time.sleep(1)
            self.find_element_click('x', '//*[@id="alertCommon"]/div/div/div[3]/button')  # 点击完成按钮
            time.sleep(1)
            self.find_element_click('x','/html/body/div[1]/div[2]/div[2]/div/div/div[3]/input')  #点击完成按钮
            self.driver.implicitly_wait(60)
            self.deprint('创建常规问卷完成')
            text="创建常规问卷完成"
        except:
            try:
                self.deprint('编辑问卷题目')
                time.sleep(6)
                self.wait_is_visible('x', '//*[@id="left-menu"]/ul/li[1]/ul/li[1]/a')  # 点击用户信息一 中的姓名
                self.find_element_click('x',
                                        '/html/body/div[1]/div[2]/main/div/div/div[2]/div/div/div[2]/ng-form/p/input')  # 点击保存问卷
                time.sleep(1)
                self.find_element_click('x', '//*[@id="alertCommon"]/div/div/div[3]/button')  # 点击完成按钮
                time.sleep(1)
                self.find_element_click('x', '/html/body/div[1]/div[2]/div[2]/div/div/div[3]/input')  # 点击完成按钮
                self.driver.implicitly_wait(60)
                self.deprint('创建常规问卷完成')
                text="创建常规问卷完成"
            except:
                self.deprint("用例执行失败")
                text="用例执行失败"
        finally:
                return text





if __name__ == '__main__':
    dr = brower()
    object = LoginPage(dr)
    object.login()
    object = ChoosePage(dr)
    object.click_menu_bt('11')
    object = QuestionnaireListPage(dr)
    object.open_create_questionnaire()
    object = NewQuestionnairePage(dr)
    object.creat_new_questionnaire_with_time()
    object.edit_questionnaire_subject()
