# -*- coding: utf-8 -*-
from pages.common_pages.base import BasePage
from pages.common_pages.login_page import LoginPage
import time
from pages.common_pages.choose_page import ChoosePage
from pages.common_pages.driver import brower


class IndexPage(BasePage):


    # 点击创建会议
    def click_createunderline(self):
        self.wait_is_visible('css','body > div.g-container.ng-scope > div.g-left.s-left > ul > li.ng-scope.has-page.active > h2 > a')
        self.deprint("点击创建会议")
        self.driver.switch_to.window(self.driver.window_handles[-1])   # 获取下一个窗口句柄，跳转
        self.wait_is_visible('css','#g-right > div > div.clearfix.ng-scope > div.contact-stats-box.w715 > div.event-stats-l > div > button') #点击创建会议
        self.driver.implicitly_wait(30)
        self.deprint("点击创建会议完成")

    #点击会议列表菜单
    def click_linelist(self,list_pos):
        self.deprint("点击会议列表")
        self.driver.implicitly_wait(10)
        css_path = "/html/body/div[2]/div[1]/ul/li[" + str(list_pos) + "]/h2/a"   #点击会议列表
        self.wait_is_visible('x', css_path)
        self.driver.refresh()
        self.deprint("点击第一场会议")
        self.driver.implicitly_wait(30)
        self.wait_is_visible('x','//*[@id="g-right"]/div/div[3]/table/tbody/tr[1]/td[2]/a')  #点击第一场会议
        self.driver.implicitly_wait(30)


if __name__ == '__main__':
    dr = brower()
    o = LoginPage(dr)
    o.login()

    o = ChoosePage(dr)
    time.sleep(3)
    o.click_menu_bt('9')

    o = IndexPage(dr)
    #o.click_linelist()
    o.click_linelist('2')
    o.quit()