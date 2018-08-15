# -*- coding: utf-8 -*-
import unittest
import os
import sys
curPath = os.path.abspath(os.path.dirname(__file__)) #os.path.basename(path):返回所给路径path的最底层路径名或者是文件名；
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
from pages.common_pages.login_page import LoginPage
from pages.common_pages.choose_page import ChoosePage
from pages.common_pages.driver import brower
from pages.wechat.smsedm import Edm_Sms
from common.common_function.mysql import DatabaseOperation
from pages.off_line_meeting_pages.details_edm import Details_Edm
from pages.off_line_meeting_pages.edm_offline import Edm_offline
from pages.management_tools.mail_pages.tablelogin_page import TableLogin
from pages.off_line_meeting_pages.index_page import IndexPage
from pages.off_line_meeting_pages.index_details_meeting import IndexDetailsOfMeeting
from pages.off_line_meeting_pages.new_meeting_page import NewMeetingPage
import time

class Edm_Test(unittest.TestCase):

    """邮件模块测试用例"""

    def setUp(self):
        self.driver= brower()
        login = LoginPage(self.driver)
        login.login()
        choose = ChoosePage(self.driver)
        choose.click_menu_bt('20')
        self.conn,self.cur=DatabaseOperation().openconnect()

    def tearDown(self):
        self.driver.quit()
        self.conn.close()
    # 创建图文素材用例
    def test_001_createEdmTask(self):

        """创建全局邮件任务"""
        # startTime=BasePage(self.driver).nowtime() #记录用例开始执行的时间
        # print "用例开始执行时间："+startTime
        test = Edm_Sms(self.driver)
        actual_result = test.createEdm("邀请函")
        expected_result = u'邮件创建成功'
        self.assertEqual(actual_result, expected_result, msg="failed")
        # object.quit()
        # base.deprint("创建线下会页面用例执行完成")
        # try:
        #     test.createEdm("邀请函")
        #     result='success'
        #
        # except:
        #     result='failed'

        # endTime = BasePage(self.driver).nowtime()  # 记录用例执行完成时间
        # insertSql = "INSERT into caselog VALUES ('创建邮件任务','邮件','%s','%s','%s')" % (startTime, endTime, result)
        # self.cur.execute(insertSql)
        # self.conn.commit()
    # def test_002_editEdm(self):
    #
    #     """编辑邮件任务并导入收件人"""
    #     startTime = BasePage(self.driver).nowtime()  # 记录用例开始执行的时间
    #     # print "用例开始执行时间："+startTime
    #     test = Edm_Sms(self.driver)
    #     try:
    #         test.editEdm()
    #         time.sleep(3)
    #         test.export()
    #         result = 'success'
    #     except:
    #         result = 'failed'
    #     endTime = BasePage(self.driver).nowtime()  # 记录用例执行完成时间
    #     insertSql = "INSERT into caselog VALUES ('编辑邮件内容并导入收件人','邮件','%s','%s','%s')" % (startTime, endTime, result)
    #     self.cur.execute(insertSql)
    #     self.conn.commit()
    def test_002_editEdm(self):
        """全局发送邮件"""
        #1、全局新建邮件任务---2、导入收件人---3、发送（测试邮件，任务管理中点击“立即发送”，启动发送按钮进行定时发送）---4、查看回执
        dr = brower()
        o = LoginPage(dr)
        o.login()
        o = ChoosePage(dr)
        time.sleep(3)
        o.click_menu_bt('20')
        type = "邀请函"
        S = Edm_Sms(dr)
        S.createEdm(type)
        S.list_edm()
        S.editMail()
        S.export()
        S.immeSendMail()
        S.viewReceipt()
        # e = Details_Edm(dr)
        # e.export_edm()

        # S.editEdm()
        # S.export()


    def test_003_offline_edm(self):

        """实例线下会邮件"""
        #实例线下会邮件---新建报名成功邮件任务---2、报名---3、查看邮件任务---4、查看回执
        dr = brower()
        o = LoginPage(dr)
        o.login()
        o = ChoosePage(dr)
        time.sleep(3)
        o.click_menu_bt('10')
        o = IndexPage(dr)  # 调用线下会的类
        o.click_createunderline()  # 调用线下会点击首页的创建会议按钮的方法
        o = NewMeetingPage(dr)  # 调用线下会的类
        o.create_neww_offline()  # 调用线下会创建会议的方法
        o = IndexDetailsOfMeeting(dr)
        o.click_indexname('4')
        S = Edm_offline(dr)
        S.createofflineEdm()
        S.startsigning()
        o = TableLogin(dr)  # 调用登录
        o.create_login()
        o.register_edm()
        s = Edm_offline(dr)
        s.viewofflineEdm()  # 查看邮件任务
        e = Details_Edm(dr)
        e.details_edm_count()
if __name__ == "__main__":
    suit=unittest.TestSuite()
    # suit.addTest(Edm_Test("test_001_createEdmTask"))
    suit.addTest(Edm_Test("test_002_editEdm"))
    suit.addTest(Edm_Test("test_003_offline_edm"))
    runner = unittest.TextTestRunner()
    runner.run(suit)
