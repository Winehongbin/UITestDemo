# -*- coding: utf-8 -*-
'''
Created on 2018-07-21
@author: 常丽楠
'''


from pages.common_pages.base import BasePage
from pages.common_pages.login_page import LoginPage
import time
from pages.common_pages.choose_page import ChoosePage
from pages.common_pages.driver import brower
import os

materialname = u'自动化创建定时群发图文' + time.strftime("%H:%M:%S")

class Create_groupsend(BasePage):
    #定时群发消息
        def create_media(self):
            self.find_element_input('x', '//*[@id="exampleInputText1"]', materialname)
            self.find_element_click('x', '//*[@id="con-local"]/section/section/div[2]/form/div[1]/div[4]/div[3]/div')
            time.sleep(2)
            cur_path = os.path.abspath(os.path.dirname(__file__))
            root_path = os.path.split(cur_path)[0]
            os.system(root_path + "/upload.exe")
            self.deprint("上传封面图成功")
            time.sleep(3)
            self.find_element_input('x', '//*[@id="con-local"]/section/section/div[2]/form/div[1]/div[6]/textarea', u'定时群发图文的摘要' + self.nowtime())
            self.find_element_click('x', './/*[@id="con-local"]/section/section[1]/div[2]/form/div[1]/div[9]/div[2]')
            self.find_element_input('x', './/*[@id="con-local"]/section/section[1]/div[2]/form/div[1]/div[9]/div[2]/div[1]/div[1]/div[2]/iframe', u'定时群发图文内容')
            self.find_element_input('x', '//*[@id="exampleInputText2"]', 'http://www.baidu.com')
            self.scrollbar("bottom")
            self.find_element_click('x', '//*[@id="con-local"]/section/section/div[2]/form/div[2]/button[1]')  # 点击保存按钮
            time.sleep(5)
            return u'素材创建成功'

        def timing_group(self):
            self.deprint("开始执行定时群发消息用例")
            time.sleep(5)

            self.wait_is_visible('x', '//*[@id="ul-nav-2"]/li[6]/a')  # 点击群发功能菜单
            time.sleep(5)
            self.wait_is_visible('x', '//*[@id="new-message"]/div[2]/div/div[2]/div/div/div/div[2]/a/span')  # 点击新建图文按钮
            self.deprint("点击新建图文按钮成功")
            time.sleep(3)
            Create_groupsend.create_media(self)
            self.wait_is_visible('x', '//*[@id="dialogBox"]/div/div/div[3]/button[1]')  # 点击确定按钮
            time.sleep(3)
            self.wait_is_visible('x', '//*[@id="new-message"]/div[1]/button/span')  # 点击选择粉丝分组按钮
            time.sleep(3)
            self.scrollbar("bottom")
            self.wait_is_visible('x', '//*[@id="Confirm"]/div/div/div[2]/div/div[2]/div[2]/span[52]')  # 选择一个分组
            self.wait_is_visible('x', '//*[@id="Confirm"]/div/div/div[3]/button[1]')  # 点击确定按钮
            time.sleep(2)
            self.wait_is_visible('x', '// *[ @ id = "qf"] / span')  #点击定时群发按钮
            time.sleep(3)
            self.wait_is_visible('x', '/html/body/div[8]/div[1]/div[1]/table/thead/tr[1]/th[3]/i')  # 选择下个月
            time.sleep(2)
            self.wait_is_visible('x', '/html/body/div[8]/div[1]/div[1]/table/tbody/tr[3]/td[4]')  #选择一个日期
            self.wait_is_visible('x', '/html/body/div[8]/div[3]/div/button[1]')  # 点击确定按钮
            time.sleep(2)
            self.wait_is_visible('x', '//*[@id="dialogBox"]/div/div/div[3]/button[1]')  # 设置成功对话框点击确定按钮


        def create_groupsend(self):
            try:
                Create_groupsend.timing_group(self)
                name = self.find_element_text('x', '//*[@id="timing-message"]/div/div/div[2]/div[1]/div[1]/div/div[2]/div[3]')
                if name == materialname:
                     self.deprint("定时群发消息用例执行完成")
                     time.sleep(3)
                     self.find_element_click('x', '// *[ @ id = "timing-message"] / div / div / div[2] / div[1] / div[1] / div / div[4] / span / a[2]')  # 点击取消预设按钮
                     return u'定时群发消息成功'
            except:
                self.deprint("用例执行失败，重试一次")
                self.deprint("再次开始执行定时群发消息用例")
                Create_groupsend.timing_group(self)
                name = self.find_element_text('x', '//*[@id="timing-message"]/div/div/div[2]/div[1]/div[1]/div/div[2]/div[3]')
                if name == materialname:
                     self.deprint("定时群发消息用例执行完成")
                     time.sleep(3)
                     self.find_element_click('x',
                                             '// *[ @ id = "timing-message"] / div / div / div[2] / div[1] / div[1] / div / div[4] / span / a[2]')  #点击取消预设按钮
                     return u'定时群发消息成功'
                else:
                     self.deprint("定时群发消息发送失败")



if __name__ == '__main__':
    driver = brower()
    login = LoginPage(driver)
    login.login()
    chooseP = ChoosePage(driver)
    chooseP.click_menu_bt("1")
    batch = Create_groupsend(driver)
    result = batch.create_groupsend()