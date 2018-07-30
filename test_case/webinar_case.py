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
    """线上会测试用例（创建并取消会议，创建发布并取消会议，设置嘉宾日程及会议标签，进入直播会场）"""

    def test_001_webinar_create_cancel(self):
        """创建并取消会议"""
        t.deprint("开始执行线上会创建后取消的用例1")
        dr = brower()
        o = LoginPage(dr)
        o.login()
        o = ChoosePage(dr)
        o.click_menu_bt('8')
        time.sleep(5)
        o = Webinar_IndexPage(dr)
        time.sleep(3)
        o.index_webinar() # 进入线上会首页
        o.index_create() # 点击首页的创建会议按钮
        wbr = Webinar_Create(dr)
        wbr.create_meeting() # 创建线上会直播会议
        actual_result = wbr.cancel_meeting() # 取消此会议
        self.assertEqual(actual_result,u'会议取消成功',msg='failed')
        o.quit()
        # t.deprint("用例1执行完成")

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
        o.webinar_list() # 进入线上会直播会议列表
        o.list_create() # 点击线上会直播列表的创建会议按钮
        wbr = Webinar_Create(dr)
        wbr.create_meeting() # 创建直播会议
        actual_result = wbr.publish_meeting() # 发布本会议
        self.assertEqual(actual_result,u'会议发布成功',  msg='failed')
        actual_result1 = wbr.cancel_meeting() # 取消本会议
        self.assertEqual( actual_result1,u'会议取消成功', msg='failed')
        o.quit()
        # t.deprint("用例2执行完成")

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
        guestnum = int(gguestnum.get_num()) # 获取嘉宾管理的嘉宾个数
        o = Webinar_IndexPage(dr)
        o.webinar_list() # 进入直播会议列表
        wbr = Webinar_Create(dr)
        wbr.return_meeting() # 进入直播会议回收站还原会议
        o.webinar_list() # 进入直播会议列表
        time.sleep(3)
        o.choose_meeting() # 选择一场直播中的会议
        wbr_seting = Webcast_Setting(dr)
        wbr_seting.into_baseinfo() # 进入会议详情的基础设置页面
        wbr_seting.edit_baseinfo() # 编辑会议的基本信息
        actual_result1 = wbr_seting.add_guest(guestnum) # 添加会议嘉宾
        # self.assertEqual('嘉宾信息成功',actual_result1,msg='failed')
        # time.sleep(2)
        actual_result2 = wbr_seting.add_agenda() # 添加会议日程
        self.assertEqual(actual_result2,u'添加会议日程成功',msg='failed')
        wbr_seting.quit()
        # t.deprint("用例3执行完成")

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
        acture_result=interact.create_luckydraw()
        except_result="抽奖添加成功"
        # wbr = Webinar_Create(dr)
        # wbr.cancel_meeting()
        self.assertEqual(acture_result,except_result,"fail")
        # self.assertTupleEqual(acture_result,except_result,"fail")
        t.deprint("用例4执行完成")

    def test_005_meeting_indexpage(self):
        """进入直播专题页"""
        t.deprint("开始执行进入直播会场的用例5")
        dr = brower()
        o = LoginPage(dr)
        o.login()
        o = ChoosePage(dr)
        o.click_menu_bt('8')
        time.sleep(5)
        o = Webinar_IndexPage(dr)
        o.webinar_list() # 进入直播会议的列表
        vtitle = o.choose_meeting() # 获取一场直播中会议的会议标题
        time.sleep(3)
        index = Webinar_Webcast(dr)
        actual_result1 = index.into_webcast(vtitle) # 进入直播会议会场，并验证会议标题
        self.assertEqual(actual_result1,u'进入直播会场成功',msg='failed')
        index.quit()
        # t.deprint('用例5执行完成')



if __name__ == '__main__':
    start = time.time()
    suite = unittest.TestSuite()
    # 指定单个单元测试（ 需要配置运行方式才能走main函数，参考https://www.cnblogs.com/youreyebows/p/7867508.html）
    # suite.addTest(Webinar_Case("test_001_webinar_create_cancel"))
    # time.sleep(3)
    # suite.addTest(Webinar_Case("test_002_webinar_publish_cancel"))
    # time.sleep(3)
    suite.addTest(Webinar_Case("test_001_webinar_create_cancel"))
    # suite.addTest(Webinar_Case("test_002_webinar_publish_cancel"))
    #
    # suite.addTest(Webinar_Case("test_003_meeting_addtag"))
    #
    # suite.addTest(Webinar_Case("test_005_meeting_indexpage"))
    # suite.addTest(Webinar_Case("test_004_meeting_addquesluckydraw"))
    # suite.addTest(Webinar_Case("test_005_meeting_indexpage"))
    runner = unittest.TextTestRunner()
    runner.run(suite)