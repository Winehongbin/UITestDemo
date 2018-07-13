# -*- coding: utf-8 -*-
from pages.common_pages.base import BasePage
from pages.common_pages.login_page import LoginPage
import time
from pages.common_pages.choose_page import ChoosePage
from pages.common_pages.driver import brower
from pages.questionnaire_page.questionnaire_list_page import QuestionnaireListPage
from pages.off_line_meeting_pages.index_details_meeting import IndexDetailsOfMeeting
# from pages.off_line_meeting_pages.interaction_manage_page import InteractionPage_Manage
from pages.off_line_meeting_pages.index_page import IndexPage


class  NewQuestionnairePage(BasePage):

    # 创建常规问卷
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
        # self.find_element_click('css','#startTime') # 点击开始时间
        # # 下拉小时列表，给20点的固定值
        # sel = self.driver.find_element_click('css','body > div:nth-child(6) > div.calendar.second.right.single > div.calendar-time > select.hourselect') #点击开始时间
        # self.Select(sel).select_by_value("0")
        # self.driver.find_element_click('css','body > div:nth-child(6) > div.ranges > div > button.applyBtn.btn.btn-small.btn-sm.btn-info')
        # self.driver.implicitly_wait(30)
        # self.driver.find_element_click('css','#endTime')  # 点击结束时间
        # self.driver.find_element_click('css','body > div:nth-child(7) > div.calendar.second.right.single > div.calendar-time > select.hourselect')  #下拉小时列表，给22点的固定值
        # self.Select(sel).select_by_value("23")
        # self.driver.find_element_click('css','body > div:nth-child(7) > div.ranges > div > button.applyBtn.btn.btn-small.btn-sm.btn-info')
        # self.driver.implicitly_wait(30)
        # self.driver.find_element_click('css','body > div.g-container-box > div.m-container.ng-scope > div.m-form-btn.form-btn-border.ng-scope > a')  # 点击结束时间
        # self.scrollbar('bottom')
        self.scrollbar('bottom')
        self.find_element_click('x','/html/body/div[1]/div[2]/main/div/div/div[2]/div/p/a')   #点击保存，进入编辑题目
        time.sleep(1)
        self.find_element_click('x','//*[@id="alertCommon"]/div/div/div[3]/button')  #点击确定按钮
        self.driver.implicitly_wait(30)

    #编辑问卷题目
    def edit_questionnaire_subject(self):
        try:
            self.deprint('编辑问卷题目')
            self.find_element_click('x', '//*[@id="left-menu"]/ul/li[1]/ul/li[1]/a')  # 点击用户信息一 中的姓名
            self.find_element_click('x', '/html/body/div[1]/div[2]/main/div/div/div[2]/div/div/div[2]/ng-form/p/input')  # 点击保存问卷
            time.sleep(1)
            self.find_element_click('x', '//*[@id="alertCommon"]/div/div/div[3]/button')  # 点击完成按钮
            time.sleep(1)
            self.find_element_click('x','/html/body/div[1]/div[2]/div[2]/div/div/div[3]/input')  #点击完成按钮
            self.driver.implicitly_wait(60)
            self.deprint('创建常规问卷完成')
        except:
            try:
                self.deprint('编辑问卷题目')
                self.find_element_click('x', '//*[@id="left-menu"]/ul/li[1]/ul/li[1]/a')  # 点击用户信息一 中的姓名
                self.find_element_click('x',
                                        '/html/body/div[1]/div[2]/main/div/div/div[2]/div/div/div[2]/ng-form/p/input')  # 点击保存问卷
                time.sleep(1)
                self.find_element_click('x', '//*[@id="alertCommon"]/div/div/div[3]/button')  # 点击完成按钮
                time.sleep(1)
                self.find_element_click('x', '/html/body/div[1]/div[2]/div[2]/div/div/div[3]/input')  # 点击完成按钮
                self.driver.implicitly_wait(60)
                self.deprint('创建常规问卷完成')
            except:
                self.deprint("用例执行失败")




if __name__ == '__main__':
    dr = brower()
    object = LoginPage(dr)
    object.login()
    object = ChoosePage(dr)
    object.click_menu_bt('11')
    object = QuestionnaireListPage(dr)
    object.open_create_questionnaire()
    object = NewQuestionnairePage(dr)
    object.creat_new_questionnaire()
    object.edit_questionnaire_subject()
