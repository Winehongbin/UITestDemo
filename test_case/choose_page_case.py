# -*- coding: utf-8 -*-
import unittest
import time
from selenium.common.exceptions import NoSuchWindowException
from pages.common_pages.driver import brower
from pages.common_pages.login_page import LoginPage
from pages.main_pages.choose_page_test import ChoosePageTest


#import time

class Choose_Page_Case(unittest.TestCase):

    """所有应用主界面模块测试用例"""

    def setUp(self):
        self.driver= brower()
        login = LoginPage(self.driver)
        login.login()
        # choose = ChoosePage(self.driver)
        # choose.click_menu_bt('20')
        # self.conn,self.cur=DatabaseOperation().openconnect()

    def tearDown(self):
        self.driver.quit()

    # 进入应用界面
    def test_001_intoApp(self):
        time.sleep(5)
        test = ChoosePageTest(self.driver)
        try:
            actual_dict=test.cyclic_test_app(23)
        except NoSuchWindowException:
            self.driver.quit()
        print actual_dict
        # actual_result = test.cyclic_test_app(2)
        # print u"循环结束时"+self.driver.window_handles
        # winHandles = self.driver.window_handles
        # for handle in winHandles:
        #     print u"循环结束时" + handle
        # expected_dict = {'微信':1,'场景':1,'DSP投放':1,'SEM助手':1,'图聚智能':1,'数据监测工具':1,'智能分析':1,
        #                  '数据看板':1,'线上会':1,'线下会':1,'表单管理':1,'问卷':1,'抽奖':1,'投票':1,
        #                  '微讨论':1,'产品管理':1,'客户管理':1,'文件管理':1,'供应商管理':1,'邮件管理':1,'短信管理':1,
        #                  '文章管理':1,'成员管理':1,'角色管理':1,'模块管理':1,'字典表管理':1}

        # expected_result = 1
        #缺少“数据监测工具”和“数据看板”和“智能分析”
        # expected_dict = {'微信':1,'场景':1,'DSP投放':1,'SEM助手':1,'图聚智能':1,
        #                  '线上会':1,'线下会':1,'表单管理':1,'问卷':1,'抽奖':1,'投票':1,
        #                  '微讨论':1,'产品管理':1,'客户管理':1,'文件管理':1,'供应商管理':1,'邮件管理':1,'短信管理':1,
        #                  '文章管理':1,'成员管理':1,'角色管理':1,'模块管理':1,'字典表管理':1}
        # expected_dict = {'wx':1,'cj':1,'DSPtf':1,'SEMzs':1,'tjzn':1,'sjjcgj':1,'znfx':1,
        #                  'sjkb':1,'xsh':1,'xxh':1}
        expected_dict = {'wx':1,'cj':1,'DSPtf':1,'SEMzs':1,'tjzn':1, 'xsh': 1, 'xxh': 1, 'bdgl': 1, 'wj': 1,'cj':1,'tp':1,'wtl':1,'cpgl':1,'gysgl':1,'yjgl':1,'dxgl':1,'wzgl':1}
        # expected_dict = {'wx': 1, 'cj': 1, 'DSPtf': 1, 'SEMzs': 1, 'tjzn': 1, 'xsh': 1, 'xxh': 1, 'bdgl': 1, 'wj': 1,'cj':1,'tp':1,'wtl':1,'cpgl':1,'khgl':1,'wjgl':1,'gysgl':1,'yjgl':1,'dxgl':1,'wzgl':1,'cygl':1,'jsgl':1,'mkgl':1,'zdbgl':1}
        print expected_dict
        # failapp=''
        # for key, value in actual_dict.items():
        #     print('{key}:{value}'.format(key=key, value=value))
        #     if value == 0:
        #         failapp = failapp+str(key)+","
        # length=len(failapp)
        # print(u"失败的应用："+failapp[0:length-1] )

        self.assertDictEqual(actual_dict,expected_dict, msg="choose page failed")
        # self.assertEqual(actual_result, expected_result, msg="choose page failed")
        # object.quit()
        # base.deprint("创建线下会页面用例执行完成")
        # try:
        #     test.createEdm("邀请函")
        #     result='success'
        #
        # except:
        #     result='failed'

        # endTime = BasePage(self.driver).nowtime()  # 记录用例执行完成时间
        # insertSql = "INSERT into caselog VALUES ('创建邮件任务','邮件','%s','%s','%s')" % (startTime, endTime, result)
        # self.cur.execute(insertSql)
        # self.conn.commit()

if __name__ == "__main__":
    suit=unittest.TestSuite()
    suit.addTest(Choose_Page_Case("test_001_intoApp"))
    runner = unittest.TextTestRunner()
    runner.run(suit)
