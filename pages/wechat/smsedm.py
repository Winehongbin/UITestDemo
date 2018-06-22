# -*- coding: utf-8 -*-
'''
Created on 2018-05-10
@author: 尤梅枝
'''
from pages.common_pages.base import BasePage
from pages.common_pages.login_page import LoginPage
import time
from pages.common_pages.choose_page import ChoosePage
from pages.common_pages.driver import brower

class Edm_Sms(BasePage):
    def createEdm(self,type):
        self.deprint("开始执行邮件任务创建用例")
        self.wait_is_visible('x','/html/body/div[3]/div[2]/div[1]/h2/div/button')
        self.element_value_input('x','//*[@id="createTask"]/div/div/div[2]/form/div[1]/div/div/input',u'自动化创建' + self.nowtime())
        self.element_value_input('x','//*[@id="createTask"]/div/div/div[2]/form/div[2]/div/div/input',u'自动化邮件标题')
        self.wait_is_visible('x','//*[@id="createTask"]/div/div/div[2]/form/div[3]/div/div/button')
        if type=="邀请函":
            self.wait_is_visible('x', '//*[@id="createTask"]/div/div/div[2]/form/div[3]/div/div/ul/li[2]/a')
        if type=="感谢函":
            self.wait_is_visible('x','//*[@id="createTask"]/div/div/div[2]/form/div[3]/div/div/ul/li[3]/a')
        if type=="通知函":
            self.wait_is_visible('x','//*[@id="createTask"]/div/div/div[2]/form/div[3]/div/div/ul/li[4]/a')
        if type=="报名确认函":
            self.wait_is_visible('x','//*[@id="createTask"]/div/div/div[2]/form/div[3]/div/div/ul/li[5]/a')
        if type=="审核通过通知函":
            self.wait_is_visible('x','//*[@id="createTask"]/div/div/div[2]/form/div[3]/div/div/ul/li[6]/a')
        time.sleep(3)
        self.driver.find_element_by_xpath('//*[@id="createTask"]/div/div/div[2]/form/div[5]/div/input').clear()
        self.element_value_input('x','//*[@id="createTask"]/div/div/div[2]/form/div[5]/div/input',u'自动化测试组')
        self.wait_is_visible('x','//*[@id="createTask"]/div/div/div[3]/button')
    def editEdm(self):
        self.deprint("开始执行邮件任务编辑用例")
        try:
            self.wait_is_visible('x','/html/body/div[3]/div[2]/div[3]/table/tbody/tr[2]/td[11]/a')
        except:
            self.wait_is_visible('x','/html/body/div[3]/div[2]/div[3]/table/tbody/tr[3]/td[11]/a')
        self.driver.switch_to.window(self.driver.window_handles[-1])  # 获取下一个窗口句柄，跳转到邮件任务详情页面
        self.deprint("窗口切换成功")
        self.wait_is_visible('x','/html/body/div[3]/div[2]/div[3]/div[2]/div/div[1]/a[2]')
        a=self.driver.switch_to.iframe('ueditor_0')
        a.find_element_by_class_name('view').send_keys('test')
        # self.element_value_input('class','view','test')



if __name__ == '__main__':
    dr = brower()
    o = LoginPage(dr)
    o.login()
    o = ChoosePage(dr)
    time.sleep(3)
    o.click_menu_bt('19')
    type="邀请函"
    S=Edm_Sms(dr)
    # S.createEdm(type)
    S.editEdm()


