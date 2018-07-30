# -*- coding: utf-8 -*-
'''
Created on 2018-05-10
@author: 尤梅枝
'''

import os
import sys
from selenium.common.exceptions import NoAlertPresentException
reload(sys)
#print sys.getdefaultencoding()
# curPath = os.path.abspath(os.path.dirname(__file__)) #os.path.basename(path):返回所给路径path的最底层路径名或者是文件名；
# rootPath = os.path.split(curPath)[0]
# sys.path.append(rootPath)
from pages.common_pages.base import BasePage
from pages.common_pages.login_page import LoginPage
import time
from pages.common_pages.choose_page import ChoosePage
from pages.common_pages.driver import brower

class Creat_media(BasePage):
    #创建图文素材用例
    def creat_media(self):
        global text
        try:
            self.deprint("开始执行图文素材创建用例")
            self.wait_is_visible('x', '//*[@id="ul-nav-2"]/li[1]/a')  # 点击素材管理菜单
            time.sleep(3)
            self.wait_is_visible('x', '//*[@id="con-graphic"]/div[1]/div[2]/div/a[2]')  # 点击新建图文按钮
            self.deprint("点击新建图文按钮成功")
            self.find_element_input('x', '//*[@id="exampleInputText1"]', u'自动化创建' + self.nowtime())
            # 点击上传图片按钮
            self.find_element_click('x', '//*[@id="con-local"]/section/section/div[2]/form/div[1]/div[4]/div[3]/div')
            cur_path = os.path.abspath(os.path.dirname(__file__))
            root_path = os.path.split(cur_path)[0]
            # print root_path
            os.system(root_path + "/upload.exe")
            # os.system("D:\\upfile.exe")
            self.deprint(u"try上传封面图成功")
            time.sleep(3)
            self.find_element_input('x', '//*[@id="con-local"]/section/section/div[2]/form/div[1]/div[6]/textarea',
                                    u'尤梅枝的摘要' + self.nowtime())
            self.find_element_click('x', './/*[@id="con-local"]/section/section[1]/div[2]/form/div[1]/div[9]/div[2]')
            self.find_element_input('x',
                                    './/*[@id="con-local"]/section/section[1]/div[2]/form/div[1]/div[9]/div[2]/div[1]/div[1]/div[2]/iframe',
                                    u'自动化创建图文内容')
            self.find_element_input('x', '//*[@id="exampleInputText2"]', 'http://www.baidu.com')
            self.scrollbar("bottom")
            self.find_element_click('x', '//*[@id="con-local"]/section/section/div[2]/form/div[2]/button[1]')  # 点击保存按钮
            self.scrollbar("top")
            # 判断是否上传成功

            try:
                # 请上传图片！
                text=self.find_element_text('x','//*[@id="con-local"]/section/section/div[2]/form/div[1]/div[5]')
                # print "text56:",text
            except:
                text="success"
            time.sleep(5)
            # print 60
            # pos = self.driver.find_element_by_xpath('//*[@id="dialogBox"]/div/div/div[2]/div/div').text
            # self.driver.find_element_by_xpath('//*[@id="dialogBox"]/div/div')
            # # self.wait_is_visible('x','//*[@id="dialogBox"]/div/div/div[3]/button[1]')
            # try:
            #     alert = driver.switch_to.alert # '''获取alert对话框'''
            #     alert.text
            #     print alert.text
            #     return alert
            # except NoAlertPresentException:
            #     return False
            # alert.accept()  # alert对话框属于警告对话框，我们这里只能接受弹窗
            # self.wait_is_visible('x','//*[@id="dialogBox"]/div/div/div[3]/button[1]')
            # self.wait_is_visible('id','close')
            # self.deprint("text:",text)
            return text
        except:
            try:
                self.deprint("用例执行失败，重试一次")
                self.deprint("再次开始执行图文素材创建用例")
                self.wait_is_visible('x', '//*[@id="ul-nav-2"]/li[1]/a')  # 点击素材管理菜单
                time.sleep(3)
                self.wait_is_visible('x', '//*[@id="con-graphic"]/div[1]/div[2]/div/a[2]')  # 点击新建图文按钮
                self.deprint("点击新建图文按钮成功")
                self.find_element_input('x', '//*[@id="exampleInputText1"]', u'自动化创建' + self.nowtime())
                self.find_element_click('x',
                                        '//*[@id="con-local"]/section/section/div[2]/form/div[1]/div[4]/div[3]/div')
                cur_path = os.path.abspath(os.path.dirname(__file__))
                root_path = os.path.split(cur_path)[0]
                os.system(root_path + "/upload.exe")
                self.deprint(u"except上传封面图成功")
                # os.system("D:\\upfile.exe")
                time.sleep(3)

                self.find_element_input('x', '//*[@id="con-local"]/section/section/div[2]/form/div[1]/div[6]/textarea',
                                        u'尤梅枝的摘要' + self.nowtime())
                self.find_element_click('x',
                                        './/*[@id="con-local"]/section/section[1]/div[2]/form/div[1]/div[9]/div[2]')
                self.find_element_input('x',
                                        './/*[@id="con-local"]/section/section[1]/div[2]/form/div[1]/div[9]/div[2]/div[1]/div[1]/div[2]/iframe',
                                        u'自动化创建图文内容')
                self.find_element_input('x', '//*[@id="exampleInputText2"]', 'http://www.baidu.com')
                self.scrollbar("bottom")

                self.find_element_click('x',
                                        '//*[@id="con-local"]/section/section/div[2]/form/div[2]/button[1]')  # 点击保存按钮
                self.scrollbar("top")
                # 判断是否上传成功
                try:
                    # 请上传图片！
                    text = self.find_element_text('x', '//*[@id="con-local"]/section/section/div[2]/form/div[1]/div[5]')
                    # print "zhixingdaolezheli109:",text
                except:
                    text = "success"
                # print 114
                time.sleep(5)
                # pos = self.driver.find_element_by_xpath('//*[@id="dialogBox"]/div/div/div[2]/div/div').text
                # self.driver.find_element_by_xpath('//*[@id="dialogBox"]/div/div')
                # # self.wait_is_visible('x','//*[@id="dialogBox"]/div/div/div[3]/button[1]')
                # try:
                #     alert = driver.switch_to.alert # '''获取alert对话框'''
                #     alert.text
                #     print alert.text
                #     return alert
                # except NoAlertPresentException:
                #     return False
                # alert.accept()  # alert对话框属于警告对话框，我们这里只能接受弹窗
                # self.wait_is_visible('x','//*[@id="dialogBox"]/div/div/div[3]/button[1]')
                # self.wait_is_visible('id','close')
                # print "text129:",text
                # self.deprint("text:", text)
                return text
            except:
                self.deprint("图文素材创建失败")
                text="fail"
                return text

    #删除第一条图文素材用例
    def delete_media(self):
        global acturn_text
        acturn_text=""
        # self.deprint(u'开始执行图文素材删除用例')
        self.deprint("开始执行图文素材删除用例")

        self.wait_is_visible('x', '//*[@id="ul-nav-2"]/li[1]/a')  # 点击素材管理菜单
        time.sleep(3)
        self.find_element_input('x','//*[@id="txtSearchGraphics"]/input',u'自动化')
        self.find_element_click('x','//*[@id="con-graphic"]/div[1]/div[1]/div/a')
        time.sleep(3)
        text=self.find_element_text('x','//*[@id="con-graphic"]/div[7]/div')
        # self.deprint(text)
        #判断是否存在标题包含“自动化”的图文素材，如果查询结果返回暂无数据则跳过，否则删除第一条自动化素材
        if text==u'暂无数据':
            # 说明用例1执行失败
            self.deprint(u'暂无数据，不进行删除')
            acturn_text=text
        else:
            # self.deprint(u'开始执行删除操作')
            self.deprint("开始执行删除操作")

            self.wait_is_visible('x', '//*[@id="con-graphic"]/div[2]/div[1]/div/div[3]/span/a[4]')
            time.sleep(3)
            acturn_text=""
            try:
                self.wait_is_visible('x', '//*[@id="dialogBox"]/div/div/div[3]/button[1]')
                acturn_text="图文素材删除用例执行完毕"
            except:
                acturn_text = "执行失败"
        # self.deprint(u'图文素材删除用例执行完毕')
        self.deprint(acturn_text)
        print "acturn_text:",acturn_text
        return acturn_text
    def enter_vote(self):
        try:
            self.deprint("开始进入投票页面")
            # 先点击小三角，再去寻找元素
            self.wait_is_visible('x','//*[@id="accordion"]/div[2]/h2/span[3]')
            self.wait_is_visible('x', '//*[@id="ul-nav-6"]/li[7]/a')
            self.deprint("进入投票成功")
            self.driver.switch_to.window(self.driver.window_handles[-1])
        except:
            try:
                self.deprint("开始进入投票页面")
                self.wait_is_visible('x', '//*[@id="ul-nav-6"]/li[7]/a')
                self.deprint("进入投票成功")
                self.driver.switch_to.window(self.driver.window_handles[-1])
            except:
                self.deprint("进入投票模块失败")





if __name__ == '__main__':
    driver = brower()
    login= LoginPage(driver)
    login.login()
    chooseP = ChoosePage(driver)
    chooseP.click_menu_bt("1")
    test=Creat_media(driver)
    # title=test.test()
    # test = Creat_media(driver)
    title = test.enter_vote()
    # test.delete_media()
