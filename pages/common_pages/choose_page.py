# -*- coding: utf-8 -*-
import time

from pages.common_pages.base import BasePage

from pages.common_pages.driver import brower
from pages.common_pages.login_page import LoginPage


class ChoosePage(BasePage):


    #点击首页菜单中的线下会按钮
    def click_menu_bt(self, button_pos):

        print self.deprint(), u":开始进入线下会"
        # 获得当前窗口
        handleNow = self.driver.current_window_handle
        self.driver.switch_to_window(handleNow)
        time.sleep(15)
        # 点击线下会
        #css_path = "#sortContainer > a:nth-child(" + button_pos + ")"
        css_path = "#sortContainer > a:nth-child(" + str(button_pos) + ")"
        self.driver.find_element_by_css_selector(css_path).click()

        self.driver.implicitly_wait(30)
        time.sleep(8)
        # 获取下一个窗口句柄，跳转
        self.driver.switch_to.window(self.driver.window_handles[-1])
        print self.deprint(), u":正常进入线下会"

if __name__ == '__main__':
    dr = brower()
    o = LoginPage(dr)
    o.login()
    o = ChoosePage(dr)
    o.click_menu_bt('9')
    # o.quit()