#-*- coding:UTF-8 -*-
#!/usr/bin/python

import os
from datetime import datetime



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
        receiver = ['394522655@qq.com','cara_gao@sinobasedm.com'] # 收件人'gavin_li@sinobasedm.com','gavin_li@sinobasedm.com','1511274870@qq.com','andy_yang@sinobasedm.com'
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
        print fileHTML
        #fileHTML = r"..\ReportAndEmail\Smarket3.0_TestReport.html"
        att = MIMEText(open(fileHTML, 'rb').read(), 'base64', 'utf-8')
        att["Content-Type"] = 'application/octet-stream'
        att["Content-Disposition"] = 'attachment; filename="Smarket3.0_TestReport.html"'
        msgRoot.attach(att)

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
    content = "test_001_createoffline"
    """创建线下会"""
    # content = "test_003_offline"


    P.PostReport_only("总时间",content)