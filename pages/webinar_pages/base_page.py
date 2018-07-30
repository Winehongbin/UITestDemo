# -*- coding:utf-8 -*-
from pages.common_pages.driver import brower
from pages.common_pages.base import BasePage
from pages.common_pages.login_page import LoginPage
from pages.common_pages.choose_page import ChoosePage
from pages.webinar_pages.index_page import Webinar_IndexPage
import time

class Webinar_Webcast(BasePage):
    # 进入会场
    def into_webcast(self,title):
        self.wait_is_visible('x','/html/body/div[1]/div[1]/div[1]/div[2]/div[1]/a[3]')
        time.sleep(3)
        # 跳转到直播会场的专题页
        self.driver.switch_to.window(self.driver.window_handles[-1])
        # 点击登录报名按钮
        self.wait_is_visible('x','/html/body/div[3]/div/div[3]')
        time.sleep(8)
        self.element_value_input('x','//*[@id="con_one_1"]/div[1]/input','18032890720')
        self.element_value_input('x','//*[@id="con_one_1"]/div[3]/input','123123')
        self.wait_is_visible('x','//*[@id="con_one_1"]/input')
        time.sleep(3)
        self.scrollbar('bottom')
        self.wait_is_visible('x','//*[@id="body-box"]/div[1]/div/div[2]/div[2]/input')
        self.deprint('进入直播会场')
        time.sleep(10)
        vtitle = self.find_element_text('x','//*[@id="mCSB_1_container"]/div[1]/div[2]/div[1]')
        time.sleep(5)
        # 判断进入的会场是否是打开的直播会议
        if vtitle == title :
            self.deprint('进入直播会场成功')
            return u'进入直播会场成功'
        else:
            self.deprint('进入直播会场失败')
            return u'进入直播会场失败'


if __name__ == '__main__':
    dr = brower()
    o = LoginPage(dr)
    o.login()
    o = ChoosePage(dr)
    time.sleep(3)
    o.click_menu_bt('8')
    o =  Webinar_IndexPage(dr)
    time.sleep(3)
    o.webinar_list()
    vtitle = o.choose_meeting()
    wc = Webinar_Webcast(dr)
    wc.into_webcast(vtitle)
    o.quit()
