# -*- coding: utf-8 -*-
from pages.common_pages.base import BasePage
from pages.common_pages.driver import brower
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    def login(self):
        self.open()
        self.driver.implicitly_wait(30)
        # self.find_element_input('x','/html/body/div[2]/div/div/div[1]/form/div[1]/input','18210127910')
        self.find_element_input('x','//*[@id="login"]/form/div[1]/input','18210127910')

        # self.find_element_input('css',"input[type='password']","123123")
        #点击登录按钮
        self.element_click('x','/html/body/div[2]/div/div/div[1]/form/input')
        self.driver.implicitly_wait(30)

if __name__ == '__main__':
    dr = brower()
    o = LoginPage(dr)
    o.login()
