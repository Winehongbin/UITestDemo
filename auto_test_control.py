# -*- coding: utf-8 -*-

import os
import sys
curPath = os.path.abspath(os.path.dirname(__file__)) #os.path.basename(path):返回所给路径path的最底层路径名或者是文件名；
# #os.path.dirname(__file__):返回脚本的路径
rootPath = os.path.split(curPath)[0]  #os.path.split(curPath)[0]:path分割成目录
sys.path.append(rootPath)
import unittest
from common.report import report
from test_case.offline_meeting_case import Offline_Meeting_Test
import time
from common.mail import email_oper
from test_case.wechat_case import Wechat_Test
from test_case.questionnaire_case import Questionnaire
# from test_case.webinar_create_case import Webinar_Case
from test_case.webinar_case import Webinar_Case
from test_case.member_case import Member_Test

class ConrollerShow():


    def Def_List(self,class_name):   #def_list 获取单元测试中，测试函数列表， #class的名字，不用双引号，直接用

        list = []
        def_name = dir(class_name)    #dir():返回当前范围内的变量、方法和定义的类型列表
        for tmp in def_name:
            def_four = str(tmp)[:4]   # str(tmp)[:4] :索引和切片，从下标为0的元素选择到下标为3的元素，不包括下标4的元素
            if def_four == "test":    #取方法前四个字母为test的
                list.append(tmp)     #append() 方法向列表的尾部添加一个新的元素。只接受一个参数
        return list

    def SupportTool_Control(self):  #SupportTool_Control 用来管理我们的用例启动方式，执行所有配置好的单元测试，生成报告并发送
        StartTime = time.time()       #time()：返回当前时间的时间戳（1970纪元后经过的浮点秒数），需要import time
        suite = unittest.TestSuite()     #创建一个测试集合

        #线下会
        offline_test = self.Def_List(Offline_Meeting_Test)   #Def_List 获取指定单元测试中，测试函数列表
        for offline_tmp in offline_test:
            suite.addTest(Offline_Meeting_Test(offline_tmp))   #addTest()的方法，测试套件中添加测试用例,可以加载不同类里面的不同测试函数

        #微信
        wechat_test = self.Def_List(Wechat_Test)  # Def_List 获取指定单元测试中，测试函数列表
        for wechat_tmp in wechat_test:
            suite.addTest(Wechat_Test(wechat_tmp))

        #问卷
        questtionnaire_test = self.Def_List(Questionnaire)  # Def_List 获取指定单元测试中，测试函数列表
        for questtionnaire_tmp in questtionnaire_test:
            suite.addTest(Questionnaire(questtionnaire_tmp))

        #线上会
        webinar_test = self.Def_List(Webinar_Case)  # Def_List 获取指定单元测试中，测试函数列表
        for webinar_tmp in webinar_test:
            suite.addTest(Webinar_Case(webinar_tmp))

        #客户管理
        member_test = self.Def_List(Member_Test)  # Def_List 获取指定单元测试中，测试函数列表
        for member_tmp in member_test:
            suite.addTest(Member_Test(member_tmp))



        #创建测试报告
        AddSuite = report.AllReport()   #AddSuite = report.AllReport() :实例化AllReport类
        AddSuite.onlyneed_suite(suite)    #onlyneed_suite(suite) ：指定suit的report

        # 发送邮件
        EndTime = time.time()
        PerformTime = EndTime - StartTime
        content = "autoTest"
        SendEmail = email_oper.SendEmailModel()  #实例化SendEmailModel类
        SendEmail.postreport_only(PerformTime,str(content)) #调用SendEmailModel类中postreport_only方法


if __name__ == '__main__':
    A = ConrollerShow()
    A.SupportTool_Control()


