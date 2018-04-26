# -*- coding: utf-8 -*-
'''
HTMLTestRunner： 是 基于 unittest 单元测试的 HTML报告 的一个第三库，
下载地址：http://tungwaiyip.info/software/HTMLTestRunner.html
鼠标右键→目标另存为，保存到本地。
安装：将下载的HTMLTestRunner.py文件复制到Python安装目录下即可

'''
import HTMLTestRunner
import os.path
import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)


class AllReport(object):    
    def LoginShow_report(self,caselist_Login,caselist_File,suitname,CaseClassName1,CaseClassName2):
        '''目前Name1为Login，Name2为FileManagement'''
        for tmp in caselist_Login:
            suitname.addTest(CaseClassName1(tmp))  #此处的Login为unittest的class名称
        for File in caselist_File:
            suitname.addTest(CaseClassName2(File))
        myfile="D:\workspace\Smarket\src\ReportAndEmail\Smarket3.0_TestReport.html"


        """
        声明报告
        w代表写入，b代表2进制；rb只能读取不能写
        open():打开Smarket3.0_TestReport.html这个文件，如果没有，可以自己手动创建文件
        """
        myresult=open(myfile,'wb')

        """
        HTMLTestRunner.HTMLTestRunner:调用HTMLTestRunner模块下的HTMLTestRunner类；
        使用HTMLTestRunner配置参数，输出报告路径、报告标题、描述；
        stream：指定测试报告文件；description：定义测试报告的副标题。
        """

        #声明报告
        myresult=open(myfile,'wb')         #w代表写入，b代表2进制；rb只能读取不能写

        runner=HTMLTestRunner.HTMLTestRunner(title=u"自动化筹备小组模型展示，前来报告",stream=myresult,
                                             description=u"此报告目前为测试阶段状态，谢谢观赏,自动化测试小组敬上")
        runner.run(suitname)
    def OnlyNeed_Suite(self,suitname):

        myfile=os.path.abspath(os.path.dirname(os.path.dirname(__file__)))+"\\report\Smarket3.0_TestReport.html"
        print myfile
        #myfile="..\ReportAndEmail\Smarket3.0_TestReport.html"

        """
          声明报告
          w代表写入，b代表2进制；rb只能读取不能写
          open():打开Smarket3.0_TestReport.html这个文件，如果没有，可以自己手动创建文件
          """
        myresult=open(myfile,'wb')

        """
        HTMLTestRunner.HTMLTestRunner:调用HTMLTestRunner模块下的HTMLTestRunner类；
        使用HTMLTestRunner配置参数，输出报告路径、报告标题、描述；
        stream：指定测试报告文件；description：定义测试报告的副标题。
        """
        runner=HTMLTestRunner.HTMLTestRunner(title=u"Smarket3.0自动化测试报告，前来报告",stream=myresult,
                                             description=u"此报告目前为自动化测试平台提供："
                                                         u"1、各模块负责人手工校验失败用例；"
                                                         u"2、确认为bug,请联系开发人员修复bug"
                                                         u"3、不是bug，请优化用例，增强代码稳定性")
        """
        HTMLTestRunner的run()方法来运行测试套件中所组件的测试用例。
        """
        runner.run(suitname)
if __name__ == "__main__":
    """
    pass是空语句,是为了保持程序结构的完整性。 pass 不做任何事情,一般用做占位语句
    """
    pass

