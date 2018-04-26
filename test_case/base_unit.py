# -*- coding: utf-8 -*-
#基础单元测试
#完成每个子单元测试需要做的事情
import unittest
from pages.common_pages.driver import brower


class BaseUnit(unittest.TestCase):


    #setUp()方法用于测试用例执行前的初始化工作。
    def setUp(self):
        self.driver = brower()

    #setDown()方法与setUp()相呼应，用于测试用例执行之后的善后工作
    def setDown(self):
        self.driver.quit()
