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
        try:
            self.deprint('开始创建试题')
            self.wait_is_visible('x', '/html/body/div[1]/div[2]/main/div/div[2]/div[2]/div[1]/div[1]/ul/li[1]/a')  # 点击默认题库
            self.wait_is_visible('x', '/html/body/div[1]/div[2]/main/div/div[2]/div[2]/div[2]/div/div[6]/button')  # 点击创建试题
            time.sleep(1)
            self.deprint('点击创建试题成功')
            self.find_element_input("x", '//*[@id="examDialog"]/div/div/div[2]/div/div[3]/div/input',
                                    "What is your favorite sport?")  # 输入试题内容
            self.find_element_input("x", '//*[@id="input_Radio0"]', 'badminton')  # 输入第一个选项
            self.find_element_click("x", '//*[@id="examDialog"]/div/div/div[2]/div/div[4]/div/div[2]/a[1]')  # 点击添加选项
            self.find_element_input("x", '//*[@id="input_Radio1"]', 'table tennis')  # 输入第二个选项

            self.find_element_click("x", '//*[@id="examDialog"]/div/div/div[2]/div/div[4]/div/div[2]/a[1]')  # 点击添加选项
            self.find_element_input("x", '//*[@id="input_Radio2"]', 'rope skipping')  # 输入第三个选项
            self.find_element_click("x", '//*[@id="examDialog"]/div/div/div[2]/div/div[4]/div/div[2]/a[1]')  # 点击添加选项
            self.find_element_input('x', '//*[@id="input_Radio3"]', 'basketball')  # 输入第四个选项
            time.sleep(1)

            js = 'document.getElementsByName("optionGroupRadio")[0].click();'  # 设置第一个选项为正确选项
            self.driver.execute_script(js)
            time.sleep(1)
            self.find_element_click('x', '//*[@id="examDialog"]/div/div/div[3]/button[1]')  # 点击确定按钮
            time.sleep(1)
            actual_result = self.find_element_text('x',
                                                   '/html/body/div[1]/div[2]/main/div/div[2]/div[2]/div[3]/div[2]/table/tbody[2]/tr/td[3]')
            self.deprint('创建试题"' + actual_result.encode("utf-8") + '"完成')
            return actual_result
        except:
            try:
                self.deprint('开始创建试题')
                self.wait_is_visible('x',
                                     '/html/body/div[1]/div[2]/main/div/div[2]/div[2]/div[1]/div[1]/ul/li[1]/a')  # 点击默认题库
                self.wait_is_visible('x',
                                     '/html/body/div[1]/div[2]/main/div/div[2]/div[2]/div[2]/div/div[6]/button')  # 点击创建试题
                time.sleep(1)
                self.deprint('点击创建试题成功')
                self.find_element_input("x", '//*[@id="examDialog"]/div/div/div[2]/div/div[3]/div/input',
                                        "What is your favorite sport?")  # 输入试题内容
                self.find_element_input("x", '//*[@id="input_Radio0"]', 'badminton')  # 输入第一个选项
                self.find_element_click("x",
                                        '//*[@id="examDialog"]/div/div/div[2]/div/div[4]/div/div[2]/a[1]')  # 点击添加选项
                self.find_element_input("x", '//*[@id="input_Radio1"]', 'table tennis')  # 输入第二个选项

                self.find_element_click("x",
                                        '//*[@id="examDialog"]/div/div/div[2]/div/div[4]/div/div[2]/a[1]')  # 点击添加选项
                self.find_element_input("x", '//*[@id="input_Radio2"]', 'rope skipping')  # 输入第三个选项
                self.find_element_click("x",
                                        '//*[@id="examDialog"]/div/div/div[2]/div/div[4]/div/div[2]/a[1]')  # 点击添加选项
                self.find_element_input('x', '//*[@id="input_Radio3"]', 'basketball')  # 输入第四个选项
                time.sleep(1)

                js = 'document.getElementsByName("optionGroupRadio")[0].click();'  # 设置第一个选项为正确选项
                self.driver.execute_script(js)
                time.sleep(1)
                self.find_element_click('x', '//*[@id="examDialog"]/div/div/div[3]/button[1]')  # 点击确定按钮
                time.sleep(1)
                actual_result = self.find_element_text('x',
                                                       '/html/body/div[1]/div[2]/main/div/div[2]/div[2]/div[3]/div[2]/table/tbody[2]/tr/td[3]')
                self.deprint('创建试题"' + actual_result.encode("utf-8") + '"完成')
                return actual_result
            except:
                self.deprint("用例执行失败")



    #删除试题
    def delete_question(self):
        try:
            self.deprint('删除试题')
            #        self.dominant_wait('x', '/html/body/div[1]/div[2]/div[1]/div[2]/div/div[1]/ul/li[1]/a')  # 点击默认题库
            time.sleep(1)
            str1 = self.find_element_text('x','/html/body/div[1]/div[2]/main/div/div[2]/div[2]/nav/div/span[2]')
            totalNum=str1.split("共")[1].split("条")[0]
            self.find_element_click('x',
                                    '/html/body/div[1]/div[2]/main/div/div[2]/div[2]/div[3]/div[2]/table/tbody[2]/tr/td[5]/span/a')  # 点击试题后面的“更多”按钮
            self.find_element_click('x',
                                    '/html/body/div[1]/div[2]/main/div/div[2]/div[2]/div[3]/div[2]/table/tbody[2]/tr/td[5]/span/ul/li[2]/a')  # 点击删除按钮
            time.sleep(1)
            self.find_element_click('x', '//*[@id="deleteExmAlert"]/div/div/div[3]/button[2]')  # 点击继续按钮
            time.sleep(1)

            str2=self.find_element_text('x', '/html/body/div[1]/div[2]/main/div/div[2]/div[2]/nav/div/span[2]')
            afterDeleteTotalNum=str2.split("共")[1].split("条")[0]
            if int(totalNum) == (int(afterDeleteTotalNum) + 1):
                self.deprint('试题删除成功')
            else:
                self.deprint('试题删除失败')
        except:
            try:
                self.deprint('删除试题')
                #        self.dominant_wait('x', '/html/body/div[1]/div[2]/div[1]/div[2]/div/div[1]/ul/li[1]/a')  # 点击默认题库
                time.sleep(1)
                firstQuestion = self.find_element_text('x',
                                                       '/html/body/div[1]/div[2]/main/div/div[2]/div[2]/div[3]/div[2]/table/tbody[2]/tr/td[3]')  # 获取第一个试题的标题
                str1 = self.find_element_text('x', '/html/body/div[1]/div[2]/main/div/div[2]/div[2]/nav/div/span[2]')
                totalNum = str1.split("共")[1].split("条")[0]
                self.find_element_click('x',
                                        '/html/body/div[1]/div[2]/main/div/div[2]/div[2]/div[3]/div[2]/table/tbody[2]/tr/td[5]/span/a')  # 点击试题后面的“更多”按钮
                self.find_element_click('x',
                                        '/html/body/div[1]/div[2]/main/div/div[2]/div[2]/div[3]/div[2]/table/tbody[2]/tr/td[5]/span/ul/li[2]/a')  # 点击删除按钮
                time.sleep(1)
                self.find_element_click('x', '//*[@id="deleteExmAlert"]/div/div/div[3]/button[2]')  # 点击继续按钮
                time.sleep(1)

                str2 = self.find_element_text('x', '/html/body/div[1]/div[2]/main/div/div[2]/div[2]/nav/div/span[2]')
                afterDeleteTotalNum = str2.split("共")[1].split("条")[0]
                if int(totalNum) == (int(afterDeleteTotalNum) + 1):
                    self.deprint('试题删除成功')
                else:
                    self.deprint('试题删除失败')
            except:
                self.deprint("用例执行失败")




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
    object.delete_question()
    object.quit()