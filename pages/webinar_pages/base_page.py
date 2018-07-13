# -*- coding:utf-8 -*-
from pages.common_pages.driver import brower
from pages.common_pages.base import BasePage
from pages.common_pages.login_page import LoginPage
from pages.common_pages.choose_page import ChoosePage
from pages.webinar_pages.index_page import Webinar_IndexPage
import time

class Webinar_Webcast(BasePage):
    # 进入会场
    def into_webcast(self):
        self.wait_is_visible('x','/html/body/div[1]/div[1]/div[1]/div[2]/div[1]/a[3]')
        time.sleep(3)
        # 跳转到直播会场的专题页
        self.driver.switch_to.window(self.driver.window_handles[-1])

if __name__ == '__main__':
    dr = brower()
    o = LoginPage(dr)
    o.login()
