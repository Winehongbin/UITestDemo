#-*- coding:UTF-8 -*-
#!/usr/bin/python

import os
from datetime import datetime
from pages.common_pages.base import BasePage


class SendEmailModel():


    def PostEmail(self):
        import smtplib  #Python对SMTP支持有smtplib和email两个模块，email负责构造邮件，smtplib负责发送邮件。
        # from email_oper.mime.multipart import MIMEMultipart
        from email.mime.multipart import MIMEMultipart
        from email.mime.text import MIMEText
        from email.header import Header
        # from email_oper.mime.text import MIMEText
        from email.mime.text import MIMEText  #//导入MIMEText类
        # from email_oper.header import Header

        sender = 'gavin_li@sinobasedm.com'                      #发件人
        receiver = ['huoyan109@126.com','huoyan108@126.com']   #收件人
        subject = "Smarket3.0自动化测试测试邮件"          #邮件主题
        smtpserver = 'smtp.exmail.qq.com'                      #不同的邮件，有不同端口
        username = 'gavin_li@sinobasedm.com'                  #进入邮箱的账户名
        password = 'Abc@123'                           #进入邮箱的密码
        fileHTML = r"..\\Smarket3.0_TestReport.html"
        fileProgramLog = "D:\Info.txt"
        fileTestLogFail = "D:\TestLogFail.txt"
        fileTestLogPass = "D:\TestLogPass.txt"
        msgRoot = MIMEMultipart()
        msgRoot['From'] = Header("李鸿飞", 'utf-8')
        msgRoot['To'] =  Header("每一位项目相关人员", 'utf-8')
        
        subject = 'Python SMTP 邮件自动化测试'
        msgRoot['Subject'] = Header(subject, 'utf-8')

        msgRoot['Python SMTP 邮件自动化测试'] = subject         #主题
        #主要内容
        text_msg = MIMEText("<html><body><p><span style='color: black;'>&nbsp;&nbsp; hello every Receiver:</span></p><p>&nbsp;&nbsp;&nbsp;&nbsp; 附件为本次回归的测试报告，请各位查收。<br/></p><p/>&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; 自动化测试小组敬上</p></body></html>",'html',_charset="utf-8")
        msgRoot.attach(text_msg)

        #附件
        att = MIMEText(open(fileHTML, 'rb').read(), 'base64', 'utf-8')
        att["Content-Type"] = 'application/octet-stream'
        att["Content-Disposition"] = 'attachment; filename="Smarket3.0_TestReport.html"'
        msgRoot.attach(att)
        att = MIMEText(open(fileProgramLog, 'rb').read(), 'base64', 'utf-8')
        att["Content-Type"] = 'application/octet-stream'
        att["Content-Disposition"] = 'attachment; filename="Info.txt"'
        msgRoot.attach(att)
        att = MIMEText(open(fileTestLogFail, 'rb').read(), 'base64', 'utf-8')
        att["Content-Type"] = 'application/octet-stream'
        att["Content-Disposition"] = 'attachment; filename="TestLogFail.txt"'
        msgRoot.attach(att)
        att = MIMEText(open(fileTestLogPass, 'rb').read(), 'base64', 'utf-8')
        att["Content-Type"] = 'application/octet-stream'
        att["Content-Disposition"] = 'attachment; filename="TestLogPass"'
        msgRoot.attach(att)      
        try:
            smtp = smtplib.SMTP()
            smtp.connect(smtpserver)
            smtp.login(username, password)
            smtp.sendmail(sender, receiver, msgRoot.as_string())
            smtp.quit()
            print "邮件发送成功"
        except smtplib.SMTPException:
            print "Error: 无法发送邮件"

    #邮件内容的设置
    def PostReport_only(self,PerformTime,content):


        import smtplib
        content_str=str(content)
        # from email.MIMEMultipart import MIMEMultipart
        from email.mime.multipart import MIMEMultipart
        from email.mime.text import MIMEText
        from email.mime.application import MIMEApplication
        from email.header import Header
        sender = 'cara_gao@sinobasedm.com'  # 发件人
        receiver = ['394522655@qq.com','cara_gao@sinobasedm.com','gavin_li@sinobasedm.com','gavin_li@sinobasedm.com','1511274870@qq.com','andy_yang@sinobasedm.com','lisa_xing@sinobasedm.com','nina_xiao@sinobasedm.com','vivian_shi@sinobasedm.com','merry_you@sinobasedm.com']
        subject = "Smarket3.0自动化平台测试邮件"  # 邮件主题
        smtpserver = 'smtp.exmail.qq.com'  # 不同的邮件，有不同端口
        username = 'cara_gao@sinobasedm.com'  # 进入邮箱的账户名
        password = 'Sino@123'  # 进入邮箱的密码
        msgRoot = MIMEMultipart()
        msgRoot['From'] = Header("自动化测试平台", 'utf-8')
        msgRoot['To'] = Header("每一位项目相关人员", 'utf-8')
        msgRoot['Subject'] = Header(subject, 'utf-8') #Subject为邮件主题
        """
        主要内容，参考例子：
        msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')
        注意到构造MIMEText对象时，第一个参数就是邮件正文，第二个参数是MIME的subtype，传入'plain'，
        最终的MIME就是'text/plain'，最后一定要用utf-8编码保证多语言兼容性。
        """
        text_msg = MIMEText(
            "<html><body><p><span style='color: black;'>&nbsp;&nbsp; hello every Receiver:</span></p>"
            "<p>&nbsp;&nbsp;&nbsp;&nbsp; 本次测试总耗时："+ str(PerformTime) +"秒<br/></p>"
            "<p>&nbsp;&nbsp;&nbsp;&nbsp; 附件为本次回归的测试报告，请各位查收。<br/></p>"
            "<p>&nbsp;&nbsp;&nbsp;&nbsp; 本次回归测试执行用例范围："+ content +"<br/></p>"
            "<p/>&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; 自动化测试小组敬上</p></body></html>",
            'html', _charset="utf-8")
        msgRoot.attach(text_msg)
        # 附件
        fileHTML = os.path.abspath(os.path.dirname(os.path.dirname(__file__))) + "\\report\Smarket3.0_TestReport.html"
        """
        定义文件目录,os.listdir(path):返回指定路径下的文件和文件夹列表;
        程序中 \ 是转义符，所以关于路径的写法要用/;
        字符串引号外加r可以不转义
        """

        result_dir = os.path.abspath(os.path.dirname(os.path.dirname(__file__))) + "\\report\\reportlog"
        print result_dir
        lists = os.listdir(result_dir)

        """
        重新按时间对目录下的文件进行排序,
        list.sort([func]):该方法没有返回值，但会对列表的对象进行排序,func 可选参数, 如果指定该参数会使用该参数的方法进行排序。
        sort按key的关键字进行升序排序，lambda的入参fn为lists列表的元素，获取文件的最后修改时间，所以最终以文件时间从小到大排序
        最后对lists元素，按文件修改时间大小从小到大排序。
        获取最新文件的绝对路径，列表中最后一个值,文件夹+文件名
        但是lambda fn这些的用法 不会，有熟练经验的大神可以补充，以便分享
        """
        lists.sort(key=lambda fn: os.path.getmtime(result_dir+"\\"+fn))
        print(('最新的文件为： ' + lists[-1]))
        fileHTML = os.path.join(result_dir, lists[-1])
        print (file)

        f = open(fileHTML, 'rb')
        mail_body = f.read()
        f.close()

        msg = MIMEText(mail_body, 'html', 'utf-8')
        msgRoot = MIMEMultipart()
        msgRoot['Subject'] = Header(subject, 'utf-8')  # Subject为邮件主题
        msgRoot.attach(msg)
        msgRoot['From'] = sender
        att = MIMEApplication(open(fileHTML, 'rb').read())
        att.add_header('Content-Disposition', 'attachment', filename=lists[-1])
        msgRoot.attach(att)

        """
        print fileHTML
        #fileHTML = r"..\ReportAndEmail\Smarket3.0_TestReport.html"
        att = MIMEText(open(fileHTML, 'rb').read(), 'base64', 'utf-8')
        att["Content-Type"] = 'application/octet-stream'
        att["Content-Disposition"] = 'attachment; filename="Smarket3.0_TestReport.html"'
        msgRoot.attach(att)
        """
        try:
            smtp = smtplib.SMTP()  #创建一个SMTP对象
            smtp.connect(smtpserver)   #/通过connect方法链接到smtp主机
            smtp.login(username, password)  #
            #sendmail()方法就是发邮件，由于可以一次发给多个人，所以传入一个list，邮件正文是一个str，as_string()把MIMEText对象变成str。
            smtp.sendmail(sender, receiver, msgRoot.as_string())
            smtp.quit()
            print "邮件发送成功"
        except smtplib.SMTPException:
            print "Error: 无法发送邮件"


if __name__ == '__main__':
    P = SendEmailModel()
    # content = "test_001_createoffline;test_002_manageoffline"
    content = "test_001_loginoffline;test_002_createoffline"
    # content = "test_003_offline"
    P.PostReport_only("总时间",content)