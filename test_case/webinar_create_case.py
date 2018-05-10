# -*- coding: utf-8 -*-

from pages.common_pages.base import BasePage
from pages.webinar_pages.index_page import Webinar_IndexPage
from pages.common_pages.login_page import LoginPage
from pages.common_pages.driver import brower
from pages.common_pages.choose_page import ChoosePage
import time
from pages.webinar_pages.create_meeting import Webinar_Create
from pages.webinar_pages.Webcast_Setting import Webcast_Setting


import unittest
from test_case.base_unit import BaseUnit
t = BasePage(object)

class Webinar_Case(BaseUnit):

    """线上会测试用例"""

    def test_001_webinar_create_cancle(self):
        # 创建线上会并取消会议
        print t.deprint(), ":开始执行线上会创建后取消的用例"
        dr = brower()
        o = LoginPage(dr)
        o.login()
        o = ChoosePage(dr)
        time.sleep(3)
        o.click_menu_bt('8')
        o = Webinar_IndexPage(dr)
        time.sleep(3)
        o.index_webinar()
        wbr = Webinar_Create(dr)
        wbr.create_meeting()
        wbr.cancel_meeting()
        print t.deprint("创建并取消线上会用例执行完成")

    def test_002_webinar_publish_cancle(self):
        # 创建线上会，发布并取消会议
        print t.deprint("开始执行线上会创建后发布并取消的用例")
        dr = brower()
        o = LoginPage(dr)
        o.login()
        o = ChoosePage(dr)
        time.sleep(3)
        o.click_menu_bt('8')
        o = Webinar_IndexPage(dr)
        time.sleep(3)
        o.index_webinar()
        wbr = Webinar_Create(dr)
        wbr.create_meeting()
        wbr.publish_meeting()
        wbr.cancel_meeting()
        print t.deprint("创建，发布并取消线上会用例执行完成")



if __name__ == '__main__':
    start = time.time()
    suite = unittest.TestSuite()
    # 指定单个单元测试（ 需要配置运行方式才能走main函数，参考https://www.cnblogs.com/youreyebows/p/7867508.html）
    suite.addTest(Webinar_Case("test_001_webinar_create_cancle"))
    suite.addTest(Webinar_Case("test_002_webinar_publish_cancle"))