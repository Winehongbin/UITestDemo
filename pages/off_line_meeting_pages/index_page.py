# -*- coding: utf-8 -*-
from pages.common_pages.base import BasePage
from pages.common_pages.login_page import LoginPage
import time
from pages.common_pages.choose_page import ChoosePage
from pages.common_pages.driver import brower


class IndexPage(BasePage):


    # 点击创建会议
    def click_createunderline(self):
        print self.deprint(), ":点击创建会议"
        # 点击创建会议
        # 获取下一个窗口句柄，跳转
        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.driver.find_element_by_css_selector(
            "#g-right > div > div.clearfix.ng-scope > div.contact-stats-box.w715 > div.event-stats-l > div > button").click()
        self.driver.implicitly_wait(30)
        print self.deprint(), ":点击创建会议完成"

    #点击会议列表菜单按钮
    def click_linelist(self):
        time.sleep(5)
        print "进入第一场线下会：", self.deprint()
        #点击“会议列表”
        self.driver.find_element_by_xpath("/html/body/div[2]/div[1]/ul/li[2]/h2/a").click()
        self.driver.implicitly_wait(30)
        time.sleep(3)
        #点击会议列表页的首个“会议名称”
        self.driver.find_element_by_css_selector("#g-right > div > div.m-grid.grid-default.grid-event.grid-over.ng-scope > table > tbody > tr:nth-child(1) > td:nth-child(2) > a").click()
        self.driver.implicitly_wait(30)
        #获取下一个窗口句柄，跳转
        self.driver.switch_to.window(self.driver.window_handles[-1])

    #

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