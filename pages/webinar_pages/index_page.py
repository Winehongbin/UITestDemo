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
            time.sleep(3)
            self.wait_is_visible('x', '/html/body/div[1]/div[1]/ul/li[1]/h2/a')

    # 进入直播会议列表页面
    def webinar_list(self):
        self.deprint("进入直播会议列表页面")
        time.sleep(2)
        # 点击直播菜单
        self.wait_is_visible('x','//*[@id="collapse2"]/li[1]/a')

    # 点击直播列表页面的创建会议按钮
    def list_create(self):
        self.deprint("点击直播列表创建会议按钮")
        self.wait_is_visible('x','/html/body/div[1]/div[2]/div/div[2]/button')
        time.sleep(5)

    # 点击首页的创建会议按钮
    def index_create(self):
        self.deprint("点击首页创建会议按钮")
        self.wait_is_visible('x', '/html/body/div[1]/div[2]/div/button')
        time.sleep(3)

    # 选择直播会议
    def choose_meeting(self):
        self.deprint('选择一场直播中的会议')
        time.sleep(3)
        for i in range(1,5):
            status1 = self.find_element_text('x','/html/body/div[1]/div[2]/div/section/ul/li['+str(i)+']/div/div[2]/p[1]/span[2]')
            self.deprint(status1)
            if status1 == u'直播中' :
                wtitle = self.find_element_text('x', '/html/body/div[1]/div[2]/div/section/ul/li[' + str(i) + ']/div/div[2]/p[1]/span[1]')
                self.wait_is_visible('x','/html/body/div[1]/div[2]/div/section/ul/li['+str(i)+']/div/a')
                self.deprint('进入直播中的会议的详情页面')
                break
            else:
                continue
        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.driver.implicitly_wait(10)
        return wtitle

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
    o.choose_meeting()
    o.quit()




