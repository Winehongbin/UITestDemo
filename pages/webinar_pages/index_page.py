# -*- coding: utf-8 -*-
from pages.common_pages.base import BasePage
from pages.common_pages.login_page import LoginPage
import time
from pages.common_pages.choose_page import ChoosePage
from pages.common_pages.driver import brower
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Webinar_IndexPage(BasePage):

    # 打开线上会的首页
    def index_webinar(self):
        self.deprint("进入线上会首页")
        # self.wait_is_visible('x','/html/body/div[1]/div[1]/ul/li[1]/h2/a')
        element = WebDriverWait(self.driver,10,0.5).until(EC.presence_of_all_elements_located((By.XPATH,'/html/body/div[1]/div[1]/ul/li[1]/h2/a')))
        # print element
        if element == 1 :
            self.wait_is_visible('x','/html/body/div[1]/div[1]/ul/li[1]/h2/a')
        else:
            time.sleep(2)
            self.wait_is_visible('x', '/html/body/div[1]/div[1]/ul/li[1]/h2/a')

if __name__ == '__main__':
    dr = brower()
    o = LoginPage(dr)
    o.login()
    o = ChoosePage(dr)
    time.sleep(3)
    o.click_menu_bt('8')
    o =  Webinar_IndexPage(dr)
    time.sleep(3)
    o.index_webinar()




