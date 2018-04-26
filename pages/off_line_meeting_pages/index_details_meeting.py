# -*- coding: utf-8 -*-
from pages.common_pages.base import BasePage
from pages.common_pages.login_page import LoginPage
import time
from pages.common_pages.choose_page import ChoosePage
from pages.common_pages.driver import brower


class Index_DetailsOfMeeting(BasePage):


    # 点击互动环节菜单
    def click_interaction(self):
        print self.deprint(), ":点击互动环节菜单"
        # 点击创建会议
        # 获取下一个窗口句柄，跳转
        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.element_click('css','driver.find_element_by_css_selector("body > div.g-container > div.g-left.s-left > ul.m-nav-ul.nav-event.ng-scope > li:nth-child(6) > a > strong')
        #
        # self.driver.find_element_by_css_selector(
        #     "#g-right > div > div.clearfix.ng-scope > div.contact-stats-box.w715 > div.event-stats-l > div > button").click()
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
    # o.click_createunderline()
    # o.quit()