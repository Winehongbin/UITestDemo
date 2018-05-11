# -*- coding: utf-8 -*-
import time
import sys
from pages.common_pages.driver import brower
reload(sys)  #在解释器里修改的编码只能保证当次有效，在重启解释器后，会发现，编码又被重置为默认的ascii了
sys.setdefaultencoding('utf8')

from pages.common_pages.base import BasePage
from pages.common_pages.login_page import LoginPage
from pages.off_line_meeting_pages.index_page import IndexPage
from pages.common_pages.choose_page import ChoosePage
from pages.common_pages.driver import brower



class NewMeetingPage(BasePage):

    # 创建一场会议
    def create_neww_offline(self,form_name):
        self.deprint("开始创建线下会")
        time_now = int(time.time()) # 获取当前时间
        time_local = time.localtime(time_now) # 转换成localtime
        dt = time.strftime("%Y-%m-%d %H:%M:%S", time_local)   #strftime：转换成新的时间格式(2016-05-09 18:59:20)
        self.driver.find_element_by_id("seminarName").send_keys(u"自动化测试" + dt)
        self.driver.find_element_by_id("seminarTime").click()         # “会议时间”字段
        handleNow = self.driver.current_window_handle
        self.driver.switch_to_window(handleNow)
        self.driver.find_element_by_name('daterangepicker_start').send_keys('2016-08-24')   #“会议时间”开始时间
        self.driver.find_element_by_name('daterangepicker_end').send_keys('2016-08-24')  #“会议时间”结束时间
        self.element_click('id','seminarTime')
        self.element_click('x','/html/body/div[4]/div[3]/div/button[1]')
        self.element_click('css','#createSeminarScroller > form > div:nth-child(5) > div > div > div:nth-child(1) > button')  # “地区”字段,点击
        self.element_click('css','#createSeminarScroller > form > div:nth-child(5) > div > div > div.dropdown.r-select.select-ssmd.open > ul > li.ng-scope > a')
        self.driver.implicitly_wait(30)
        self.element_value_input('css','#createSeminarScroller > form > div:nth-child(6) > div > input',u'北京')  # "会议地点" 字段
        self.nameofform(u"新建注册表单(9)")
        self.driver.implicitly_wait(30)
        self.element_click('css','#createSeminarScroller > form > div:nth-child(10) > div.col-md-2 > div > button > span') # 选择不启用启用微信公众号
        self.driver.implicitly_wait(10)
        self.element_click('css','#createSeminarScroller > form > div:nth-child(10) > div.col-md-2 > div > ul > li:nth-child(1) > a')
        self.driver.implicitly_wait(10)
        self.element_click('css','#createSeminar > div > div > div.modal-footer > button')         # 点击“创建”按钮
        self.driver.implicitly_wait(30)
        self.deprint( "线下会创建成功"),

    def nameofform(self, form_name):

        #点击选择
        self.element_click('x', '//*[@id="createSeminarScroller"]/form/div[8]/div[2]/div/button/span')

        for num in range(1, 100):  #遍历选项，选中form_name 因为遍历100遍，及100个下表元素。如果没有正确选中，很有可能找不到元素，报错。
            ele = '//*[@id="createSeminarScroller"]/form/div[8]/div[2]/div/ul/li[' + str(num) + ']/a'
            print ele
            all_form_name = self.find_element_text("x", ele)  # 获各个注册单名称
            print all_form_name
            if all_form_name == form_name:  # 判断对应注册单的名称，点击选择
                self.element_click("x", ele)
                break


if __name__ == '__main__':
    dr = brower()
    object = LoginPage(dr)
    object.login()

    object = ChoosePage(dr)
    object.click_menu_bt('9')

    object = IndexPage(dr)
    object.click_createunderline()
    object = NewMeetingPage(dr)
    # object.nameofform(u"新建注册表单(9)")
    object.create_neww_offline(u"新建注册表单(9)")

    # object.quit()