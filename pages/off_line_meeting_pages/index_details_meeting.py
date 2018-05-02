# -*- coding: utf-8 -*-
from pages.common_pages.base import BasePage
from pages.common_pages.login_page import LoginPage
import time
from pages.common_pages.choose_page import ChoosePage
from pages.common_pages.driver import brower
from pages.off_line_meeting_pages.index_page import IndexPage
from pages.off_line_meeting_pages.interaction_manage_page import InteractionPage_Manage


class Index_DetailsOfMeeting(BasePage):


    # 点击互动环节菜单
    def click_interaction(self):
        print self.deprint(), ":点击互动环节菜单"
        # 点击创建会议
        # 获取下一个窗口句柄，跳转
        self.driver.switch_to.window(self.driver.window_handles[-1])
        # self.element_click('link', '互动环节')
        self.wait_is_visible('x','/html/body/div[2]/div[2]/ul[2]/li[6]')
        self.driver.implicitly_wait(30)
        print self.deprint(), "：进入互动环节页面"


if __name__ == '__main__':
    dr = brower()
    o = LoginPage(dr)
    o.login()
    o = ChoosePage(dr)
    o.click_menu_bt('9')
    o = IndexPage(dr)
    o.click_linelist()
    o = InteractionPage_Manage(dr)
    o.creat_questionnaire()
    o = Index_DetailsOfMeeting(dr)
    o.click_interaction()

