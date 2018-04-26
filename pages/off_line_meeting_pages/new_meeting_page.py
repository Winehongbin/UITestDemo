# -*- coding: utf-8 -*-
import time


from pages.common_pages.base import BasePage
from pages.common_pages.login_page import LoginPage
from pages.off_line_meeting_pages.index_page import IndexPage
from pages.common_pages.choose_page import ChoosePage
from pages.common_pages.driver import brower



class NewMeetingPage(BasePage):

    # 创建一场会议
    def create_neww_offline(self):
        print self.deprint(), ":开始创建线下会"
        ##创建新的会议页面
        # “会议名称”字段
        # 获取当前时间
        time_now = int(time.time())
        # 转换成localtime
        time_local = time.localtime(time_now)
        # 转换成新的时间格式(2016-05-09 18:59:20)
        dt = time.strftime("%Y-%m-%d %H:%M:%S", time_local)
        self.driver.find_element_by_id("seminarName").send_keys(u"自动化测试" + dt)
        # “会议时间”字段
        self.driver.find_element_by_id("seminarTime").click()
        handleNow = self.driver.current_window_handle
        self.driver.switch_to_window(handleNow)
        self.driver.find_element_by_name('daterangepicker_start').send_keys('2016-08-24')
        self.driver.find_element_by_name('daterangepicker_end').send_keys('2016-08-24')
        self.element_click('id','seminarTime')
        self.element_click('x','/html/body/div[4]/div[3]/div/button[1]')
        # “地区”字段,点击
        self.element_click('css','#createSeminarScroller > form > div:nth-child(5) > div > div > div:nth-child(1) > button')
        self.element_click('css','#createSeminarScroller > form > div:nth-child(5) > div > div > div.dropdown.r-select.select-ssmd.open > ul > li.ng-scope > a')
        self.driver.implicitly_wait(30)
        # "会议地点" 字段
        self.element_value_input('css','#createSeminarScroller > form > div:nth-child(6) > div > input',u'北京')
        # self.driver.find_element_by_css_selector("#createSeminarScroller > form > div:nth-child(6) > div > input").send_keys(
        #     u"北京")
        self.driver.implicitly_wait(30)

        # 选择不启用启用微信公众号
        self.element_click('css','#createSeminarScroller > form > div:nth-child(10) > div.col-md-2 > div > button > span')
        self.driver.implicitly_wait(10)
        self.element_click('css','#createSeminarScroller > form > div:nth-child(10) > div.col-md-2 > div > ul > li:nth-child(1) > a')
        self.driver.implicitly_wait(10)

        # 点击“创建”按钮
        self.element_click('css','#createSeminar > div > div > div.modal-footer > button')
        self.driver.implicitly_wait(30)
        # 201804166
        print self.deprint(), "：线下会创建成功"

if __name__ == '__main__':
    dr = brower()
    object = LoginPage(dr)
    object.login()

    object = ChoosePage(dr)
    object.click_menu_bt('9')

    object = IndexPage(dr)
    object.click_createunderline()
    object = NewMeetingPage(dr)
    object.create_neww_offline()
    # object.quit()