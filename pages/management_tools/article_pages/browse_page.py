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
        try:
            # self.deprint("开始浏览栏目")
            o = SectionListPage(dr)
            time.sleep(3)
            current_handle = self.driver.current_window_handle
            all_handles = self.driver.window_handles
            url = o.choose_more().encode('unicode-escape').decode('string_escape')
            newwindow = 'window.open("' + url + '")'
            self.driver.execute_script(newwindow)
            self.deprint("完成浏览栏目")
            time.sleep(3)
            # self.driver.close()
            for handle in all_handles:
                if handle == current_handle:
                    self.driver.switch_to_window(handle)
                    # self.driver.switch_to_window(self.driver.window_handles[1])
        except:
            self.deprint("浏览栏目失败")


if __name__ == '__main__':
    dr = brower()
    object = LoginPage(dr)
    object.login()
    object = ChoosePage(dr)
    object.click_menu_bt('22')
    o=SectionListPage(dr)
    o.new_section()
    o.choose_more()
    o = BrowsePage(dr)
    o.browse_section()
    o=SectionListPage(dr)
    o.open_detail_data()

