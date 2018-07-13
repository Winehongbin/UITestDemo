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
from pages.webinar_pages.base_page import Webinar_Webcast
t = BasePage(object)

class Webinar_Case(BaseUnit):
    """线上会测试用例（创建并取消会议，创建发布并取消会议，设置嘉宾日程及会议标签，设置问卷和抽奖，进入直播专题页）"""

    def test_001_webinar_create_cancel(self):
        """创建并取消会议"""
        t.deprint("开始执行线上会创建后取消的用例1")
        dr = brower()
        o = LoginPage(dr)
        o.login()
        o = ChoosePage(dr)
        o.click_menu_bt('8')
        time.sleep(5)
        # gguestnum = Get_Guestnum(dr)
        # guestnum = int(gguestnum.get_num())
        o = Webinar_IndexPage(dr)
        time.sleep(3)
        o.index_webinar()
        o.index_create()
        wbr = Webinar_Create(dr)
        wbr.create_meeting()
        wbr.cancel_meeting()
        o.quit()
        t.deprint("用例1执行完成")

    def test_002_webinar_publish_cancel(self):
        """创建发布并取消会议"""
        t.deprint("开始执行线上会创建后发布并取消的用例2")
        dr = brower()
        o = LoginPage(dr)
        o.login()
        o = ChoosePage(dr)
        o.click_menu_bt('8')
        time.sleep(5)
        o = Webinar_IndexPage(dr)
        time.sleep(3)
        o.webinar_list()
        o.list_create()
        wbr = Webinar_Create(dr)
        wbr.create_meeting()
        wbr.publish_meeting()
        wbr.cancel_meeting()
        o.quit()
        t.deprint("用例2执行完成")

    def test_003_meeting_addtag(self):
        """设置嘉宾日程及会议标签"""
        t.deprint("开始执行添加嘉宾和日程及会议标签的直播会议的用例3")
        dr = brower()
        o = LoginPage(dr)
        o.login()
        o = ChoosePage(dr)
        o.click_menu_bt('8')
        time.sleep(5)
        gguestnum = Get_Guestnum(dr)
        guestnum = int(gguestnum.get_num())
        o = Webinar_IndexPage(dr)
        o.webinar_list()
        wbr = Webinar_Create(dr)
        wbr.return_meeting()
        o.webinar_list()
        time.sleep(3)
        o.choose_meeting()
        wbr_seting = Webcast_Setting(dr)
        wbr_seting.into_baseinfo()
        wbr_seting.edit_baseinfo()
        wbr_seting.add_guest(guestnum)
        time.sleep(2)
        wbr_seting.add_agenda()
        wbr_seting.quit()
        t.deprint("用例3执行完成")

    def test_004_meeting_addquesluckydraw(self):
        """设置问卷和抽奖"""
        t.deprint("开始执行添加问卷和抽奖的直播会议的用例4")
        dr = brower()
        o = LoginPage(dr)
        o.login()
        o = ChoosePage(dr)
        o.click_menu_bt('8')
        time.sleep(5)
        o = Webinar_IndexPage(dr)
        o.webinar_list()
        o.choose_meeting()
        time.sleep(3)
        interact = InteractionSetting(dr)
        interact.interaction_setting()
        time.sleep(2)
        interact.create_questionnar()
        newquestion = NewQuestionnairePage(dr)
        newquestion.creat_new_questionnaire()
        newquestion.edit_questionnaire_subject()
        interact.click_refresh()
        time.sleep(2)
        interact.create_luckydraw()
        # wbr = Webinar_Create(dr)
        # wbr.cancel_meeting()
        interact.quit()
        t.deprint("用例4执行完成")

    def test_005_meeting_indexpage(self):
        """进入直播专题页"""
        t.deprint("开始执行进入会议专题页的用例5")
        dr = brower()
        o = LoginPage(dr)
        o.login()
        o = ChoosePage(dr)
        o.click_menu_bt('8')
        time.sleep(5)
        o = Webinar_IndexPage(dr)
        o.webinar_list()
        o.choose_meeting()
        time.sleep(3)
        index = Webinar_Webcast(dr)
        index.into_webcast()
        index.quit()
        t.deprint('用例5执行完成')



if __name__ == '__main__':
    start = time.time()
    suite = unittest.TestSuite()
    # 指定单个单元测试（ 需要配置运行方式才能走main函数，参考https://www.cnblogs.com/youreyebows/p/7867508.html）
    # suite.addTest(Webinar_Case("test_001_webinar_create_cancel"))
    # time.sleep(3)
    # suite.addTest(Webinar_Case("test_002_webinar_publish_cancel"))
    # time.sleep(3)
    suite.addTest(Webinar_Case("test_003_meeting_addtag"))
    suite.addTest(Webinar_Case("test_004_meeting_addquesluckydraw"))
    runner = unittest.TextTestRunner()
    runner.run(suite)