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
class Create_vote(BasePage):
    #创建投票
    def new_vote(self):
        self.deprint("开始执行创建投票用例")
        self.wait_is_visible('x','/html/body/div[1]/div[2]/main/div/div[1]/div/div[2]/div/button/span')
        title=u'自动化创建投票'+self.nowtime()
        self.element_value_input('id','pollTitle',title)
        self.wait_is_visible('id','dropdownMenu3')
        self.wait_is_visible('x','//*[@aria-labelledby="dropdownMenu3"]/ul/li[1]')
        self.wait_is_visible('x','//*[@class="tags"]/div[2]')
        self.wait_is_visible('x','//*[@class="tags"]/div[3]/div/span[1]')
        self.scrollbar('bottom')
        self.wait_is_visible('x','/html/body/div[1]/div[2]/main/div/div/div/div[2]/div/button')
        self.wait_is_visible('x','//*[@id="alertCommon"]/div/div/div[3]/button')
    def setItems(self):
        self.wait_is_visible('x','//*[@id="left-menu"]/ul/li[2]/ul/li[1]/a')
        self.element_value_input('x', '//question-items/div[1]/div/text-field/div[1]/div[1]/div[1]/input', u'你的爱好？')
        self.wait_is_visible('link',u'添加选项')
        self.element_value_input('x','//question-items/div[1]/div/text-field/div[1]/div[1]/div[4]/div[1]/div[1]/div/input',u'看电影')
        self.wait_is_visible('link', u'添加选项')
        self.element_value_input('x', '//question-items/div[1]/div/text-field/div[1]/div[1]/div[4]/div[2]/div[1]/div/input', u'打乒乓')
        self.wait_is_visible('link', u'添加选项')
        self.element_value_input('x','//question-items/div[1]/div/text-field/div[1]/div[1]/div[4]/div[3]/div[1]/div/input',u'睡觉觉')
        self.wait_is_visible('x','/html/body/div[1]/div[2]/div[2]/div/div/div[2]/div/div/div[2]/div/button')
        self.wait_is_visible('x','//*[@id="alertCommon"]/div/div/div[3]/button')
    def browse_vote(self):
        url=self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/main/div/div/div[1]/div[2]/div[2]/div[2]/span/text()')
        print url
    def edit_vote(self):
        self.wait_is_visible('x','/html/body/div[1]/div[2]/main/div/div[2]/div/div[1]/div/div[2]')
        element=self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/main/div/div[2]/div/div[1]/div/div[3]/div[1]/p[1]/span[2]')
        ActionChains(self.driver).move_to_element(element).perform()
        # self.wait_is_visible('x','/html/body/div[1]/div[2]/main/div/div[2]/div/div[1]/div/div[3]/div[1]/p[1]/span[2]')


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