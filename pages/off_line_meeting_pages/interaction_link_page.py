# -*- coding: utf-8 -*-

from pages.common_pages.base import BasePage
from pages.common_pages.driver import brower
import  time
from pages.common_pages.login_page import LoginPage
from pages.off_line_meeting_pages.index_page import IndexPage
from pages.common_pages.choose_page import ChoosePage


class Interaction_Line(BasePage):


    #互动环节操作
    def interaction_link(self):
        time.sleep(15)
        #获取下一个窗口句柄，跳转
        self.driver.switch_to.window(self.driver.window_handles[-1])
        # 点选“互动环节”
        print self.deprint(),":开始添加互动环节"
        self.driver.implicitly_wait(30)
        self.element_click("x","/html/body/div[2]/div[2]/a[1]")
        self.driver.implicitly_wait(30)
        time.sleep(3)
        # 点击确定
        if self.driver.find_element_by_css_selector("#modulecheckbox6").is_selected():
            self.driver.implicitly_wait(30)
            time.sleep(2)
            self.element_click('css','#setFiled > div > div > div.modal-footer > input')
            self.driver.implicitly_wait(30)
            time.sleep(5)
        else:
            self.element_click('css','#setFiled > div > div > div.modal-body.ng-isolate-scope > div:nth-child(4) > div:nth-child(7) > label')
            self.driver.implicitly_wait(30)
            time.sleep(5)
            self.element_click('css','#setFiled > div > div > div.modal-footer > input')
        print self.deprint(),"：添加互动环节成功"

if __name__ == "__main__":
    dr = brower()
    o = LoginPage(dr)
    o.login()
    o = ChoosePage(dr)
    o.click_menu_bt('9')
    o = IndexPage(dr)
    o.click_linelist()

    o = Interaction_Line(dr)
    o.interaction_link()