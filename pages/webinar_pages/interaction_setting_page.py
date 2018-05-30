# -*- coding:utf-8 -*-
from pages.common_pages.base import BasePage
from pages.webinar_pages.index_page import Webinar_IndexPage
from pages.common_pages.login_page import LoginPage
from pages.common_pages.driver import brower
from pages.common_pages.choose_page import ChoosePage
import time
from pages.webinar_pages.create_meeting import Webinar_Create
from pages.questionnaire_page.new_questionnaire_page import NewQuestionnairePage

class InteractionSetting(BasePage):

    # 进入互动设置页面
    def interaction_setting(self):
        self.deprint("点击互动设置")
        self.wait_is_visible('x','/html/body/div[1]/div[2]/div[1]/ul/li[2]/ul/li[2]/a')


    # 创建问卷
    def create_questionnar(self):
        self.wait_is_visible('x','/html/body/div[1]/div[2]/div[2]/div/div[2]/div[1]/div/a[1]')
        time.sleep(1)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.deprint("跳转到问卷创建页面")

    # 点击刷新按钮
    def click_refresh(self):
        self.driver.switch_to.window(self.driver.window_handles[2])
        try:
            self.wait_is_visible('x','/html/body/div[1]/div[2]/div[2]/div/div[2]/div[1]/div/a[2]')
            self.wait_is_visible('x','/html/body/div[1]/div[2]/div[2]/div/div[2]/div[2]/div/div/div/div/a')
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

if __name__ == '__main__':

    dr = brower()
    o = LoginPage(dr)
    o.login()
    o = ChoosePage(dr)
    time.sleep(3)
    o.click_menu_bt('8')
    o = Webinar_IndexPage(dr)
    time.sleep(3)
    o.index_webinar()
    wbr = Webinar_Create(dr)
    wbr.create_meeting()
    question = InteractionSetting(dr)
    question.interaction_setting()
    time.sleep(2)
    question.create_questionnar()
    newquestion = NewQuestionnairePage(dr)
    newquestion.creat_new_questionnaire()
    newquestion.edit_questionnaire_subject()
    question.click_refresh()


