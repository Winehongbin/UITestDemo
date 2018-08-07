# -*- coding:utf-8 -*-
from pages.common_pages.base import BasePage
from pages.webinar_pages.index_page import Webinar_IndexPage
from pages.common_pages.login_page import LoginPage
from pages.common_pages.driver import brower
from pages.common_pages.choose_page import ChoosePage
import time,os
from pages.webinar_pages.create_meeting import Webinar_Create
from pages.questionnaire_page.new_questionnaire_page import NewQuestionnairePage

class InteractionSetting(BasePage):

    # 进入互动设置页面
    def interaction_setting(self):
        self.deprint("点击互动设置")
        self.wait_is_visible('x','/html/body/div[1]/div[2]/div[1]/ul/li[2]/ul/li[2]/a')
        current_handles=self.driver.current_window_handle
        return current_handles


    # 创建问卷
    def create_questionnar(self):
        self.wait_is_visible('x','/html/body/div[1]/div[2]/div[2]/div/div[2]/div[1]/div/a[1]')
        time.sleep(1)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.deprint("跳转到问卷创建页面")
    def refresh_meeting(self,current_habdles):
        # 进入到会议详情页面并刷新当前页面
        all_handles = self.driver.window_handles
        for i in all_handles:
            if i == current_habdles:
                self.driver.switch_to.window(i)
                self.driver.refresh()
    # 点击问卷的刷新按钮
    def click_refresh(self,current_habdles):
        # self.driver.switch_to.window(self.driver.window_handles[2])
        try:
            all_handles=self.driver.window_handles
            for i in all_handles:
                if i ==current_habdles:
                    self.driver.switch_to.window(i)
                    self.driver.refresh()
                    self.wait_is_visible('x', '//*[@id="collapse2"]/li[2]/a')
                    self.wait_is_visible('x', '/html/body/div[1]/div[2]/div[2]/div/div[2]/div[2]/div/div/div/div/a')
                    self.wait_is_visible('x', '//*[@id="collapse2"]/li[2]/a')
                    self.wait_is_visible('x', '/html/body/div[1]/div[2]/div[2]/div/div[2]/div[2]/div/div/div/div/a')
                    time.sleep(3)
                    self.deprint('问卷创建成功，且设置为默认问卷')
        except:
            try:
                self.wait_is_visible('x', '/html/body/div[1]/div[2]/div[2]/div/div[2]/div[1]/div/a[2]')
                self.wait_is_visible('x', '/html/body/div[1]/div[2]/div[2]/div/div[2]/div[2]/div/div/div/div/a')
                time.sleep(3)
                self.deprint('问卷创建成功，且设置为默认问卷')
            except:
                self.deprint('问卷创建失败')
    def Close_AndRefresh(self):
        # 关闭并刷新当前页面
        self.driver.close()
        self.driver.refresh()
    # 添加抽奖信息
    def create_luckydraw(self):
        self.deprint('添加抽奖信息')
        # 点击添加抽奖按钮
        self.wait_is_visible('x','/html/body/div[1]/div[2]/div[2]/div/div[4]/div[1]/div/a[1]')
        time.sleep(3)
        # 填写抽奖信息：增加第一个奖项
        self.find_element_input('x','//*[@id="myModa45"]/div/div/div[2]/form/div[1]/div[1]/input',u'一等奖')
        self.wait_is_visible('x','//*[@id="myModa45"]/div/div/div[2]/form/div[1]/div[2]/div/button')
        self.wait_is_visible('x','//*[@id="myModa45"]/div/div/div[2]/form/div[1]/div[2]/div/ul/li/a[1]')
        self.find_element_input('x','//*[@id="myModa45"]/div/div/div[2]/form/div[1]/div[3]/input',u'苹果8')
        # 增加第二个奖项
        self.wait_is_visible('x','//*[@id="myModa45"]/div/div/div[2]/form/div[3]/div/span')
        self.find_element_input('x','//*[@id="myModa45"]/div/div/div[2]/form/div[2]/div[1]/input',u'二等奖')
        self.wait_is_visible('x','//*[@id="myModa45"]/div/div/div[2]/form/div[2]/div[2]/div/button')
        self.wait_is_visible('x','//*[@id="myModa45"]/div/div/div[2]/form/div[2]/div[2]/div/ul/li/a[2]')
        self.find_element_input('x','//*[@id="myModa45"]/div/div/div[2]/form/div[2]/div[3]/input',u'蓝牙耳机')
        # 点击确定按钮
        self.wait_is_visible('x','//*[@id="myModa45"]/div/div/div[3]/a[1]')
        time.sleep(5)
        target = self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/div[4]/div[2]/div/table/tbody/tr[1]/td[1]")
        self.driver.execute_script("arguments[0].scrollIntoView();", target)
        vluckydrawname1 = self.find_element_text('x','/html/body/div[1]/div[2]/div[2]/div/div[4]/div[2]/div/table/tbody/tr[1]/td[1]')
        vluckydrawname2 = self.find_element_text('x','/html/body/div[1]/div[2]/div[2]/div/div[4]/div[2]/div/table/tbody/tr[2]/td[1]')

        if vluckydrawname1 == u'一等奖'and vluckydrawname2 == u'二等奖':
            self.deprint('抽奖添加成功')
            return "抽奖添加成功"
        else:
            self.deprint('抽奖添加失败')
            return "抽奖添加失败"
    def create_vote(self):
        # 点击新建投票按钮
        self.wait_is_visible('x','/html/body/div[1]/div[2]/div[2]/div/div[3]/div[1]/div/a[1]')
        # 跳转到新开的窗口中
        self.driver.switch_to.window(self.driver.window_handles[-1])
        time.sleep(1)
        # 输入标题
        self.find_element_input('x','//*[@id="pollTitle"]','自动化测试'+self.nowtime())
        # 点击设置时间后面的时间控件按钮
        self.wait_is_visible('x','//*[@id="txtTime"]')
        # 点击确定按钮
        self.wait_is_visible('x','/html/body/div[5]/div[3]/div/button[1]')
        # 拖动滚动条到最下面
        self.scrollbar("bottom")
        # 点击保存按钮
        self.wait_is_visible('x','/html/body/div[1]/div[2]/main/div/div/div/div[2]/div/button')
        # 对于弹出的提示框点击确定按钮
        self.wait_is_visible('x','//*[@id="alertCommon"]/div/div/div[3]/button')
    def Edit_vote(self):
        time.sleep(1)
        # 点击添加姓名选项
        self.wait_is_visible('x','//*[@id="left-menu"]/ul/li[1]/ul/li[1]/a')
        # 点击保存按钮
        self.wait_is_visible('x','/html/body/div[1]/div[2]/div[2]/div/div/div[2]/div/div/div[2]/div/button')
        # 针对弹出的对话框点击确定按钮
        self.wait_is_visible('x','//*[@id="alertCommon"]/div/div/div[3]/button')
        # 关闭当前投票页面
        self.close()
    def Add_File(self):
        # 点击添加文件按钮
        self.scrollbar("bottom")
        self.deprint("开始点击添加文件按钮")
        self.wait_is_visible('x','/html/body/div[1]/div[2]/div[2]/div/div[5]/div[1]/div/a[1]')
        # 切换到新开的窗口中
        self.driver.switch_to.window(self.driver.window_handles[-1])
        time.sleep(1)
        # 点击上传文件按钮
        self.wait_is_visible('x','/html/body/div/div[1]/div[2]/div[4]/div[2]/div/button[1]')
        # 开始上传图片
        cur_path = os.path.abspath(os.path.dirname(__file__))
        root_path = os.path.split(cur_path)[0]
        # print root_path
        os.system(root_path + "/upload.exe")
        # 关闭当前页面
        self.close()
if __name__ == '__main__':

    dr = brower()
    o = LoginPage(dr)
    o.login()
    o = ChoosePage(dr)
    time.sleep(3)
    o.click_menu_bt('8')
    time.sleep(2)
    o =  Webinar_IndexPage(dr)
    # o.index_webinar()
    o.webinar_list()
    time.sleep(3)
    o.choose_meeting()
    # time.sleep(3)
    # o.index_webinar()
    # wbr = Webinar_Create(dr)
    # wbr.create_meeting()
    time.sleep(2)
    luckydraw = InteractionSetting(dr)
    luckydraw.interaction_setting()
    luckydraw.create_luckydraw()
    # question.interaction_setting()
    # time.sleep(2)
    # question.create_questionnar()
    # newquestion = NewQuestionnairePage(dr)
    # newquestion.creat_new_questionnaire()
    # newquestion.edit_questionnaire_subject()
    # question.click_refresh()


