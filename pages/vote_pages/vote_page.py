# -*- coding: utf-8 -*-
'''
Created on 2018-07-16
@author: 尤梅枝
'''
from pages.common_pages.base import BasePage
from pages.wechat.create_material import Creat_media
from pages.common_pages.login_page import LoginPage
from pages.common_pages.choose_page import ChoosePage
from pages.common_pages.driver import brower
from selenium.webdriver.common.action_chains import ActionChains
import time
class Create_vote(BasePage):
    #创建投票
    def new_vote(self):
        self.deprint("开始执行创建投票用例")
        self.wait_is_visible('x','/html/body/div[1]/div[2]/main/div/div[1]/div/div[2]/div/button/span') #点击创建投票按钮
        title=u'自动化创建投票'+self.nowtime()
        self.element_value_input('id','pollTitle',title) #输入投票标题
        self.wait_is_visible('id','dropdownMenu3') #点击参与方式下拉框
        self.wait_is_visible('x','//*[@aria-labelledby="dropdownMenu3"]/ul/li[1]') #选择全部用户可参与方式
        self.wait_is_visible('x','//*[@class="tags"]/div[2]')
        self.wait_is_visible('x','//*[@class="tags"]/div[3]/div/span[1]') #选择标签
        self.scrollbar('bottom')
        self.wait_is_visible('x','/html/body/div[1]/div[2]/main/div/div/div/div[2]/div/button') #点击保存按钮
        self.wait_is_visible('x','//*[@id="alertCommon"]/div/div/div[3]/button') #点击确定弹窗
    def setItems(self):
        self.wait_is_visible('x','//*[@id="left-menu"]/ul/li[2]/ul/li[1]/a') #选择单选题
        self.element_value_input('x', '//question-items/div[1]/div/text-field/div[1]/div[1]/div[1]/input', u'你的爱好？') #输入题目标题
        self.wait_is_visible('link',u'添加选项')
        self.element_value_input('x','//question-items/div[1]/div/text-field/div[1]/div[1]/div[4]/div[1]/div[1]/div/input',u'看电影') #输入题目选项
        self.wait_is_visible('link', u'添加选项')
        self.element_value_input('x', '//question-items/div[1]/div/text-field/div[1]/div[1]/div[4]/div[2]/div[1]/div/input', u'打乒乓') #输入题目选项
        self.wait_is_visible('link', u'添加选项')
        self.element_value_input('x','//question-items/div[1]/div/text-field/div[1]/div[1]/div[4]/div[3]/div[1]/div/input',u'睡觉觉') #输入题目选项
        self.wait_is_visible('x','/html/body/div[1]/div[2]/div[2]/div/div/div[2]/div/div/div[2]/div/button') #点击保存按钮
        self.wait_is_visible('x','//*[@id="alertCommon"]/div/div/div[3]/button') #点击确定弹窗
    def browse_vote(self):
        time.sleep(3)
        text=self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/main/div/div/div[1]/div[2]/div[2]/div[2]/span') #找到投票获取链接元素
        url1=text.get_attribute('innerText') #获取链接内容，链接内容后携带了【获取链接】部分文本
        url2=url1[0:28]      #截取文本，去掉【获取链接】
        # print "截取前的链接地址："+ url1
        # print "投票链接地址为："+url2
        js = 'window.open("' + url2 + '")'  #新开创建打开投票链接地址
        self.driver.execute_script(js)
        self.driver.switch_to.window(self.driver.window_handles[-1])  #切换到新开的窗口
        self.wait_is_visible('x','//*[@id="questionContainer"]/div[1]/div/div/ul/li[1]/label') #选择投票选项
        self.wait_is_visible('x','//*[@id="questionContainer"]/div[2]/input') #提交投票
        time.sleep(2)
        text2=self.find_element_text('x','/html/body/div/div/div/div[1]/p[1]') #获取投票提交结果页的提示信息作为判断是否成功的依据
        # print text2
        return text2

    def edit_vote(self):
        # self.wait_is_visible('x','/html/body/div[1]/div[2]/main/div/div[2]/div/div[1]/div/div[2]')
        element=self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/main/div/div[2]/div/div[1]/div/div[2]')
        ActionChains(self.driver).move_to_element(element).perform()
        time.sleep(2)
        self.wait_is_visible('x','/html/body/div[1]/div[2]/main/div/div[2]/div/div[1]/div/div[1]/div[2]/a[3]/div/span')
        # self.wait_is_visible('x','//*[@id="alertCommon"]/div/div/div[3]/button[2]')
        # self.scrollbar('bottom')
        # self.wait_is_visible('x','/html/body/div[1]/div[2]/main/div/div/div/div[2]/div/button')
        # self.wait_is_visible('x', '//*[@id="alertCommon"]/div/div/div[3]/button')  # 点击确定弹窗
        # self.wait_is_visible('x', '/html/body/div[1]/div[2]/div[2]/div/div/div[2]/div/div/div[2]/div/button')  # 点击保存按钮
        # self.wait_is_visible('x', '//*[@id="alertCommon"]/div/div/div[3]/button')  # 点击确定弹窗






if __name__ == '__main__':


    driver = brower()
    login= LoginPage(driver)
    login.login()
    chooseP = ChoosePage(driver)
    chooseP.click_menu_bt("1")
    test=Creat_media(driver)
    test.enter_vote()
    vote=Create_vote(driver)
    vote.new_vote()
    vote.setItems()
    vote.browse_vote()