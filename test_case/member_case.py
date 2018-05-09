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
    def test_001_NewCustomEmailField(self):
        test=FieldAction(self.driver)
        test.NewCustomEmailField()
    def test_002_NewCustomListField(self):
        test=FieldAction(self.driver)
        test.NewCustomListField(u"省市")
    def test_003_NewCustomListField(self):
        test = FieldAction(self.driver)
        test.EditForm(u"自动化测试专用", u"手机", u"姓名")
    def test_004_DelField(self):
        test = FieldAction(self.driver)
        test.DelField(u"自定义邮箱身份标识")
        test.DelField(u"自定义列表字段")
if __name__ == "__main__":
    suit=unittest.TestSuite()
    suit.addTest(Member_Test("test_001_NewCustomEmailField"))
    suit.addTest(Member_Test("test_002_NewCustomListField"))
    suit.addTest(Member_Test("test_003_NewCustomListField"))
    suit.addTest(Member_Test("test_004_DelField"))
    runner = unittest.TextTestRunner()
    runner.run(suit)
