# -*- coding: utf-8 -*-
import time
from datetime import datetime
from common.report import report
import sys
reload(sys)  #在解释器里修改的编码只能保证当次有效，在重启解释器后，会发现，编码又被重置为默认的ascii了
sys.setdefaultencoding('utf8')
import os
curPath = os.path.abspath(os.path.dirname(__file__)) #os.path.basename(path):返回所给路径path的最底层路径名或者是文件名；
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
import unittest
from pages.common_pages.login_page import LoginPage
import time
from pages.common_pages.choose_page import ChoosePage
from pages.common_pages.driver import brower
from pages.member.member_management import MemberAction
import time
from common.mail import email_oper


class Member_Test(unittest.TestCase):
    """ 客户管理测试用例（创建图文素材用例、新建自定义列表字段、删除新创建的两个自定义字段） """
    def setUp(self):
        self.driver= brower()
        login = LoginPage(self.driver)
        login.login()
        choose = ChoosePage(self.driver)
        time.sleep(2)
        choose.click_menu_bt('16')
    def tearDown(self):
        self.driver.quit()
    #创建图文素材用例
    # def test_001_new_custom_mail_field(self):
    #     test = MemberAction(self.driver)
    #     actual_result = test.new_custom_mail_field()
    #     expected_result = u'自定义字段创建成功'
    #     self.assertEqual(actual_result, expected_result, msg="failed")
        # """ 新建自定义身份标识字段"""
        # try:
        #     test=MemberAction(self.driver)
        #     test.new_custom_mail_field()
        # except:
        #     try:
        #         test = MemberAction(self.driver)
        #         test.new_custom_mail_field()
        #     except:
        #         test.deprint(u"新增自定义邮箱身份标识用例失败")

    def test_002_new_custom_list_field(self):
        """ 新建自定义列表字段 """
        # test=MemberAction(self.driver)
        # test.new_custom_list_field(u"省市")
        test = MemberAction(self.driver)
        actual_result = test.new_custom_list_field(u"省市")
        expected_result = u'新增列表字段成功'
        self.assertEqual(actual_result, expected_result, msg="failed")
    # def test_003_edit_form(self):
    #     """ 编辑注册表单删除添加指定字段"""
    #     test = FieldAction(self.driver)
    #     test.edit_form(u"自动化测试专用", u"手机", u"姓名")
    def test_004_del_field(self):
        """ 删除新创建的两个自定义字段 """
        test = MemberAction(self.driver)
        # test.del_field(u"自定义邮箱身份标识")
        # test.del_field(u"自定义列表字段")
        actual_result = test.del_field(u"自定义邮箱身份标识")
        expected_result = u'完成删除操作'
        self.assertEqual(actual_result, expected_result, msg="failed")

    # def test_005_contact_basic_tag(self):
    #     """ 添加删除联系人基本标签 """
    #     test = MemberAction(self.driver)
    #     test.search_contact("auto_test@test.com")
    #     dickname = test.basic_tag()
    #     expect_result = {'name1:': u"新增自动化测试专用标签", 'name2:': u"新增自动化测试专用标签", 'shezhi1:': u"人工设置", 'shezhi2:': u"人工设置",
    #                      'tag_name1': u"自动化测试1", 'tag_name2:': u"自动化测试1"}
    #     self.assertDictEqual(expect_result, dickname, u"基本信息标签添加数据记录有误")


        # actual_result1,actual_result2,actual_result3,actual_result4,actual_result5,actual_result6  = test.basic_tag()
        # print  actual_result1,actual_result2,actual_result3,actual_result4,actual_result5,actual_result6
        # expect_result = [u"人工设置",u"人工设置",u"新增自动化测试专用标签",u"新增自动化测试专用标签",u"自动化测试1",u"自动化测试1"]
        # print expect_result[0]
        # self.assertDictContainsSubset(u"人工设置",actual_result1,u"基本信息标签添加数据记录有误")
        # self.assertDictContainsSubset(expect_result[1], actual_result2, u"基本信息标签添加数据记录有误")
        # self.assertDictContainsSubset(expect_result[2], actual_result3, u"基本信息标签添加数据记录有误")
        # self.assertDictContainsSubset(expect_result[3], actual_result4, u"基本信息标签添加数据记录有误")
        # self.assertDictContainsSubset(expect_result[4], actual_result5, u"基本信息标签添加数据记录有误")
        # self.assertDictContainsSubset(expect_result[5], actual_result6, u"基本信息标签添加数据记录有误")
if __name__ == "__main__":
    suit=unittest.TestSuite()
    suit.addTest(Member_Test("test_004_del_field"))
    #uit.addTest(Member_Test("test_002_new_custom_list_field"))
    # suit.addTest(Member_Test("test_003_edit_form"))
    # suit.addTest(Member_Test("test_004_del_field"))
    runner = unittest.TextTestRunner()
    runner.run(suit)
