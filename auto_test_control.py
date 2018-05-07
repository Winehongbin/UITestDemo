# -*- coding: utf-8 -*-


import os
import sys
"""
os.path.basename(path):返回所给路径path的最底层路径名或者是文件名
os.path.dirname(__file__):返回脚本的路径
os.path.split(curPath)[0]:path分割成目录
"""
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
import unittest
from common.report import report
from common.mail import email_oper
from test_case.offline_meeting import Offline_Meeting_Test
import time
from common.mail import email_oper

class ConrollerShow():
    def Def_List(self,class_name):
        #class的名字，不用双引号，直接用
        list = []
        def_name = dir(class_name)
        for tmp in def_name:
            def_four = str(tmp)[:4]
            if def_four == "test":
                list.append(tmp)
        return list
    def SupportTool_Control(self):
        StartTime = time.time()
        suite = unittest.TestSuite()

        #线下会   #文件名： #类名：
        offline_test = self.Def_List(Offline_Meeting_Test)
        for offline_tmp in offline_test:
            suite.addTest(Offline_Meeting_Test(offline_tmp))

        #创建测试报告
        AddSuite = report.AllReport()
        AddSuite.OnlyNeed_Suite(suite)

        # 发送邮件
        EndTime = time.time()
        PerformTime = EndTime - StartTime
        # content = "autoTest"
        content ="test_002_createoffline"
        # content =["test_001_loginoffline","test_002_createoffline","test_003_interaction"]

        SendEmail = email_oper.SendEmailModel()
        SendEmail.PostReport_only(PerformTime,str(content))

if __name__ == '__main__':
    A = ConrollerShow()
    A.SupportTool_Control()


