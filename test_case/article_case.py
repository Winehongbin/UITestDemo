# -*- coding: utf-8 -*-

import unittest
import time
from pages.common_pages.driver import brower
from pages.common_pages.login_page import LoginPage
from pages.common_pages.choose_page import ChoosePage
from pages.management_tools.article_pages.section_list_page import SectionListPage

class Article(unittest.TestCase):
    """ 文章管理测试用例（创建栏目） """
    def setUp(self):
        self.driver = brower()
        object = LoginPage(self.driver)
        object.login()

        object = ChoosePage(self.driver)
        object.click_menu_bt('21')

    def tearDown(self):
        self.driver.quit()

    def test_001_create_section(self):
        """创建浏览删除栏目"""
        time.sleep(10)
        object = SectionListPage(self.driver)
        object.new_section()
        object.browse_section()
        actual_result = object.open_detail_data()
        expected_result = (u'1',u'1')
        # 对元祖进行断言
        self.assertTupleEqual(actual_result,expected_result,"fail")
        # self.assertEqual(actual_result, expected_result, msg="failed")  #验证浏览量和浏览人数
        object.deprint("浏览量和浏览人数验证通过")
        object.delete_section()


if __name__ == '__main__':
    suit = unittest.TestSuite()
    suit.addTest(Article("test_001_create_section"))
    runner = unittest.TextTestRunner()
    runner.run(suit)