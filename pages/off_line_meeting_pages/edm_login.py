# -*- coding: utf-8 -*-
from pages.common_pages.base import BasePage
from pages.common_pages.login_page import LoginPage
from pages.common_pages.choose_page import ChoosePage
from pages.common_pages.driver import brower
from pages.off_line_meeting_pages.index_page import IndexPage
from pages.off_line_meeting_pages.new_meeting_page import NewMeetingPage
from pages.management_tools.mail_pages.tablelogin_page import TableLogin
from pages.webinar_pages.index_page import Webinar_IndexPage
from pages.off_line_meeting_pages.index_details_meeting import IndexDetailsOfMeeting
import time
from pages.off_line_meeting_pages.edm_offline import Edm_offline


class Edm_Login(BasePage):


    def signupoffline(self):  # 登录成功后，进入表单报名页面，报名线下会#20180807
        time.sleep(5)
        self.deprint('进入pc预览默认表单报名页面')
        self.driver.find_element_by_xpath('//*[@id="body-box"]/form/div[5]/input').clear()  # 清空工号
        self.element_value_input('x', '//*[@id="body-box"]/form/div[5]/input', '69')  # 输入工号
        self.element_click('x', '//*[@id="body-box"]/form/input')  # 点击提交按钮
        time.sleep(2)
        self.deprint('线下会报名成功')
        self.driver.close()  # 关闭报名成功窗口

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
        o.click_indexname('11')
        e = Webinar_IndexPage(dr)
        e.login_newcustom()

        # S = Edm_offline(dr)
        # S.createofflineEdm()
        # S.startsigning()
        # o = TableLogin(dr)  #调用登录
        # o.create_login()#
        # # o = Edm_Login(dr)
        # # S.signupoffline()#



        #
