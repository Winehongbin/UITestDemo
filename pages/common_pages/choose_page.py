# -*- coding: utf-8 -*-
import time
from pages.common_pages.base import BasePage
from pages.common_pages.driver import brower
from pages.common_pages.login_page import LoginPage
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ChoosePage(BasePage):
    #点击首页菜单中的线下会按钮
    def click_menu_bt(self, button_pos):

        time.sleep(3)
        handleNow = self.driver.current_window_handle # 获得当前窗口
        self.driver.switch_to_window(handleNow)
        self.driver.implicitly_wait(30)
        print self.deprint(), u":开始进入线下会"
        css_path = "#sortContainer > a:nth-child(" + str(button_pos) + ")"
        self.wait_is_visible('css',css_path)
        time.sleep(3)
        self.driver.switch_to.window(self.driver.window_handles[-1]) # 获取下一个窗口句柄，跳转
        print self.deprint(), u":正常进入线下会"

if __name__ == '__main__':
    dr = brower()
    o = LoginPage(dr)
    o.login()
    o = ChoosePage(dr)
    time.sleep(3)
    o.click_menu_bt('9')
    # o.quit()