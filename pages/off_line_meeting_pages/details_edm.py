# -*- coding: utf-8 -*-

from pages.common_pages.base import BasePage
from pages.common_pages.login_page import LoginPage
from pages.common_pages.choose_page import ChoosePage
from pages.common_pages.driver import brower
from pages.off_line_meeting_pages.index_page import IndexPage
from pages.off_line_meeting_pages.new_meeting_page import NewMeetingPage
from pages.webinar_pages.index_page import Webinar_IndexPage
from pages.off_line_meeting_pages.index_details_meeting import IndexDetailsOfMeeting
from pages.off_line_meeting_pages.edm_offline import Edm_offline
import time
from pages.management_tools.mail_pages.tablelogin_page import TableLogin
import os

class Details_Edm(BasePage):


    def details_edm_count(self):
        self.driver.switch_to.window(self.driver.window_handles[3])  # 获取下一个窗口句柄，跳转到邮件任务详情页面
        num = self.find_element_text('x', '/html/body/div[1]/div[3]/div[1]/div[1]/ul/li[3]/div[1]/div[1]/a')  # 获取收件人总数
        # 对获取的收件人总数进行如下判断
        if int(num) == 1:
            self.deprint('线下会实例邮件任务执行成功')
            offlineedm = '线下会实例邮件任务执行成功'
        else:
            self.deprint('线下会实例邮件任务执行失败')
            offlineedm = '线下会实例邮件任务执行失败'
        return offlineedm

    # 点击导入收件人#20180809
    def export_edm(self):

        print u'uuuuu'
        self.driver.switch_to.window(self.driver.window_handles[-1])  # 获取下一个窗口句柄，跳转到邮件任务详情页面#20180809
        # self.wait_is_visible('x', '/html/body/div[3]/div[2]/div[2]/div[1]/div/span')
        self.wait_is_visible('x', '/html/body/div[1]/div[3]/div[1]/div[1]/ul/li[3]/div[2]/button')
        # self.wait_is_visible('x', '//*[@id="importAddressee"]/div/div/div[2]/div/div[1]/div/button')
        self.wait_is_visible('x', '//*[@id="importAddressee"]/div/div/div[2]/div/div[2]/div[2]/button')
        cur_path = os.path.abspath(os.path.dirname(__file__))
        time.sleep(3)
        os.system(cur_path + "/file/export.exe")
        self.deprint("收件人上传成功")
        # self.wait_is_visible('x', '//*[@id="importAddressee"]/div/div/div[3]/button')
        self.wait_is_visible('x', '//*[@id="importAddressee"]/div/div/div[3]/button')

        self.deprint("开始导入收件人")
        time.sleep(10)
        # self.driver.quit()

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

        e = Details_Edm(dr)
        e.details_edm_count()
