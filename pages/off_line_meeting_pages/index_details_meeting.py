# -*- coding: utf-8 -*-
from pages.common_pages.base import BasePage
from pages.common_pages.login_page import LoginPage
from pages.common_pages.choose_page import ChoosePage
from pages.common_pages.driver import brower
from pages.off_line_meeting_pages.index_page import IndexPage
from pages.off_line_meeting_pages.interaction_manage_page import InteractionPageManage
# from pages.off_line_meeting_pages.interaction_link_page import Interaction_Line
import time

class IndexDetailsOfMeeting(BasePage):


    # 点击互动环节菜单
    def click_interaction(self):
        self.deprint("点击互动环节菜单")
        self.driver.switch_to.window(self.driver.window_handles[-1])  # 获取下一个窗口句柄，跳转
        self.wait_is_visible('x','/html/body/div[2]/div[2]/ul[2]/li[6]')
        self.driver.implicitly_wait(30)
        self.deprint("进入互动环节页面")

        # 点击会议详情列表页面的列表按钮#20180807

    def click_indexname(self, button_num):
        x_path = "/html/body/div[2]/div[2]/ul[2]/li[" + str(button_num) + "]/a"  # 把按钮位置设为参数获取
        print type(x_path)
        if button_num == '11':
            self.deprint("进入邮件任务页面")
        if button_num == '12':
            self.deprint("进入短信任务页面")
        if button_num == '4':
            self.deprint("进入报名表单页面")

        # self.scrollbar("bottom")
        # # 下面的两句是将鼠标拖动到指定元素可见为止
        # target = self.driver.find_element_by_xpath(x_path)

        # self.driver.execute_script("arguments[0].scrollIntoView();", target)  # 拖动到可见的元素去
        time.sleep(5)
        self.scrollbar("200")
        time.sleep(5)
        self.wait_is_visible('x', x_path)


if __name__ == '__main__':
    dr = brower()
    o = LoginPage(dr)
    o.login()
    o = ChoosePage(dr)
    o.click_menu_bt('9')
    o = IndexPage(dr)
    o.click_linelist()
    o = Interaction_Line(dr)
    o.interaction_link()
    o = InteractionPageManage(dr)
    o.creat_questionnaire()
    o = IndexDetailsOfMeeting(dr)
    o.click_interaction()

