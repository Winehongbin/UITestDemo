# -*- coding: utf-8 -*-
from selenium.common.exceptions import NoAlertPresentException

from pages.common_pages.base import BasePage
from pages.webinar_pages.index_page import Webinar_IndexPage
from pages.common_pages.login_page import LoginPage
from pages.common_pages.driver import brower
from pages.common_pages.choose_page import ChoosePage
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Webinar_Create(BasePage):

    "创建线上会"
    def create_meeting(self):
        self.deprint("开始创建线上会")
        titlet = self.nowtime()
        wrtitle = u'自动化创建测试会议' + str(titlet)
        #点击首页的创建会议按钮
        # self.wait_is_visible('x','/html/body/div[1]/div[2]/div/button')
        elementnew = WebDriverWait(self.driver,10,0.5).until(EC.presence_of_all_elements_located((By.XPATH,'/html/body/div[1]/div[2]/div/button')))
        if elementnew == 1 :
            self.wait_is_visible('x','/html/body/div[1]/div[2]/div/button')
        else:
            time.sleep(20)
            self.wait_is_visible('x', '/html/body/div[1]/div[2]/div/button')
        self.driver.implicitly_wait(20)
        #填写会议信息：会议标题
        self.element_value_input('x','//*[@id="title"]',wrtitle)
        # 主办方
        self.element_value_input('x', '//*[@id="sponser"]', u'校')
        #选择注册表单
        self.element_click('x','//*[@id="webinarModal"]/div[1]/div/div[2]/div[2]/div[5]/div[1]/div/div/div/button')
        self.element_click('x','//*[@id="webinarModal"]/div[1]/div/div[2]/div[2]/div[5]/div[1]/div/div/div/ul/li[2]/a')
        #self.element_value_input('x','/html/body/p',u'会议简介信息')
        #选择数据权限（下拉类型的字段）
        self.element_click('x','//*[@id="webinarModal"]/div[1]/div/div[2]/div[2]/div[8]/div[1]/div/div/div/button')
        self.element_click('x','//*[@id="webinarModal"]/div[1]/div/div[2]/div[2]/div[8]/div[1]/div/div/div/ul/li[2]/a')
        #点击保存按钮
        self.element_click('x','//*[@id="save"]')

        #保存会议后，判断去设置按钮是否显示，显示后，点击去设置
        element = WebDriverWait(self.driver,10,0.5).until(EC.presence_of_all_elements_located((By.XPATH,'//*[@id="webinarModal"]/div[1]/div/div[3]/a')))
        if element == 1 :
            self.wait_is_visible('x','//*[@id="webinarModal"]/div[1]/div/div[3]/a')
        else:
            time.sleep(20)
            self.wait_is_visible('x', '//*[@id="webinarModal"]/div[1]/div/div[3]/a')

        #获取下一个窗口句柄，跳转到会议详情页面
        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.driver.implicitly_wait(10)
        time.sleep(5)
        vwrtitle =  self.find_element_text('x','/html/body/div[1]/div[2]/div[2]/div/div[2]/div/ul/li[1]/span')
        # print vwrtitle
        # print wrtitle
        # try:
        #     vwrtitle = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div[2]/div/div[2]/div/ul/li[1]/span")))
        #     #
        #     self.driver.
        #
        # finally:
        #     self.driver.quit()
        #判断会议标题是否一致
        if wrtitle == vwrtitle:
            self.deprint("创建会议成功"),
        else:
            self.deprint("创建会议失败")

    #发布会议
    def publish_meeting(self):
        #点击发布按钮
        self.wait_is_visible('x','/html/body/div[1]/div[1]/div[1]/div[2]/div[1]/button[1]')
        time.sleep(5)
        self.wait_is_visible('x','//*[@id="systemDialog"]/div/div/div[3]/button[1]')
        time.sleep(5)
        vstatus = u'进入会场'
        vvstatus = self.find_element_text('x','/html/body/div[1]/div[1]/div[1]/div[2]/div[1]/a[3]')
        if vstatus == vvstatus :
            self.deprint("会议发布成功")
        else:
            self.deprint("会议发布失败")


    #取消会议
    def cancel_meeting(self):
        #获取会议标题
        wbrtitle = self.find_element_text('x','/html/body/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/strong[1]')
        #点击取消按钮
        self.wait_is_visible('x','/html/body/div[1]/div[2]/div[1]/div/button')
        #判断是否为未发布状态，只有未发布状态的会议，取消时，没有确认信息
        wbrstatus = self.find_element_text('x','/html/body/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/span[1]')
        if wbrstatus != u'未发布':
            time.sleep(2)
            self.wait_is_visible('x','//*[@id="alertModal"]/div/div/div[3]/button[1]')
        #点击直播回收站，查看是否存在取消的直播会议
        time.sleep(5)
        self.wait_is_visible('x','/html/body/div[1]/div[2]/div/div[2]/a')
        vwbrtitle = self.find_element_text('x','/html/body/div[1]/div[2]/div/div[1]/section/ul/li[1]/div/div[2]/p[1]/span[1]')
        wbrstatus = self.find_element_text('x','/html/body/div[1]/div[2]/div/div[1]/section/ul/li[1]/div/div[2]/p[1]/span[2]')
        vwbrstatus = u'已取消'
        if wbrtitle == vwbrtitle and wbrstatus == vwbrstatus :
        #if wbrtitle == vwbrtitle :
            self.deprint("取消会议成功")
        else:
            self.deprint("取消会议失败")

    # 还原会议
    def return_meeting(self):
        # 进入直播会议回收站
        self.wait_is_visible('x','/html/body/div[1]/div[2]/div/div[2]/a')
        time.sleep(3)
        # 点击还原按钮
        self.wait_is_visible('x','/html/body/div[1]/div[2]/div/div[1]/section/ul/li[1]/div/button')
        time.sleep(5)

if __name__ == '__main__':
    dr = brower()
    o = LoginPage(dr)
    o.login()
    o = ChoosePage(dr)
    time.sleep(3)
    o.click_menu_bt('8')
    o =  Webinar_IndexPage(dr)
    time.sleep(3)
    o.index_webinar()
    wbr = Webinar_Create(dr)
    wbr.create_meeting()
    # wbr.publish_meeting()
    wbr.cancel_meeting()



