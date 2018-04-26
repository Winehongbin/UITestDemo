# -*- coding: utf-8 -*-
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from datetime import datetime

import time

import os

from selenium.webdriver.common.by import By

class OffLineMeeting():
    """
    def login(self):
        # print u"开始登陆", self.deprint()
        #201604166
        # global driver
        print self.deprint(),":开始登陆"
        driver.find_element_by_xpath("//form/div[1]/input")
        driver.find_element_by_xpath("/html/body/div[2]/div/div/div[1]/form/div[1]/input").send_keys("18210127910")
        driver.find_element_by_css_selector("input[type='password']").send_keys('123123')
        driver.find_element_by_xpath("/html/body/div[2]/div/div/div[1]/form/input").click()
        driver.implicitly_wait(30)
        print self.deprint(),":登陆完成"

    def clickUnderLine(self):
        print self.deprint(),u":开始进入线下会"
        # 获得当前窗口
        handleNow = driver.current_window_handle
        driver.switch_to_window(handleNow)
        time.sleep(8)
        #点击线下会
        driver.find_element_by_css_selector("#sortContainer > a:nth-child(9)").click()
        # driver.find_element_by_css_selector("# sortContainer > a:nth-child(9) > img").click()
        driver.implicitly_wait(30)
        time.sleep(8)
        # 获取下一个窗口句柄，跳转
        driver.switch_to.window(driver.window_handles[-1])
        print self.deprint(),":正常进入线下会"

    #创建一场会议--------已拉出
    def createUnderLine(self):
        print self.deprint(),":开始创建线下会"
        # 点击创建会议
        # 获取下一个窗口句柄，跳转
        driver.switch_to.window(driver.window_handles[-1])
        driver.find_element_by_css_selector(
            "#g-right > div > div.clearfix.ng-scope > div.contact-stats-box.w715 > div.event-stats-l > div > button").click()
        driver.implicitly_wait(30)
        ##创建新的会议页面
        # “会议名称”字段
        # 获取当前时间
        time_now = int(time.time())
        # 转换成localtime
        time_local = time.localtime(time_now)
        # 转换成新的时间格式(2016-05-09 18:59:20)
        dt = time.strftime("%Y-%m-%d %H:%M:%S", time_local)
        driver.find_element_by_id("seminarName").send_keys(u"自动化测试" + dt)
        # “会议时间”字段
        driver.find_element_by_id("seminarTime").click()
        handleNow = driver.current_window_handle
        driver.switch_to_window(handleNow)
        driver.find_element_by_name('daterangepicker_start').send_keys('2016-08-24')
        driver.find_element_by_name('daterangepicker_end').send_keys('2016-08-24')
        driver.find_element_by_id("seminarTime").click()
        driver.find_element_by_xpath("/html/body/div[4]/div[3]/div/button[1]").click()
        # “地区”字段
        driver.find_element_by_css_selector(
            "#createSeminarScroller > form > div:nth-child(5) > div > div > div:nth-child(1) > button").click()
        driver.find_element_by_css_selector(
            "#createSeminarScroller > form > div:nth-child(5) > div > div > div.dropdown.r-select.select-ssmd.open > ul > li.ng-scope > a").click()
        driver.implicitly_wait(30)
        # "会议地点" 字段
        driver.find_element_by_css_selector("#createSeminarScroller > form > div:nth-child(6) > div > input").send_keys(
            u"北京")
        driver.implicitly_wait(30)
         # “注册表单”字段

        20180415
        #不启动注册表单,默认启动不错做
        # driver.find_element_by_css_selector("#createSeminarScroller > form > div:nth-child(9) > div.col-md-2 > div > button > span").click()
        # driver.find_element_by_css_selector("#createSeminarScroller > form > div:nth-child(9) > div.col-md-2 > div > ul > li:nth-child(2) > a").click()

        #点击模板选择
        driver.find_element_by_css_selector('#createSeminarScroller > form > div:nth-child(8) > div.col-md-6 > div > button > span').click()
        # 获取所有模板
        time.sleep(3)
        driver.find_element_by_css_selector('#createSeminarScroller > form > div:nth-child(8) > div.col-md-6 > div > ul > li:nth-child(8) > a').click()
        driver.implicitly_wait(10)

        #选择不启用启用微信公众号
        driver.find_element_by_css_selector('#createSeminarScroller > form > div:nth-child(9) > div.col-md-2 > div > button > span').click()
        driver.implicitly_wait(10)
        driver.find_element_by_css_selector('#createSeminarScroller > form > div:nth-child(9) > div.col-md-2 > div > ul > li:nth-child(1) > a').click()
        driver.implicitly_wait(10)

        driver.find_element_by_css_selector('#createSeminarScroller > form > div:nth-child(9) > div.col-md-6 > div > button > span').click()
        # 获取所有模板
        driver.find_element_by_css_selector('#createSeminarScroller > form > div:nth-child(9) > div.col-md-6 > div > ul > li:nth-child(8) > a').click()
        #Select(driver.find_element_by_css_selector("#createSeminarScroller > form > div:nth-child(9) > div.col-md-6 > div > ul")).select_by_visible_text(u'新建注册表单(9)')

        driver.implicitly_wait(30)
         #点击“创建”按钮
        driver.find_element_by_css_selector("#createSeminar > div > div > div.modal-footer > button").click()
        driver.implicitly_wait(30)
        #201804166
        print self.deprint(),"：线下会创建成功"
        print self.deprint(),":线下会进入报名表单管理栏目"
        # 点击“报名表单”菜单
        time.sleep(3)
        driver.find_element_by_css_selector('body > div.g-container > div.g-left.s-left > ul.m-nav-ul.nav-event.ng-scope > li:nth-child(3) > a').click()
        driver.implicitly_wait(30)
        time.sleep(8)
        # 点击“开始报名”按钮
        driver.find_element_by_css_selector('#g-right > div > div:nth-child(1) > div.m-grid.grid-noborder.grid-formmanage.u-mt10 > table > tbody > tr > td:nth-child(9) > a.icon-o-start.ng-scope').click()
        driver.implicitly_wait(30)
        print self.deprint(),":启动报名表单成功"

       """
    def is_element_exist(self, css):
        s = driver.find_elements_by_css_selector(css_selector=css)
        if len(s) == 0:
            # print "元素未找到:%s" % css
            return False
        elif len(s) == 1:
            return True
        else:
            # print "找到%s个元素：%s" % (len(s), css)
            return False
    #开始会议
    def beginLan(self):
        print "beginLan：", self.deprint()
    #返回会议列表
    def returnlist(self):
         driver.find_element_by_css_selector("#g-right > div > div.event-subtitle.ng-scope > div > a").click()
         driver.implicitly_wait(30)


    """
    #获取会议列表
    def clicklist(self):
        time.sleep(5)
        print "进入第一场线下会：", self.deprint()
        #点击“会议列表”
        driver.find_element_by_xpath("/html/body/div[2]/div[1]/ul/li[2]/h2/a").click()
        driver.implicitly_wait(30)
        time.sleep(3)
        #点击会议列表页的首个“会议名称”
        driver.find_element_by_css_selector("#g-right > div > div.m-grid.grid-default.grid-event.grid-over.ng-scope > table > tbody > tr:nth-child(1) > td:nth-child(2) > a").click()
        driver.implicitly_wait(30)
        #获取下一个窗口句柄，跳转
        driver.switch_to.window(driver.window_handles[-1])

    #互动环节操作
    def interaction_link(self):
        time.sleep(5)
        # 点选“互动环节”
        print self.deprint(),":开始添加互动环节"
        driver.find_element_by_css_selector("body > div.g-container > div.g-left.s-left > a.icon-o-setmodule.ng-scope").click()
        driver.implicitly_wait(30)
        time.sleep(3)
        # 点击确定
        if driver.find_element_by_css_selector("#modulecheckbox6").is_selected():
            driver.implicitly_wait(30)
            time.sleep(2)
            driver.find_element_by_css_selector("#setFiled > div > div > div.modal-footer > input").click()
            driver.implicitly_wait(30)
            time.sleep(5)
        else:
            driver.find_element_by_css_selector("#setFiled > div > div > div.modal-body.ng-isolate-scope > div:nth-child(4) > div:nth-child(7) > label").click()

            driver.implicitly_wait(30)
            time.sleep(5)
            driver.find_element_by_css_selector("#setFiled > div > div > div.modal-footer > input").click()
        print self.deprint(),"：添加互动环节成功"
     """
    #创建问卷
    def creat_que(self):
        time.sleep(5)
        print self.deprint(),":开始创建问卷"
        #点击左侧的“互动环节”按钮
        driver.find_element_by_css_selector("body > div.g-container > div.g-left.s-left > ul.m-nav-ul.nav-event.ng-scope > li:nth-child(6) > a > strong").click()
        driver.implicitly_wait(30)
        time.sleep(3)
        #点击“创建互动”按钮
        driver.find_element_by_css_selector("#g-right > div > div.event-title.ng-scope > div > div > a").click()
        driver.implicitly_wait(30)
        #点击下拉列表“创建问卷”选项
        driver.find_element_by_css_selector("#g-right > div > div.event-title.ng-scope > div > div > ul > li:nth-child(1) > a").click()
        driver.implicitly_wait(30)
        #获取下一个窗口句柄，跳转
        driver.switch_to.window(driver.window_handles[-1])
        #填写问卷标题
        driver.find_element_by_css_selector("#questionaireTitle").send_keys(u"问题一")
        driver.implicitly_wait(30)
        #点击开始时间
        driver.find_element_by_css_selector('#startTime').click()
        #选择日期控件的时间，设置死
        # 下拉小时列表，给20点的固定值
        sel = driver.find_element_by_css_selector('body > div:nth-child(6) > div.calendar.second.right.single > div.calendar-time > select.hourselect')
        Select(sel).select_by_value("0")
        driver.find_element_by_css_selector('body > div:nth-child(6) > div.ranges > div > button.applyBtn.btn.btn-small.btn-sm.btn-info').click()
        driver.implicitly_wait(30)
        # 点击结束时间
        driver.find_element_by_css_selector('#endTime').click()
        # 下拉小时列表，给22点的固定值
        sel = driver.find_element_by_css_selector(
            'body > div:nth-child(7) > div.calendar.second.right.single > div.calendar-time > select.hourselect')
        Select(sel).select_by_value("23")
        driver.find_element_by_css_selector(
            'body > div:nth-child(7) > div.ranges > div > button.applyBtn.btn.btn-small.btn-sm.btn-info').click()
        driver.implicitly_wait(30)
        #点击确定
        driver.find_element_by_css_selector("body > div.g-container-box > div.m-container.ng-scope > div.m-form-btn.form-btn-border.ng-scope > a").click()
        self.create_questions()

    #创建问题
    def create_questions(self):
        print self.deprint(),':创建问答题集'
        time.sleep(3)
        #添加姓名字段
        driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div[1]/ul/li[1]/ul/li[1]/a').click()
        # driver.find_element_by_partial_link_text("姓名").click()
        # driver.find_element_by_css_selector('body > div.g-container-box > div.m-container.ng-scope > div.m-form-setting.ng-scope > div.g-fs-right > ng-form > question-items > div > sugar-form-field > div > div > div.g-fs-input > div > input'). send_keys(u'：')

        driver.implicitly_wait(30)
        # 添加用户名
        driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div[1]/ul/li[1]/ul/li[5]/a').click()
        # driver.find_element_by_partial_link_text("公司").click()
        # driver.find_element_by_css_selector('body > div.g-container-box > div.m-container.ng-scope > div.m-form-setting.ng-scope > div.g-fs-right > ng-form > question-items > div:nth-child(2) > sugar-form-field > div > div > div.g-fs-input > div > input'). send_keys(u'：')
        # # driver.find_element_by_css_selector('body > div.g-container-box > div.m-container.ng-scope > div.m-form-setting.ng-scope > div.g-fs-right > ng-form > question-items > div > sugar-form-field > div > div > div.g-fs-input > div > input').send_keys(u'必填')
        driver.implicitly_wait(30)

        #添加公司
        driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div[1]/ul/li[1]/ul/li[7]/a').click()
        # driver.find_element_by_partial_link_text("身份标识").click()
        # # driver.find_element_by_css_selector('body > div.g-container-box > div.m-container.ng-scope > div.m-form-setting.ng-scope > div.g-fs-right > ng-form > question-items > div:nth-child(3) > sugar-form-field > div > div > div.g-fs-input > div > input'). send_keys(u'必填')
        # driver.find_element_by_css_selector('body > div.g-container-box > div.m-container.ng-scope > div.m-form-setting.ng-scope > div.g-fs-right > ng-form > question-items > div > sugar-form-field > div > div > div.g-fs-input > div > input').send_keys(':')

        driver.implicitly_wait(30)


        # 最后保存
        driver.find_element_by_css_selector(
            'body > div.g-container-box > div.m-container.ng-scope > div.m-form-setting.ng-scope > div.g-fs-right > ng-form > p > input').click()
        driver.implicitly_wait(30)
        driver.switch_to.window(driver.window_handles[-1])
        driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div[2]/input").click()
        print self.deprint(),":创建问卷完成"
    #gm 20180415
    #关闭问题统计界面
    def close_tongji(self):
        driver.close()
        driver.switch_to.window(driver.window_handles[-1])
    #end gm 20180415
    #进入会议专题
    def topicpage(self):
        #点击会议专题按钮
        time.sleep(15)
        driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[2]/div[1]/p/a[1]").click()
        driver.implicitly_wait(30)
        time.sleep(15)
        #点击注册按钮
        # driver.find_element_by_xpath('/html/body/div[1]/div/div/div/a[2]').click()
        # driver.implicitly_wait(30)
        # time.sleep(15)
    # 我要报名页面
    def sign_up(self):  #我要报名页面

        #点击“我要报名”
        # 获取下一个窗口句柄，跳转
        driver.switch_to.window(driver.window_handles[-1])
        #点击我要报名按钮
        driver.find_element_by_css_selector("body > div.event-state > div > div > a").click()
        driver.implicitly_wait(30)
        time.sleep(8)

        #20180416判断是登录页面还是直接报名

        mail_dress= self.is_element_exist('#con_one_1 > div:nth-child(1) > input')
        if mail_dress:
            print u"答题者的登录页面"
        else:
            print u"直接登记报名"
        if self.valid_new_sign_up():
            time.sleep(3)
            driver.switch_to.window(driver.window_handles[-1])

            # 点击登录
            driver.find_element_by_css_selector("#con_one_1 > input").click()
            driver.implicitly_wait(30)
            # time.sleep(1)

            #20180416
            """
            the_element= driver.find_element_by_css_selector('#con_one_1 > div.login-null').is_displayed()
            if the_element:
                print "element appears."
                test.new_register()
            else:
                return
            """

            """
            print dd
            if dd.is_element_visible:
                test.new_register()
            time.sleep(3)
            """
            #20180416
            time.sleep(2)
            driver.close()
            driver.switch_to.window(driver.window_handles[-1])
            # driver.close()
            # volume_ans(self)


        # else:
        #     test.new_register()
    #回答问卷
    def volume_ans(self):
        #点击“互动环节”菜单
        driver.switch_to.window(driver.window_handles[-1])
        driver.refresh()
        time.sleep(3)
        driver.find_element_by_xpath('/html/body/div[2]/div[2]/ul[2]/li[6]/a/strong').click()
        driver.implicitly_wait(30)

        # 点击开始按钮
       # driver.find_element_by_css_selector(
        #    '#g-right > div > div.row.ng-scope > div:nth-child(1) > div > div.interact-oprate > a.link-icon-gray.ng-binding.ng-scope > i').click()
        """ 20180416
        driver.find_element_by_partial_link_text('提前开始').click()
        driver.implicitly_wait(30)
        driver.refresh()
        """
        #点击“第一个问卷
        time.sleep(3)
        driver.refresh()
        driver.implicitly_wait(30)
        # #点击统计按钮
        # driver.find_element_by_xpath('//*[@id="g-right"]/div/div[2]/div/div/div[3]/a[7]').click()
        # driver.find_element_by_xpath('// *[ @ id = "g-right"] / div / div[2] / div[1] / div').click()

        #点击问卷的统计按钮
        driver.find_element_by_xpath('//*[@id="g-right"]/div/div[2]/div[1]/div/div[3]/a[7]').click()
        driver.implicitly_wait(30)
        # 获取下一个窗口句柄，跳转
        driver.switch_to.window(driver.window_handles[-1])
        time.sleep(3)
        # 获取复制按钮的内容
        #body > div.g - container - box > div.m - container.ng - scope > div.clearfix.ng - scope > div.vote - link - box > form > div:nth - child(1) > div > input
        pc_url = driver.find_element_by_css_selector('body > div.g-container-box > div.m-container.ng-scope > div.clearfix.ng-scope > div.vote-link-box > form > div:nth-child(1) > div > input').get_attribute("value")
        print 'pc_url:'+pc_url
        # 新打开一个一个浏览
        # 浏览器 新窗口打开连接
        newwindow = 'window.open("' + pc_url + '")'
        print newwindow
        driver.execute_script(newwindow)
        # 移动句柄，对新打开页面进行操作
        driver.switch_to.window(driver.window_handles[-1])
        #20180416 判断是否是登录
        mail_dress = self.is_element_exist('#con_one_1 > div:nth-child(1) > input')
        if mail_dress:
            print u"是答题者的登录页面"
            driver.find_element_by_xpath('//*[@id="con_one_1"]/div[1]/input').send_keys('12@126.com')
            driver.implicitly_wait(30)
            driver.find_element_by_xpath('//*[@id="con_one_1"]/div[3]/input').send_keys('123123')
            driver.implicitly_wait(30)
            time.sleep(3)
            # 点击登录
            driver.find_element_by_xpath('//*[@id="con_one_1"]/input').click()
            time.sleep(5)
        else:
            print u"直接答题:",self.deprint()

        """
        driver.find_element_by_xpath('//*[@id="con_one_1"]/div[1]/input').send_keys('12@126.com')
        driver.implicitly_wait(30)
        driver.find_element_by_xpath('//*[@id="con_one_1"]/div[3]/input').send_keys('123123')
        driver.implicitly_wait(30)
        time.sleep(3)
        #点击登录
        driver.find_element_by_xpath('//*[@id="con_one_1"]/input').click()
        time.sleep(5)
        """
        #答题

        #问卷内容输入
        #填写姓名
        driver.find_element_by_css_selector('#questionContainer > div.r-form > div > div:nth-child(1) > div.question-option > input').clear()
        driver.implicitly_wait(10)
        time.sleep(3)
        driver.find_element_by_css_selector('#questionContainer > div.r-form > div > div:nth-child(1) > div.question-option > input').send_keys(u'王小强')

        # driver.find_element_by_css_selector('#questionContainer > div.r-form > div > div > div.question-option > input').send_keys(u'王小强')
        driver.implicitly_wait(10)

        #添写用户名
        driver.find_element_by_css_selector('#questionContainer > div.r-form > div > div:nth-child(2) > div.question-option > input').clear()
        driver.implicitly_wait(10)

        driver.find_element_by_css_selector('#questionContainer > div.r-form > div > div:nth-child(2) > div.question-option > input').send_keys(u'Sino')
        driver.implicitly_wait(10)

        #添加手机
        driver.find_element_by_css_selector('#questionContainer > div.r-form > div > div:nth-child(3) > div.question-option > input').clear()
        driver.implicitly_wait(10)
        driver.find_element_by_css_selector('#questionContainer > div.r-form > div > div:nth-child(3) > div.question-option > input').send_keys(u'13303220321')
        driver.implicitly_wait(10)



        #点击提交按钮
        driver.find_element_by_css_selector('#questionContainer > div.m-form-btn > input').click()
        driver.implicitly_wait(30)
        time.sleep(5)   #20180417
        driver.close()

        # 移动句柄，对新打开页面进行操作
        driver.switch_to.window(driver.window_handles[-1])
    #答题记录验证
    def record_ver(self):
        #验证记录是否存在
        driver.switch_to.window(driver.window_handles[-1])
        driver.implicitly_wait(10)
        driver.refresh()
        time.sleep(2)
        is_find=self.is_element_exist('body > div.g-container-box > div.m-container.ng-scope > div:nth-child(5) > section > div > table > tbody > tr > td:nth-child(3)')

        if is_find:
            an_user=driver.find_element_by_css_selector('body > div.g-container-box > div.m-container.ng-scope > div:nth-child(5) > section > div > table > tbody > tr > td:nth-child(3)').text
            if an_user=="12@126.com":
                print u"答题记录已存在"
            else:
                print u"答题记录不存在"
        else:
            print u"没有找到答题记录，可以作答"
        driver.switch_to.window(driver.window_handles[-1])
        driver.refresh()
        time.sleep(5)
    def valid_new_sign_up(self):
        # 邮箱
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="con_one_1"]/div[1]/input').send_keys('12@126.com')
        driver.implicitly_wait(30)
        # 错误提示要素
        mailError = driver.find_element_by_xpath('//*[@id="con_one_1"]/div[2]').text
        #print u"服务器返回测错误信息" + mailError
        if mailError:
            print "出现问题： ", self.deprint()
            return False
        # 密码
        driver.find_element_by_xpath('//*[@id="con_one_1"]/div[3]/input').send_keys('123123')
        driver.implicitly_wait(30)
        mailError = driver.find_element_by_xpath('//*[@id="con_one_1"]/div[4]').text
        #print u"服务器返回测错误信息" + mailError
        if mailError:
            print "出现问题：", self.deprint()
            return False
        return True
    #注册信息页面
    def new_register(self):   #register---注册
        # 点击“注册”按钮
        driver.find_element_by_css_selector("#con_one_1 > div.form-bottom > div > div.col-md-5.form-bottom-txt > a").click()
        driver.implicitly_wait(30)
        time.sleep(3)
        # 获取下一个窗口句柄，跳转
        driver.switch_to.window(driver.window_handles[-1])
        # 判断新增用户
        if self.valid_new_register():
            # 点击注册
            driver.find_element_by_css_selector("body > div.g-content.loading_hide > div.form-con.form-lg > form > div:nth-child(35) > div:nth-child(1) > input").click()
            driver.implicitly_wait(30)
            driver.close()
            driver.switch_to.window(driver.window_handles[-1])
        else:
            # 如果新增失败，返回列表
            print "问题！：", self.deprint()
            # 获取下一个窗口句柄，跳转
            print driver.window_handles[-1]
            driver.switch_to.window(driver.window_handles[-1])
    #验证注册信息
    def valid_new_register(self):
        # 邮箱
        driver.find_element_by_xpath('/html/body/div[3]/div[2]/form/div[3]/div[1]/input').send_keys('12@126.com')
        driver.implicitly_wait(30)

        mailError = driver.find_element_by_xpath('/html/body/div[3]/div[2]/form/div[3]/div[2]/p').text
        print u"服务器返回测错误信息" + mailError
        if mailError:
            print "出现问题"
            return False
        #密码
        driver.find_element_by_xpath('/html/body/div[3]/div[2]/form/div[9]/div[1]/input[1]').send_keys('123123')
        driver.implicitly_wait(30)

        mailError = driver.find_element_by_xpath('/html/body/div[3]/div[2]/form/div[9]/div[2]/p').text
        print u"服务器返回测错误信息" + mailError
        if mailError:
            print "出现问题 "
            return False
        return True



    """
    def OpenChrome(self):
        global driver

        curPath = os.path.abspath(os.path.dirname(__file__))
        print curPath
        rootPath = os.path.split(curPath)[0]
        print rootPath
        driver_path = rootPath+"\CommonFunction\chromedriver.exe"
        print driver_path
        driver = webdriver.Chrome(driver_path)
        driver.maximize_window()
        driver.get('https://uat-tenant.smarket.net.cn')

        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get('https://uat-tenant.smarket.net.cn')
        # driver.get('https://tenant.smarket.net.cn')


        driver.implicitly_wait(30)
    #关闭浏览器
    def closeChrome(self):
        driver.quit()
    """
    def create_offline(self):
        self.OpenChrome()
        self.login()
        self.clickUnderLine()
        self.createUnderLine()
        self.deprint()
    def offline_mange(self):
        self.OpenChrome()
        self.login()
        self.clickUnderLine()
        self.clicklist()
        self.interaction_link()
        self.creat_que()
    def ans_user(self):
        self.OpenChrome()
        self.login()
        self.clickUnderLine()
        self.clicklist()
        self.topicpage()
        self.sign_up()
        self.volume_ans()
        self.record_ver()

    """
    #当前时间 201804166
    def deprint(self):
        dt = datetime.now()
        strnow = datetime.strftime(dt, '%Y-%m-%d %H:%M:%S')
        return strnow
    """


if __name__ == "__main__":
    test = OffLineMeeting()

    # test.offline_mange()
    # test.ans_user()
    # test.all_line()
    test.create_offline()




