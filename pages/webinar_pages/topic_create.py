# -*- coding: utf-8 -*-
"""
os模块就是对操作系统进行操作，比如取文件的路径。

sys模块提供了一系列有关Python运行环境的变量和函数,例如：
#生成报告是报错，编码错误。python2.7默认使用ascii，设置成utf-8，python2.7以后不用setdefaultencoding了
   reload(sys)
  sys.setdefaultencoding('utf8')
"""
import sys
reload(sys)  #在解释器里修改的编码只能保证当次有效，在重启解释器后，会发现，编码又被重置为默认的ascii了
sys.setdefaultencoding('utf8')
import os
curPath = os.path.abspath(os.path.dirname(__file__))
print os.path.dirname(__file__)
print curPath
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

import time
from datetime import datetime
import unittest
from test_case.base_unit import BaseUnit
from common.report import report
from pages.common_pages.login_page import LoginPage
from pages.common_pages.choose_page import ChoosePage
from pages.off_line_meeting_pages.index_page import IndexPage
from common.mail import email_oper

class Topic_create_Test(BaseUnit):

    """线下会测试用例"""

    # 登录，并创建线下会
    def test_001_createtopic(self):
        #下面一句的文字，是通过Python的一种注释doc string，用于函数、类和方法的描述，HTMLTestRunner可以读取此类型注释
        """ 测试创建会议 """

        print "开始执行登录，并创建线下会用例：", self.noww()
        object = LoginPage(self.driver)

        object = ChoosePage(self.driver)
        object.clickUnderLine()
        object = IndexPage(self.driver)
        object.ClickCreateUnderLine()
        print "登录，并创建线下会用例执行完成：", self.noww()