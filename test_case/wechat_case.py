# -*- coding: utf-8 -*-
import time
from datetime import datetime
import unittest
import os
import sys
from datetime import datetime
curPath = os.path.abspath(os.path.dirname(__file__)) #os.path.basename(path):返回所给路径path的最底层路径名或者是文件名；
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
from pages.common_pages.login_page import LoginPage
import time
from pages.common_pages.choose_page import ChoosePage
from pages.common_pages.driver import brower
from pages.wechat.create_material import Creat_media
from common.common_function.mysql import DatabaseOperation
from pages.common_pages.base import BasePage
from pages.vote_pages.vote_page import Create_vote
from pages.wechat.syn_materials import Syn_materials
from pages.wechat.create_groupsend import Create_groupsend
from pages.wechat.create_channelqrcode import Create_channelqrcode


class Wechat_Test(unittest.TestCase):

    """微信测试用例（创建图文素材、删除图文素材、创建微信实例下投票并浏览提交投票、同步微信素材、定时群发消息、新增渠道二维码）"""

    def setUp(self):
        self.driver= brower()
        login = LoginPage(self.driver)
        login.login()
        choose = ChoosePage(self.driver)
        choose.click_menu_bt('1')
        # self.conn,self.cur=DatabaseOperation().openconnect()  #创建数据库连接

    def tearDown(self):
        self.driver.quit()
        # self.conn.close() #关闭数据库连接
    # 创建图文素材用例
    def test_001_createMedia(self):

        """测试创建图文素材"""
        startTime=BasePage(self.driver).nowtime() #记录用例开始执行的时间
        # print "用例开始执行时间："+startTime
        test=Creat_media(self.driver)
        actual_result=test.creat_media()
        expected_result=u'素材创建成功'
        if actual_result==expected_result:
            result='success'
        else:
            result='failed'
        # self.assertEqual(actual_result,expected_result,msg="failed")
        endTime=BasePage(self.driver).nowtime() #记录用例执行完成时间
        # print "用例开始完成时间：" + endTime
        # insertSql = "INSERT into caselog VALUES ('创建图文素材','微信','%s','%s','%s')"  % (startTime,endTime,result)  #执行结果插入数据库
        # # print insertSql
        # self.cur.execute(insertSql)
        # self.conn.commit()

    def test_002_deleteMedia(self):
        """测试删除图文素材"""
        startTime = BasePage(self.driver).nowtime()  # 记录用例开始执行的时间
        # print "用例开始执行时间：" + startTime
        test=Creat_media(self.driver)
        try:
            test.delete_media()
            endTime = BasePage(self.driver).nowtime()  # 记录用例执行完成时间
            # print "用例开始完成时间：" + endTime
            result='success' #设置用例执行结果为success
        except:
            result='failed' #设置用例执行结果为failed
            endTime = BasePage(self.driver).nowtime()  # 记录用例执行完成时间
        # insertSql = "INSERT into caselog VALUES ('删除图文素材','微信','%s','%s','%s')" % (startTime, endTime, result) #将用例执行结果插入数据库
        # # print insertSql
        # self.cur.execute(insertSql)
        # self.conn.commit()

    def test_003_createVote(self):
        """创建微信实例下的投票、浏览投票、提交投票"""
        changetoVote=Creat_media(self.driver)
        changetoVote.enter_vote()
        time.sleep(3)
        test=Create_vote(self.driver)
        test.new_vote()
        time.sleep(3)
        test.setItems()
        actual_result=test.browse_vote()
        expected_result = u'提交成功！'
        self.assertEqual(actual_result,expected_result,msg='failed')
    # 丽楠添加
    def test_004_synMaterials(self):
        """同步微信素材"""
        syn = Syn_materials(self.driver)
        actual_result = syn.syn_materials()
        expected_result = u'同步微信素材成功'
        if actual_result == expected_result:
            result = 'success'
        else:
            result = 'failed'

    def test_005_createGroupsend(self):
        """定时群发消息"""
        groupsend = Create_groupsend(self.driver)
        actual_result = groupsend.create_groupsend()
        expected_result = u'定时群发消息成功'
        if actual_result == expected_result:
            result = 'success'
        else:
            result = 'failed'

    def test_006_createChannelqrcode(self):
        """新增渠道二维码"""
        createchannel = Create_channelqrcode(self.driver)
        actual_result = createchannel.create_channelqrcode(self.driver)
        expected_result = u'新增渠道二维码成功'
        if actual_result == expected_result:
            result = 'success'
        else:
            result = 'failed'


if __name__ == "__main__":
    suit=unittest.TestSuite()
    # suit.addTest(Wechat_Test("test_004_synMaterials"))
    # suit.addTest(Wechat_Test("test_005_createGroupsend"))
    suit.addTest(Wechat_Test("test_005_createGroupsend"))
    # suit.addTest(Wechat_Test("test_002_deleteMedia"))
    runner = unittest.TextTestRunner()
    runner.run(suit)
