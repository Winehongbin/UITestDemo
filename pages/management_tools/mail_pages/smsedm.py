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
import os
from pages.off_line_meeting_pages.details_edm import Details_Edm

class Edm_Sms(BasePage):

    def createEdm(self,type):
        self.deprint("开始执行邮件任务创建用例")
        self.wait_is_visible('x','/html/body/div[1]/div[3]/div[1]/div[2]/div[1]/div[2]/button') #点击新建任务
        self.element_value_input('x','//*[@id="createTask"]/div/div/div[2]/form/div/div[1]/div/input',u'自动化创建' + self.nowtime())#输入任务名称
        self.element_value_input('x','//*[@id="createTask"]/div/div/div[2]/form/div/div[2]/div/input',u'自动化邮件标题')#输入邮件标题
        self.wait_is_visible('x','//*[@id="createTask"]/div/div/div[2]/form/div/div[3]/div/div/button/span[2]')#点击任务分类
        if type=="邀请函":
            self.wait_is_visible('x', '//*[@id="createTask"]/div/div/div[2]/form/div/div[3]/div/div/ul/li[2]')
        if type=="感谢函":
            self.wait_is_visible('x','//*[@id="createTask"]/div/div/div[2]/form/div/div[3]/div/div/ul/li[3]')
        if type=="通知函":
            self.wait_is_visible('x','//*[@id="createTask"]/div/div/div[2]/form/div/div[3]/div/div/ul/li[4]')
        if type=="报名确认函":
            self.wait_is_visible('x','//*[@id="createTask"]/div/div/div[2]/form/div/div[3]/div/div/ul/li[5]')
        if type=="审核通过通知函":
            self.wait_is_visible('x','//*[@id="createTask"]/div/div/div[2]/form/div/div[3]/div/div/ul/li[6]')
        time.sleep(3)
        self.driver.find_element_by_xpath('//*[@id="createTask"]/div/div/div[2]/form/div/div[5]/div/input').clear()#清空发件人显示名称
        self.element_value_input('x','//*[@id="createTask"]/div/div/div[2]/form/div/div[5]/div/input',u'自动化测试组')#填写发件人显示名称
        try:
            self.wait_is_visible('x', '//*[@id="createTask"]/div/div/div[3]/button[2]')  # 点击确定按钮
            return u'邮件创建成功'
        except:
            return u'邮件创建失败'

    def list_edm(self):#20180809
        time.sleep(3)
        self.driver.switch_to.window(self.driver.window_handles[-1])  # 获取下一个窗口句柄，跳转到邮件任务详情页面#20180809
        self.wait_is_visible('x','/html/body/div[1]/div[3]/div[1]/div[2]/div[2]/table/tbody/tr[1]/td[2]/a') #点击第一个邮件任务#20180809

    #编辑邮件#20180809
    def editEdm(self):
        self.deprint("开始执行邮件任务编辑用例")
        self.element_value_input('x','/html/body/div[3]/div[2]/div[2]/div[4]/input',u'自动化创建')
        self.wait_is_visible('x','/html/body/div[3]/div[2]/div[2]/button') #搜索自动化创建的邮件任务进行编辑
        for n in range(2,5):
            xpath='/html/body/div[3]/div[2]/div[3]/table/tbody/tr['+str(n)+']/td[10]'
            # print xpath
            test=self.find_element_text('x',xpath)
            if test==u'正常':
                xpath2='/html/body/div[3]/div[2]/div[3]/table/tbody/tr['+str(n)+']/td[11]/a'
                self.wait_is_visible('x',xpath2)
                break
            else:
                continue
        self.driver.switch_to.window(self.driver.window_handles[-1])  # 获取下一个窗口句柄，跳转到邮件任务详情页面
        self.deprint("窗口切换成功")
        self.wait_is_visible('x','/html/body/div[3]/div[2]/div[3]/div[2]/div/div[1]/a[2]')
        time.sleep(1)
        iframe=self.driver.find_element_by_xpath('//*[@id="ueditor_0"]')
        self.driver.switch_to.frame(iframe) #切换iframe到邮件内容输入窗口
        self.deprint("iframe切换成功")
        self.wait_is_visible('x','/html/body')
        self.element_value_input('x','/html/body',u'自动化测试编辑的内容') #输入邮件内容
        self.driver.switch_to.default_content() #从邮件内容输入的iframe窗口切换回主文档
        self.deprint("从iframe切回主文档成功")
        self.scrollbar("bottom")
        self.wait_is_visible('x','/html/body/div[3]/div[2]/div[2]/form/div[6]/div/button') #点击保存按钮

    # 点击导入收件人#20180809
    def export(self):
        time.sleep(5)
        self.driver.switch_to.window(self.driver.window_handles[-1])  # 获取下一个窗口句柄，跳转到邮件任务详情页面#20180809
        self.wait_is_visible('x', '/html/body/div[1]/div[3]/div[1]/div[1]/ul/li[3]/div[2]/button')
        self.wait_is_visible('x', '//*[@id="importAddressee"]/div/div/div[2]/div/div[2]/div[2]/button')
        cur_path = os.path.abspath(os.path.dirname(__file__)) + "\\file\export.exe"
        zh_path = eval(repr(cur_path).replace('\\', '\\\\'))
        time.sleep(2)
        os.system(zh_path)
        self.deprint("收件人上传成功")
        self.wait_is_visible('x', '//*[@id="importAddressee"]/div/div/div[3]/button')
        time.sleep(2)
        self.deprint("开始导入收件人")
        time.sleep(10)
        # self.driver.quit()

    def editMail(self):
        self.deprint("开始执行邮件任务编辑用例")
        time.sleep(3)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.wait_is_visible('x',
                             '/html/body/div[1]/div[3]/div[1]/div[2]/div/div[7]/div[1]/div[2]/ul/li[3]/a')  # 点击编辑按钮
        self.deprint("点击编辑按钮成功")
        iframe = self.driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[8]/iframe")
        self.driver.switch_to_frame(iframe)
        ifr = self.driver.find_element_by_xpath('//*[@id="ueditor_0"]')
        self.driver.switch_to.frame(ifr)  # 切换iframe到邮件内容输入窗口
        self.deprint("iframe切换成功")
        self.wait_is_visible('x', '/html/body')
        self.element_value_input('x', '/html/body', u'自动化测试编辑的内容')  # 输入邮件内容
        self.driver.switch_to.parent_frame()  # 从邮件内容输入的iframe窗口切换回主文档
        self.deprint("从iframe切回主文档成功")
        self.scrollbar("bottom")
        self.wait_is_visible('x', '/html/body/div[1]/div[1]/form/div[7]/div/input')  # 点击保存按钮

    def immeSendMail(self):
        time.sleep(5)
        self.driver.switch_to.window(self.driver.window_handles[-1])  # 获取下一个窗口句柄，跳转到邮件任务详情页面#20180809
        self.wait_is_visible('x', '/html/body/div[1]/div[3]/div[1]/div[2]/div/div[1]/div[2]/span[3]')  # 进入发送任务管理
        self.deprint("进入发送任务管理")
        time.sleep(7)
        iframe = self.driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[8]/iframe")
        self.driver.switch_to_frame(iframe)
        self.wait_is_visible('x', '/html/body/div[1]/section/div/div[1]/div[2]/button[2]')  # 点击启动发送按钮]
        self.deprint("启动发送")
        self.wait_is_visible('x', '//*[@id="TaskSend"]/div/div/div[2]/div[2]/label/ins')  # 选中立即执行发送按钮
        self.wait_is_visible('x', '//*[@id="TaskSend"]/div/div/div[3]/button[2]')  # 点击确定按钮
        time.sleep(5)
        self.wait_is_visible('x', '//*[@id="alertCommon"]/div/div/div[3]/button')  # 点击确定按钮





if __name__ == '__main__':
    dr = brower()
    o = LoginPage(dr)
    o.login()
    o = ChoosePage(dr)
    time.sleep(3)
    o.click_menu_bt('20')
    type="邀请函"
    S=Edm_Sms(dr)
    S.createEdm(type)
    S.list_edm()
    e = Details_Edm(dr)
    e.export_edm()

    # S.editEdm()
    # S.export()


