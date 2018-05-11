# -*- coding: utf-8 -*-
import time
from datetime import datetime
import unittest
from test_case.base_unit import BaseUnit
from pages.common_pages.base import BasePage
from pages.common_pages.login_page import LoginPage
import time
from pages.common_pages.choose_page import ChoosePage
from pages.common_pages.driver import brower
from pages.member.member_management import FieldAction

class Member_Test(unittest.TestCase):
    """ 客户管理测试用例 """
    def setUp(self):
        self.driver= brower()
        login = LoginPage(self.driver)
        login.login()
        choose = ChoosePage(self.driver)
        time.sleep(2)
        choose.click_menu_bt("16")
    def tearDown(self):
        self.driver.quit()
    # 创建图文素材用例
    def test_001_new_custom_mail_field(self):
        """ 新建自定义身份标识字段"""
        test=FieldAction(self.driver)
        test.new_custom_mail_field()
    def test_002_new_custom_list_field(self):
        """ 新建自定义列表字段 """
        test=FieldAction(self.driver)
        test.new_custom_list_field(u"省市")
    def test_003_edit_form(self):
        """ 编辑注册表单删除添加指定字段"""
        test = FieldAction(self.driver)
        test.edit_form(u"自动化测试专用", u"手机", u"姓名")
    def test_004_del_field(self):
        """ 删除新创建的两个自定义字段 """
        test = FieldAction(self.driver)
        test.del_field(u"自定义邮箱身份标识")
        test.del_field(u"自定义列表字段")
if __name__ == "__main__":
    suit=unittest.TestSuite()
    suit.addTest(Member_Test("test_001_new_custom_mail_field"))
    suit.addTest(Member_Test("test_002_new_custom_list_field"))
    suit.addTest(Member_Test("test_003_edit_form"))
    suit.addTest(Member_Test("test_004_del_field"))
    runner = unittest.TextTestRunner()
    runner.run(suit)
