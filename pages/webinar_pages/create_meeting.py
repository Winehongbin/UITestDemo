# -*- coding: utf-8 -*-

from pages.common_pages.base import BasePage
from pages.webinar_pages.index_page import Webinar_IndexPage
from pages.common_pages.login_page import LoginPage
from pages.common_pages.driver import brower
from pages.common_pages.choose_page import ChoosePage
import time



class Webinar_Create(BasePage):

    "创建线上会"
    def Create_Meeting(self):
        print "开始创建线上会",self.deprint()
        wrtitle = u'测试会议'
        self.wait_is_visible('x','/html/body/div[1]/div[2]/div/button')
        self.driver.implicitly_wait(20)
        self.element_value_input('x','//*[@id="title"]',wrtitle)
        #self.element_value_input('x', '//*[@id="title"]', u'测试会议')
        self.element_value_input('x', '//*[@id="sponser"]', u'校')
        self.element_click('x','//*[@id="webinarModal"]/div[1]/div/div[2]/div[2]/div[5]/div[1]/div/div/div/button')
        self.element_click('x','//*[@id="webinarModal"]/div[1]/div/div[2]/div[2]/div[5]/div[1]/div/div/div/ul/li[2]/a')
        #self.element_value_input('x','/html/body/p',u'会议简介信息')
        self.element_click('x','//*[@id="webinarModal"]/div[1]/div/div[2]/div[2]/div[8]/div[1]/div/div/div/button')
        self.element_click('x','//*[@id="webinarModal"]/div[1]/div/div[2]/div[2]/div[8]/div[1]/div/div/div/ul/li[2]/a')
        self.element_click('x','//*[@id="save"]')

        #保存会议后，加载时间太长
        time.sleep(10)
        self.wait_is_visible('x','//*[@id="webinarModal"]/div[1]/div/div[3]/a')


        #获取下一个窗口句柄，跳转到会议详情页面
        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.driver.implicitly_wait(10)
        self.find_element_text('x', '/html/body/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/strong[1]')
        time.sleep(5)
        vwrtitle =  self.find_element_text('x','/html/body/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/strong[1]')
        if wrtitle == vwrtitle:
            print self.deprint(), ":创建会议成功"
        else:
            print("创建会议失败")

if __name__ == '__main__':
    dr = brower()
    o = LoginPage(dr)
    o.login()
    o = ChoosePage(dr)
    time.sleep(3)
    o.click_menu_bt('8')
    o =  Webinar_IndexPage(dr)
    time.sleep(3)
    o.Index_Webinar()
    test = Webinar_Create(dr)
    test.Create_Meeting()


