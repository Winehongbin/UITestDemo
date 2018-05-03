# -*- coding: utf-8 -*-

from selenium import webdriver
from pages.common_pages.base import BasePage
from pages.common_pages.login_page import LoginPage
import time
from pages.common_pages.choose_page import ChoosePage
from pages.common_pages.driver import brower

class creat_media(BasePage):


    def creat_media(self):

        self.refresh()

        self.find_element_click('x', '//*[@id="ul-nav-2"]/li[1]/a')

        # self.find_element_click(('x','//*[@id="con-graphic"]/div[1]/div[2]/div/a[2]')
        self.find_element_click('x', '//*[@id="con-graphic"]/div[1]/div[2]/div/a[2]')
        #
        #
        # self.find_element_input('x','//*[@id="exampleInputText1"]','自动化测试创建')
        # #输入图文标题
        # self.find_element_input('x','//*[@id="exampleInputText1"]','test')


if __name__ == '__main__':
    driver = brower()
    test = LoginPage(driver)
    test.login()
    test = ChoosePage(driver)
    test.click_menu_bt("1")
    test=creat_media(driver)
    test.creat_media()