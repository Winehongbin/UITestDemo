# -*- coding: utf-8 -*-
# 用于奥点云uat测试
from test_case.base_unit import BaseUnit
from pages.common_pages.base import BasePage
from pages.common_pages.login_page import LoginPage
from pages.common_pages.choose_page import ChoosePage
from pages.webinar_pages.index_page import Webinar_IndexPage
import time,unittest
from pages.webinar_pages.create_meeting import Webinar_Create
from pages.webinar_pages.interaction_setting_page import InteractionSetting
from pages.questionnaire_page.new_questionnaire_page import NewQuestionnairePage
from pages.webinar_pages.enter_meeting import enter_meeting

base = BasePage(object)
class ADY(BaseUnit):
    """奥点云uat测试用例"""

    # def test_001_RecordTime(self):
    #     """ 测试验证线上会老用户登陆会场，记录其参会时长 """
    #     dr=self.driver
    #     base.deprint("开始执行登陆操作")
    #     LoginPage(dr).login_uat()
    #     base.deprint("开始执行选择线上会操作")
    #     ChoosePage(dr).click_menu_bt("9")
    #     time.sleep(5)
    #     base.deprint("开始执行线上会建会操作")
    #     o = Webinar_IndexPage(dr)
    #     time.sleep(3)
    #     o.index_webinar()  # 进入线上会首页
    #     o.index_create()  # 点击首页的创建会议按钮
    #     wbr = Webinar_Create(dr)
    #     current_handle=wbr.create_meeting("2")  # 创建线上会直播会议
    #     base.deprint("开始发布会议")
    #     wbr.publish_meeting()
    #     base.deprint("点击进入会场操作")
    #     wbr.enter_meenting()
    #     base.deprint("开始执行登陆报名操作")
    #     o.login_meeting()
    #     base.deprint("开始验证该用户的参会时长")
    #     o.switch_window(current_handle)
    #     base.deprint("点击详细数据页面")
    #     text=o.detail_data()
    #     except_result="pc"
    #     self.assertEqual(text,except_result,'fail')
    # def test_002_fobidden(self):
    #     """会中互动禁言用户"""
    #     dr = self.driver
    #     base.deprint("开始执行登陆操作")
    #     LoginPage(dr).login_uat()
    #     base.deprint("开始执行选择线上会操作")
    #     ChoosePage(dr).click_menu_bt("9")
    #     time.sleep(5)
    #     base.deprint("开始执行线上会建会操作")
    #     o = Webinar_IndexPage(dr)
    #     time.sleep(3)
    #     o.index_webinar()  # 进入线上会首页
    #     o.index_create()  # 点击首页的创建会议按钮
    #     wbr = Webinar_Create(dr)
    #     current_handle = wbr.create_meeting("2")  # 创建线上会直播会议
    #     base.deprint("开始发布会议")
    #     wbr.publish_meeting()
    #     base.deprint("点击进入会场操作")
    #     wbr.enter_meenting()
    #     base.deprint("开始执行登陆报名操作")
    #     currnet_handle1=o.login_meeting()
    #     base.deprint("开始发表评论")
    #     o.publiccomment()
    #     base.deprint("切换到会议详情页面并刷新")
    #     o.switch_window(current_handle)
    #     base.deprint("点击进入会中互动按钮")
    #     o.enter_meeting_hd()
    #     base.deprint("点击互动问答按钮")
    #     o.Click_hdButton()
    #     base.deprint("点击禁言按钮")
    #     current_handle2=o.Click_JYButton()
    #     base.deprint("回到线上会页面，再次发言")
    #     o.return_offmeeting(currnet_handle1,'test')
    #     base.deprint("切换到互动页面页面并刷新")
    #     o.switch_window(current_handle2)
    #     base.deprint("循环遍历所有的li中没有刚刚的发言内容test即可")
    #     JYtext=o.XHBL_content("1")
    #     JJtext=""
    #     except_result="success"
    #     if JYtext=="success":
    #         base.deprint("将该用户解禁")
    #         o.Click_JJButton()
    #         base.deprint("再次跳转进会中页面")
    #         o.return_offmeeting(currnet_handle1, 'hello')
    #         base.deprint("切换到互动环节页面并刷新")
    #         o.switch_window(current_handle2)
    #         base.deprint("循环遍历所有的li中有刚刚的发言内容hello即可")
    #         JJtext = o.XHBL_content("2")
    #         print "JJtext:",JJtext
    #     self.assertEqual(JJtext,except_result,'fail')
    def test_003_newcustom(self):
        """新注册用户参会，并参与投票，问卷，抽奖"""
        dr = self.driver
        base.deprint("开始执行登陆操作")
        LoginPage(dr).login_uat()
        base.deprint("开始执行选择线上会操作")
        ChoosePage(dr).click_menu_bt("9")
        time.sleep(5)
        base.deprint("开始执行线上会建会操作")
        o = Webinar_IndexPage(dr)
        time.sleep(3)
        o.index_webinar()  # 进入线上会首页
        o.index_create()  # 点击首页的创建会议按钮
        wbr = Webinar_Create(dr)
        current_handle = wbr.create_meeting("2")  # 创建线上会直播会议
        base.deprint("开始发布会议")
        wbr.publish_meeting()
        base.deprint("开始设置问卷")
        interact = InteractionSetting(dr)
        current_handle = interact.interaction_setting()
        time.sleep(2)
        interact.create_questionnar()
        newquestion = NewQuestionnairePage(dr)
        newquestion.creat_new_questionnaire()
        newquestion.edit_questionnaire_subject()
        time.sleep(2)
        base.deprint("开始添加抽奖")
        interact.Close_AndRefresh()
        interact.create_luckydraw()
        base.deprint("开始创建投票")
        interact.Close_AndRefresh()
        interact.create_vote()
        interact.Edit_vote()
        base.deprint("开始添加文件")
        interact.Close_AndRefresh()
        interact.Add_File()
        base.deprint("开始刷新当前页面，并将问卷设置为默认")
        interact.click_refresh(current_handle)
        base.deprint("进入会中互动，将投票等信息设置为发布")
        entermeet=enter_meeting(dr)
        entermeet.Click_entermeeting()
        base.deprint("开始发布投票")
        entermeet.Public_Vote()
        base.deprint("开始回到会议详情页面，点击刷新按钮")
        interact.refresh_meeting(current_handle)
        base.deprint("开始点击进入会场按钮")
        wbr.enter_meenting()
        base.deprint("开始执行注册操作")
        o.login_newcustom()
        base.deprint("开始点击投票的提交按钮")
        o.Click_VoteCommitBut()
        base.deprint("开始点击会上的问卷按钮")
        meeting_handle=o.Click_QuestButton()
        base.deprint("开始点击文件下载按钮")
        o.Click_FileDown()
        base.deprint("开始验证抽奖")
        o.Is_Quark()
        base.deprint("切换到会中页面，查看是否中奖")
        o.Is_TrueQuark(meeting_handle)
        base.deprint("切换到会议详情信息页面，查看参会人员登陆记录")
        acture_result =o.Get_EnterMeeting(current_handle)
        except_result="success"
        self.assertEqual(acture_result,except_result,"fail")
if __name__ == '__main__':
    # StartTime = time.time()
    # suite = unittest.TestSuite()
    # # 指定单个单元测试（ 需要配置运行方式才能走main函数，参考https://www.cnblogs.com/youreyebows/p/7867508.html）
    # suite.addTest(ADY("test_004"))
    # # suite.addTest(Offline_Meeting_Test("test_002_interaction"))
    # # suite.addTest(Offline_Meeting_Test("test_003_createoffline"))
    #
    #
    # # 执行单元测试，生成报告
    # AddSuite = report.AllReport()
    # AddSuite.onlyneed_suite(suite)
    #
    # # 发送邮件
    # EndTime = time.time()
    # PerformTime = EndTime - StartTime
    # content = "test_createoffline"
    #
    # # SendEmail = email.SendEmailModel()
    # SendEmail = email_oper.SendEmailModel()
    # SendEmail.postreport_only(PerformTime, content)
    pass