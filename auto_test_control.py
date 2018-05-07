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

    """
    def_list 获取单元测试中，测试函数列表
    dir():返回当前范围内的变量、方法和定义的类型列表
    str(tmp)[:4] :索引和切片，从下标为0的元素选择到下标为3的元素，不包括下标4的元素
    append() 方法向列表的尾部添加一个新的元素。只接受一个参数
    """
    def Def_List(self,class_name):
        #class的名字，不用双引号，直接用
        list = []
        def_name = dir(class_name)
        for tmp in def_name:
            def_four = str(tmp)[:4]
            if def_four == "test":
                list.append(tmp)
        return list

    """
    SupportTool_Control 用来管理我们的用例启动方式，执行所有配置好的单元测试，生成报告并发送
    time()：返回当前时间的时间戳（1970纪元后经过的浮点秒数），需要import time
    """
    def SupportTool_Control(self):
        StartTime = time.time()
        suite = unittest.TestSuite()     #创建一个测试集合


        offline_test = self.Def_List(Offline_Meeting_Test)   #Def_List 获取指定单元测试中，测试函数列表
        for offline_tmp in offline_test:
            suite.addTest(Offline_Meeting_Test(offline_tmp))   #addTest()的方法，测试套件中添加测试用例,可以加载不同类里面的不同测试函数

        """
        创建测试报告
        AddSuite = report.AllReport() :实例化AllReport类
        OnlyNeed_Suite(suite) ：指定suit的report

        """
        AddSuite = report.AllReport()
        AddSuite.OnlyNeed_Suite(suite)

        # 发送邮件
        EndTime = time.time()
        PerformTime = EndTime - StartTime
        content = "autoTest"
        # content ="test_002_createoffline"
        # content =["test_001_loginoffline","test_002_createoffline","test_003_interaction"]

        SendEmail = email_oper.SendEmailModel()
        SendEmail.PostReport_only(PerformTime,str(content))  #20180507


if __name__ == '__main__':
    A = ConrollerShow()

    A.SupportTool_Control()


