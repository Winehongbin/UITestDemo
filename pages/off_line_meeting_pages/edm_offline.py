# -*- coding: utf-8 -*-

from pages.common_pages.base import BasePage
from pages.common_pages.login_page import LoginPage
from pages.common_pages.choose_page import ChoosePage
from pages.common_pages.driver import brower
from pages.off_line_meeting_pages.index_page import IndexPage
from pages.off_line_meeting_pages.new_meeting_page import NewMeetingPage
from pages.webinar_pages.index_page import Webinar_IndexPage
from pages.off_line_meeting_pages.index_details_meeting import IndexDetailsOfMeeting
# from pages.edm_pages.edm_global import Edm_Global
import time
from pages.management_tools.mail_pages.tablelogin_page import TableLogin
#线下会实例邮件用例：创建一场线下会--创建实例邮件任务--报名线下会--查看邮件任务


class Edm_offline(BasePage):


    # 创建线下会报名成功邮件任务
    def createofflineEdm(self):
        self.deprint('开始执行创建线下会实例邮件任务')
        time.sleep(5)
        self.element_click('x', '/html/body/div[2]/div[2]/ul[2]/li[4]/a/strong')  # 点击左侧的报名表单按钮
        self.element_click('x', '//*[@id="g-right"]/div/div[1]/div[2]/table/tbody/tr/td[9]/a[3]')  # 点击编辑图标
        self.deprint('打开编辑报名表单窗口')
        time.sleep(2)
        self.element_click('x', '//*[@id="newSignForm"]/div/div/div[2]/ul/li[2]/a')  # 点击消息通知标签
        time.sleep(2)
        self.wait_is_visible('x', '//*[@id="message-con"]/div[4]/div[2]/a[2]')  # 点击报名确认的创建新任务图标
        self.driver.switch_to.window(self.driver.window_handles[2])  # 获取下一个窗口句柄，跳转到邮件任务详情页面
        self.deprint('进入到邮件任务详情页面')
        time.sleep(6)
        text = self.find_element_text('x', '/html/body/div[1]/div[3]/div[1]/div[2]/div/div[2]/span')  # 拿到邮件分类名称
        if text == '审核通过通知函':
            self.deprint('线下会实例邮件创建成功')
        else:
            self.deprint('线下会实例邮件创建失败')
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[1])  # 获取上一个窗口句柄，跳转到报名名单页面
        self.deprint('进入到编辑报名表单窗口')
        time.sleep(1)
        self.element_click('x', '//*[@id="message-con"]/div[4]/div[2]/a[1]')  # 点击报名确认的刷新图标
        self.element_click('x', '//*[@id="message-con"]/div[4]/div[1]/div/button')  # 选择邮件任务
        self.element_click('x', '//*[@id="message-con"]/div[4]/div[1]/div/ul/li[2]/a')  # 选择刚才建的邮件任务
        self.element_click('x', '//*[@id="newSignForm"]/div/div/div[3]/button')  # 点击保存按钮
        self.deprint('线下会与实例邮件关联完成')

    # 将报名表单开启报名
    def startsigning(self):
        self.deprint('开始执行将报名表单开启报名')
        time.sleep(5)
        self.element_click('x', '//*[@id="g-right"]/div/div[1]/div[2]/table/tbody/tr/td[9]/a[4]')  # 点击报名表单的开始报名图标
        self.deprint('已开始进行报名')
        self.deprint('开始执行报名线下会')
        time.sleep(3)
        self.element_click('x', '//*[@id="g-right"]/div/div[1]/div[2]/table/tbody/tr/td[9]/a[1]')  # 点击报名表单的pc预览
        self.driver.switch_to.window(self.driver.window_handles[2])  # 跳转到登录页面

    # 报名会议后，查看邮件任务
    def viewofflineEdm(self):
        self.deprint('开始执行线下会查看邮件任务')
        time.sleep(3)
        self.driver.switch_to.window(self.driver.window_handles[1])#获取上一个窗口句柄，跳转到线下会会议页面
        self.scrollbar("200")
        time.sleep(3)
        self.element_click('x','/html/body/div[2]/div[2]/ul[2]/li[11]/a/strong')#点击左侧的邮件任务菜单
        self.driver.switch_to.window(self.driver.window_handles[2])  # 获取下一个窗口句柄，跳转到邮件管理页面
        time.sleep(2)
        self.deprint('进入到邮件管理页面')
        # 点击邮件任务列表的任务名称链接
        self.element_click('x','/html/body/div[1]/div[3]/div[1]/div[2]/div[2]/table/tbody/tr[1]/td[2]/a')



if __name__ == '__main__':
        dr = brower()
        o = LoginPage(dr)
        o.login()
        o = ChoosePage(dr)
        time.sleep(3)
        o.click_menu_bt('10')
        o = IndexPage(dr)#调用线下会的类
        o.click_createunderline()#调用线下会点击首页的创建会议按钮的方法
        o = NewMeetingPage(dr)#调用线下会的类
        o.create_neww_offline()#调用线下会创建会议的方法
        o = IndexDetailsOfMeeting(dr)
        o.click_indexname('4')
        # e = Webinar_IndexPage(dr)
        # e.login_newcustom()

        # a = Edm_Global(dr)
        # a.createEdm('邀请函')
        S = Edm_offline(dr)
        S.createofflineEdm()
        S.startsigning()


        o = TableLogin(dr)  #调用登录
        o.create_login()#
        o.register_edm()
        # o.signupoffline()  #

        s = Edm_offline(dr)
        s.viewofflineEdm()#查看邮件任务
