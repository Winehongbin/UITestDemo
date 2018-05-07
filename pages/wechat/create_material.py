# -*- coding: utf-8 -*-
import os

from selenium import webdriver
from pages.common_pages.base import BasePage
from pages.common_pages.login_page import LoginPage
import time
from pages.common_pages.choose_page import ChoosePage
from pages.common_pages.driver import brower

class creat_media(BasePage):
    def creat_media(self):
        self.dominant_wait('x', '//*[@id="ul-nav-2"]/li[1]/a')
        time.sleep(3)
        self.dominant_wait('x','//*[@id="con-graphic"]/div[1]/div[2]/div/a[2]')
        print self.printime(),u'点击新建图文按钮成功'
        self.find_element_input('x','//*[@id="exampleInputText1"]',u'自动化创建'+self.deprint())
        self.find_element_click('x','//*[@id="con-local"]/section/section/div[2]/form/div[1]/div[4]/div[3]/div')
        pic=os.getcwd()
        print pic
        os.system(pic +  "/upload.exe")
        self.find_element_input('x','//*[@id="con-local"]/section/section/div[2]/form/div[1]/div[6]/textarea',u'尤梅枝的摘要'+self.deprint())
        # self.find_element_click('x','.//*[@id="con-local"]/section/section[1]/div[2]/form/div[1]/div[9]/div[2]')
        self.find_element_input('x','//*[@id="exampleInputText2"]','http://www.baidu.com')
        self.find_element_click('x','//*[@id="con-local"]/section/section/div[2]/form/div[2]/button[1]')
        time.sleep(5)
        title=self.driver.find_element_by_xpath('//*[@id="dialogBox"]/div/div/div[2]/div/div').text
        self.find_element_click('x','//*[@id="dialogBox"]/div/div/div[3]/button[1]')
        print title
        return title

if __name__ == '__main__':
    driver = brower()
    test = LoginPage(driver)
    test.login()
    test = ChoosePage(driver)
    test.click_menu_bt("1")
    test=creat_media(driver)
    test.creat_media()