# -*- coding: utf-8 -*-

from pages.common_pages.base import BasePage
from pages.webinar_pages.index_page import Webinar_IndexPage
from pages.common_pages.login_page import LoginPage
from pages.common_pages.driver import brower
from pages.common_pages.choose_page import ChoosePage
import time
from pages.webinar_pages.create_meeting import Webinar_Create
from pages.webinar_pages.webcast_setting import Webcast_Setting
from pages.webinar_pages.guest_manager import Get_Guestnum
import unittest
from test_case.base_unit import BaseUnit
from pages.webinar_pages.interaction_setting_page import InteractionSetting
from pages.questionnaire_page.new_questionnaire_page import NewQuestionnairePage
t = BasePage(object)

class Webinar_Case(BaseUnit):
# class Webinar_Case(BaseUnit):

    """线上会测试用例（创建线上会并取消会议、创建线上会，发布并取消会议、）"""

    def test_001_webinar_create_cancel(self):
        """创建线上会并取消会议"""
        t.deprint("开始执行线上会创建后取消的用例")
        dr = brower()
        o = LoginPage(dr)
        o.login()
        o = ChoosePage(dr)
        o.click_menu_bt('8')
        time.sleep(5)
        gguestnum = Get_Guestnum(dr)
        guestnum = int(gguestnum.get_num())
        o = Webinar_IndexPage(dr)
        time.sleep(3)
        o.index_webinar()
        wbr = Webinar_Create(dr)
        wbr.create_meeting()
        wbr_seting = Webcast_Setting(dr)
        wbr_seting.add_guest(guestnum)
        time.sleep(2)
        wbr_seting.add_agenda()
        time.sleep(2)
        question = InteractionSetting(dr)
        question.interaction_setting()
        time.sleep(2)
        question.create_questionnar()
        newquestion = NewQuestionnairePage(dr)
        newquestion.creat_new_questionnaire()
        newquestion.edit_questionnaire_subject()
        question.click_refresh()
        wbr.cancel_meeting()
        o.quit()
        t.deprint("创建并取消线上会用例执行完成")

    def test_002_webinar_publish_cancel(self):
        """创建线上会，发布并取消会议"""
        t.deprint("开始执行线上会创建后发布并取消的用例")
        dr = brower()
        o = LoginPage(dr)
        o.login()
        o = ChoosePage(dr)
        o.click_menu_bt('8')
        time.sleep(5)
        o = Webinar_IndexPage(dr)
        time.sleep(3)
        o.index_webinar()
        wbr = Webinar_Create(dr)
        wbr.create_meeting()
        wbr.publish_meeting()
        wbr.cancel_meeting()
        o.quit()
        t.deprint("创建，发布并取消线上会用例执行完成")

if __name__ == '__main__':
    start = time.time()
    suite = unittest.TestSuite()
    # 指定单个单元测试（ 需要配置运行方式才能走main函数，参考https://www.cnblogs.com/youreyebows/p/7867508.html）
    suite.addTest(Webinar_Case("test_001_webinar_create_cancel"))
    time.sleep(3)
    suite.addTest(Webinar_Case("test_002_webinar_publish_cancel"))
    runner = unittest.TextTestRunner()
    runner.run(suite)