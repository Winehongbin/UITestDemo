# -*- coding: utf-8 -*-

import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__)) #os.path.basename(path):返回所给路径path的最底层路径名或者是文件名；
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
import unittest
from pages.common_pages.login_page import LoginPage
from pages.common_pages.choose_page import ChoosePage
from pages.common_pages.driver import brower
from pages.questionnaire_page.questionnaire_list_page import QuestionnaireListPage
from pages.questionnaire_page.question_bank_page import QuestionBankManagement
from pages.questionnaire_page.new_questionnaire_page import NewQuestionnairePage
import time

class Questionnaire(unittest.TestCase):
    """ 问卷测试用例（创建试题、删除试题、创建常规问卷） """
    def setUp(self):
        self.driver = brower()
        object = LoginPage(self.driver)
        object.login()

        object = ChoosePage(self.driver)
        object.click_menu_bt('11')

    def tearDown(self):
        self.driver.quit()

    def test_001_create_question(self):
        """创建试题"""
        time.sleep(10)
        object = QuestionnaireListPage(self.driver)
        object.open_questionBank()
        object = QuestionBankManagement(self.driver)
        actual_result=object.create_question()
        expect_result="What is your favorite sport?"
        self.assertEqual(actual_result,expect_result,u"试题没有创建成功")

    def test_002_delete_question(self):
        """删除试题"""
        time.sleep(10)
        object = QuestionnaireListPage(self.driver)
        object.open_questionBank()
        object = QuestionBankManagement(self.driver)
        object.delete_question()

    '''def test_003_create_questionnaire(self):
         """创建常规问卷"""
         time.sleep(10)
         object=QuestionnaireListPage(self.driver)
         object.open_create_questionnaire()
         object=NewQuestionnairePage(self.driver)
         object.creat_new_questionnaire()
         time.sleep(5)
         object.edit_questionnaire_subject()'''

if __name__ == '__main__':
    suit = unittest.TestSuite()
    suit.addTest(Questionnaire("test_001_create_question"))
    suit.addTest(Questionnaire("test_002_delete_question"))
    # suit.addTest(Questionnaire("test_003_create_questionnaire"))
    runner = unittest.TextTestRunner()
    runner.run(suit)