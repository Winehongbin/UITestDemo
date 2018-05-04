# -*- coding: utf-8 -*-
"""
os模块就是对操作系统进行操作，比如取文件的路径。

sys模块提供了一系列有关Python运行环境的变量和函数,例如：
#生成报告是报错，编码错误。python2.7默认使用ascii，设置成utf-8，python2.7以后不用setdefaultencoding了
   reload(sys)
  sys.setdefaultencoding('utf8')
"""
import sys

from pages.common_pages.driver import brower

reload(sys)  #在解释器里修改的编码只能保证当次有效，在重启解释器后，会发现，编码又被重置为默认的ascii了
sys.setdefaultencoding('utf8')
import os
curPath = os.path.abspath(os.path.dirname(__file__))
print os.path.dirname(__file__)
print curPath
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
from pages.off_line_meeting_pages.interaction_link_page import Interaction_Line
import time
from datetime import datetime
import unittest
from test_case.base_unit import BaseUnit
from common.report import report
from pages.common_pages.login_page import LoginPage
from pages.common_pages.choose_page import ChoosePage
from pages.off_line_meeting_pages.index_page import IndexPage
from common.mail import email_oper
from pages.off_line_meeting_pages.new_meeting_page import NewMeetingPage


class Offline_Meeting_Test(BaseUnit):

    """线下会测试用例"""

    # 登录，并进入线下会页面测试用例
    def test_001_loginoffline(self):
        #下面一句的文字，是通过Python的一种注释doc string，用于函数、类和方法的描述，HTMLTestRunner可以读取此类型注释
        """ 测试进入线下会 """

        print "开始执行登录，并进入线下会用例：", self.noww()
        dr = brower()
        object = LoginPage(dr)
        object.login()
        object = ChoosePage(dr)
        object.click_menu_bt('9')
        object = IndexPage(dr)
        object.click_linelist()
        object.quit()
        print "进入线下会页面用例执行完成：", self.noww()

    def test_002_createoffline(self):
        """ 测试创建线下会 """

        print "开始执行登录，并进入线下会用例：", self.noww()
        dr = brower()
        object = LoginPage(dr)
        object.login()
        object = ChoosePage(dr)
        object.click_menu_bt('9')
        object = IndexPage(dr)
        object.click_createunderline()
        object = NewMeetingPage(dr)
        object.create_neww_offline()
        print "进入线下会页面用例执行完成：", self.noww()


    def test_003_interaction(self):
        """ 添加互动环节"""

        print "开始执行登录，并进入线下会用例：", self.noww()
        dr = brower()
        o = LoginPage(dr)
        o.login()
        o = ChoosePage(dr)
        o.click_menu_bt('9')
        o = IndexPage(dr)
        o.click_linelist()
        o = Interaction_Line(dr)
        o.interaction_link()
        print "进入线下会页面用例执行完成：", self.noww()





    """
     # 管理线下会
    def test_002_manageoffline(self):
         print "开始执行添加线下会问卷用例"

         print "添加线下会问卷用例执行完毕"
    def test_003_offline(self):
        print self.noww(),":开始执行添加线下会问卷用例"

        print self.noww(),":添加线下会问卷用例执行完毕"
    """
    #获取当前时间
    def noww(self):
        owww=datetime.now()
        strnoww = datetime.strftime(owww, '%Y-%m-%d %H:%M:%S')
        return strnoww

if __name__ == "__main__":
    #全部用例按照数字顺序测试
    #unittest.main()
    StartTime = time.time()
    suite = unittest.TestSuite()
    # 指定单个单元测试（ 需要配置运行方式才能走main函数，参考https://www.cnblogs.com/youreyebows/p/7867508.html）
    suite.addTest(Offline_Meeting_Test("test_001_createoffline"))


    #执行单元测试，生成报告
    AddSuite = report.AllReport()
    AddSuite.OnlyNeed_Suite(suite)

    #发送邮件
    EndTime = time.time()
    PerformTime = EndTime - StartTime
    content ="test_001_createoffline"

    # SendEmail = email.SendEmailModel()
    SendEmail = email_oper.SendEmailModel()
    SendEmail.PostReport_only(PerformTime,content)