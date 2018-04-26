# -*- coding: utf-8 -*-
from pages.common_pages.base import BasePage
from pages.common_pages.driver import brower


class LoginPage(BasePage):
    def login(self):
        self.open()
        self.driver.find_element_by_xpath("/html/body/div[2]/div/div/div[1]/form/div[1]/input").send_keys("18210127910")
        self.driver.find_element_by_css_selector("input[type='password']").send_keys('123123')
        self.element_click('x','/html/body/div[2]/div/div/div[1]/form/input')
        self.driver.implicitly_wait(30)

if __name__ == '__main__':
    dr = brower()
    o = LoginPage(dr)
    o.login()
