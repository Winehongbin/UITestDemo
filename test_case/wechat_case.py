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
from pages.wechat.create_material import Creat_media

class Wechat_Test(unittest.TestCase):

    """微信测试用例"""

    def setUp(self):
        self.driver= brower()
        login = LoginPage(self.driver)
        login.login()
        choose = ChoosePage(self.driver)
        choose.click_menu_bt("1")

    def tearDown(self):
        self.driver.quit()
    # 创建图文素材用例
    def test_001_createMedia(self):

        """测试创建图文素材"""

        test=Creat_media(self.driver)
        actual_result=test.creat_media()
        expected_result=u'素材创建成功'
        self.assertEqual(actual_result,expected_result,msg="failed")

    def test_002_deleteMedia(self):
        """测试删除图文素材"""
        test=Creat_media(self.driver)
        test.delete_media()
if __name__ == "__main__":
    suit=unittest.TestSuite()
    suit.addTest(Wechat_Test("test_001_createMedia"))
    suit.addTest(Wechat_Test("test_001_createMedia"))
    runner = unittest.TextTestRunner()
    runner.run(suit)
