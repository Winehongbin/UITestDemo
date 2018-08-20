# -*- coding: utf-8 -*-

import time
from pages.common_pages.base import BasePage
from pages.common_pages.login_page import LoginPage
from pages.common_pages.choose_page import ChoosePage
from pages.common_pages.driver import brower
from pages.management_tools.article_pages.section_list_page import SectionListPage


class BrowsePage(BasePage):

    # 浏览栏目
    def browse_section(self):
        self.driver.switch_to_window(self.driver.window_handles[-1])  # 移动句柄，对新打开页面进行操作

        try:
            # self.deprint("开始浏览栏目")
            o = SectionListPage(dr)
            time.sleep(3)
            # current_handle = self.driver.current_window_handle
            # all_handles = self.driver.window_handles
            # url = o.choose_more().encode('unicode-escape').decode('string_escape')
            url = o.choose_more()
                # .encode('unicode-escape').decode("utf-8")
            # url = self.driver.find_element_by_css_selector(
            #     'body > div.g-container-box > div.m-container.ng-scope > div.clearfix.ng-scope > div.vote-link-box > form > div:nth-child(1) > div > input').get_attribute(
            #     "value")

            print url
            newwindow = 'window.open("' + url + '")'
            print newwindow
            # newwindow = 'window.open(" + url + ")'
            self.driver.execute_script(newwindow)
            self.driver.switch_to_window(self.driver.window_handles[-1]) # 移动句柄，对新打开页面进行操作
            time.sleep(3)
            self.deprint("完成浏览栏目")
            time.sleep(3)
            self.driver.close()
            # # for handle in all_handles:
            # #     if handle == current_handle:
            # #         self.driver.switch_to_window(handle)
            # #         # self.driver.switch_to_window(self.driver.window_handles[1])
            # time.sleep(5)
        except:
            self.deprint("浏览栏目失败")
        """

        pc_url = self.driver.find_element_by_css_selector(
            'body > div.g-container-box > div.m-container.ng-scope > div.clearfix.ng-scope > div.vote-link-box > form > div:nth-child(1) > div > input').get_attribute(
            "value")
        print 'pc_url:' + pc_url
        # 新打开一个一个浏览
        # 浏览器 新窗口打开连接
        newwindow = 'window.open("' + pc_url + '")'
        print newwindow
        driver.execute_script(newwindow)
        # 移动句柄，对新打开页面进行操作
        driver.switch_to.window(driver.window_handles[-1])
         """

if __name__ == '__main__':
    dr = brower()
    object = LoginPage(dr)
    object.login()
    object = ChoosePage(dr)
    object.click_menu_bt('22')
    o=SectionListPage(dr)
    o.new_section()
    # o.choose_more()
    o = BrowsePage(dr)
    o.browse_section()
    time.sleep(3)
    o=SectionListPage(dr)
    o.open_detail_data()

