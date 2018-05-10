# -*- coding: utf-8 -*-

import time
from pages.common_pages.base import BasePage
from pages.common_pages.login_page import LoginPage
from pages.common_pages.choose_page import ChoosePage
from pages.common_pages.driver import brower
from pages.questionnaire_page.questionnaire_list_page import QuestionnaireListPage

class QuestionBankManagement(BasePage):

# 创建试题
    def create_question(self):
        print self.deprint(),':开始创建试题'
        self.dominant_wait('x','/html/body/div[1]/div[2]/div[1]/div[2]/div/div[1]/ul/li[1]/a') #点击默认题库
        self.dominant_wait('x','/html/body/div[1]/div[2]/div[1]/div[2]/div/div[2]/div/div[1]/button') #点击创建试题
        time.sleep(1)
        self.find_element_input("x",'//*[@id="examDialog"]/div/div/div[2]/div[3]/div/input',"What's your favorite sport?") #输入试题内容
        self.find_element_click("x",'//*[@id="examDialog"]/div/div/div[2]/div[4]/div/div/a[1]') #点击添加选项
        self.find_element_input("x",'//*[@id="input_Radio0"]','badminton') #输入第一个选项
        self.find_element_click("x",'//*[@id="examDialog"]/div/div/div[2]/div[4]/div/div/a[1]') #点击添加选项
        self.find_element_input("x",'//*[@id="input_Radio1"]','table tennis') #输入第二个选项

        self.find_element_click("x",'//*[@id="examDialog"]/div/div/div[2]/div[4]/div/div/a[1]') #点击添加选项
        self.find_element_input("x",'//*[@id="input_Radio2"]','rope skipping') #输入第三个选项
        self.find_element_click("x",'//*[@id="examDialog"]/div/div/div[2]/div[4]/div/div/a[1]') #点击添加选项
        self.find_element_input('x','//*[@id="input_Radio3"]','basketball') #输入第四个选项
        time.sleep(1)

        js='document.getElementsByName("optionGroupRadio")[0].click();'#设置第一个选项为正确选项
        self.driver.execute_script(js)
        time.sleep(1)
        self.find_element_click('x','//*[@id="examDialog"]/div/div/div[3]/button[1]') #点击确定按钮
        print self.deprint(), ':创建试题完成'
        return  self.find_element_text('x','/html/body/div[1]/div[2]/div[1]/div[2]/div/div[2]/div/ul/li[1]/div/p[1]')


if __name__ == '__main__':
    dr = brower()
    object = LoginPage(dr)
    object.login()
    object = ChoosePage(dr)
    object.click_menu_bt('11')
    object = QuestionnaireListPage(dr)
    object.open_questionBank()
    object = QuestionBankManagement(dr)
    object.create_question()
    # object.quit()