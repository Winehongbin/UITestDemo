# -*- coding: utf-8 -*-

from pages.common_pages.base import BasePage
from pages.common_pages.driver import brower
import  time
from pages.common_pages.login_page import LoginPage
from pages.off_line_meeting_pages.index_page import IndexPage
from pages.common_pages.choose_page import ChoosePage


class InteractionAndCancle(BasePage):


    #互动环节添加操作
    def interaction_and_cancle(self,but_pos):
        time.sleep(15)
        self.driver.switch_to.window(self.driver.window_handles[-1])    #获取下一个窗口句柄，跳转
        # 点选“互动环节”
        print self.deprint(),":开始添加互动环节"
        self.driver.implicitly_wait(30)
        css_path = "/html/body/div[2]/div[2]/a[" + str(but_pos) + "]"  #按着元素位置对互动环节和取消会议两个元素进行判断
        self.wait_is_visible('x', css_path)
        if but_pos == '1':
            time.sleep(5)
            if self.driver.find_element_by_css_selector("#modulecheckbox6").is_selected():  #如果“互动环节”已经被选择
                self.driver.implicitly_wait(30)
                time.sleep(2)
                self.element_click('css','#setFiled > div > div > div.modal-footer > input')  #已经被选择，点击确定按钮
                self.driver.implicitly_wait(30)
                time.sleep(5)
                print self.deprint(), "：已添加互动环节"
            else:
                self.element_click('css','#setFiled > div > div > div.modal-body.ng-isolate-scope > div:nth-child(4) > div:nth-child(7) > label')
                self.driver.implicitly_wait(30)
                time.sleep(5)
                self.element_click('css','#setFiled > div > div > div.modal-footer > input')
                print self.deprint(),"：添加互动环节成功"
        if but_pos == '2':
            self.wait_is_visible('x','//*[@id="commonAlertWindow"]/div/div/div[3]/button')
            print self.deprint(), "：点击取消会议按钮"
        # self.close()
        print but_pos
if __name__ == "__main__":
    dr = brower()
    o = LoginPage(dr)
    o.login()
    o = ChoosePage(dr)
    o.click_menu_bt('9')
    o = IndexPage(dr)
    o.click_linelist('2')

    o = InteractionAndCancle(dr)
    o.interaction_and_cancle('2')