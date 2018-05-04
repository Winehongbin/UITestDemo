# -*- coding: utf-8 -*-
from pages.common_pages.base import BasePage
from pages.common_pages.login_page import LoginPage
import time
from pages.common_pages.choose_page import ChoosePage
from pages.common_pages.driver import brower
from pages.off_line_meeting_pages.index_details_meeting import IndexDetailsOfMeeting
from pages.off_line_meeting_pages.interaction_manage_page import InteractionPage_Manage
from pages.off_line_meeting_pages.index_page import IndexPage


class  NewQuestionnairePage(BasePage):

    def creat_new_questionnaire(self):

        print self.deprint(), ":开始创建问卷"
        # 获取下一个窗口句柄，跳转
        self.driver.refresh()
        self.driver.switch_to.window(self.driver.window_handles[-1])
        # 填写问卷标题
        self.element_value_input('css','#questionaireTitle',u"问题一")
        # self.driver.find_element_by_css_selector("#questionaireTitle").send_keys(u"问题一") 20180428
        self.driver.implicitly_wait(30)
        # 点击开始时间
        self.driver.find_element_by_css_selector('#startTime').click()
        # 选择日期控件的时间，设置死
        # 下拉小时列表，给20点的固定值
        sel = self.driver.find_element_by_css_selector(
            'body > div:nth-child(6) > div.calendar.second.right.single > div.calendar-time > select.hourselect')
        self.Select(sel).select_by_value("0")
        self.driver.find_element_by_css_selector(
            'body > div:nth-child(6) > div.ranges > div > button.applyBtn.btn.btn-small.btn-sm.btn-info').click()
        self.driver.implicitly_wait(30)
        # 点击结束时间
        self.driver.find_element_by_css_selector('#endTime').click()
        # 下拉小时列表，给22点的固定值
        sel = self.driver.find_element_by_css_selector(
            'body > div:nth-child(7) > div.calendar.second.right.single > div.calendar-time > select.hourselect')
        self.Select(sel).select_by_value("23")
        self.driver.find_element_by_css_selector(
            'body > div:nth-child(7) > div.ranges > div > button.applyBtn.btn.btn-small.btn-sm.btn-info').click()
        self.driver.implicitly_wait(30)
        # 点击确定
        self.driver.find_element_by_css_selector(
            "body > div.g-container-box > div.m-container.ng-scope > div.m-form-btn.form-btn-border.ng-scope > a").click()

if __name__ == '__main__':
    dr = brower()
    o = LoginPage(dr)
    o.login()
    o = ChoosePage(dr)
    o.click_menu_bt('9')
    o = IndexPage(dr)
    o.click_linelist()
    o = IndexDetailsOfMeeting(dr)
    o.click_interaction()
    o = InteractionPage_Manage(dr)
    o.creat_questionnaire()
    o = NewQuestionnairePage(dr)
    o.creat_new_questionnaire()