# -*- coding: utf-8 -*-
import time
from datetime import datetime
import unittest
import os
import sys
from datetime import datetime
curPath = os.path.abspath(os.path.dirname(__file__)) #os.path.basename(path):返回所给路径path的最底层路径名或者是文件名；
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
from pages.common_pages.login_page import LoginPage
import time
from pages.common_pages.choose_page import ChoosePage
from pages.common_pages.driver import brower
from pages.wechat.smsedm import Edm_Sms
from common.common_function.mysql import DatabaseOperation
from pages.common_pages.base import BasePage
class Edm_Test(unittest.TestCase):

    """邮件模块测试用例"""

    def setUp(self):
        self.driver= brower()
        login = LoginPage(self.driver)
        login.login()
        choose = ChoosePage(self.driver)
        choose.click_menu_bt('19')
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

if __name__ == "__main__":
    suit=unittest.TestSuite()
    suit.addTest(Edm_Test("test_001_createEdmTask"))
    suit.addTest(Edm_Test("test_002_editEdm"))
    runner = unittest.TextTestRunner()
    runner.run(suit)
