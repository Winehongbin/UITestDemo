# -*- coding: utf-8 -*-
from pages.common_pages.base import BasePage
from pages.common_pages.login_page import LoginPage
import time
from pages.common_pages.choose_page import ChoosePage
from pages.common_pages.driver import brower
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
# from pages.webinar_pages.create_meeting import Webinar_Create
from selenium.webdriver.support import expected_conditions as EC

class Webinar_IndexPage(BasePage):

    # 打开线上会的首页
    def index_webinar(self):
        self.deprint("进入线上会首页")
        # self.wait_is_visible('x','/html/body/div[1]/div[1]/ul/li[1]/h2/a')
        element = WebDriverWait(self.driver,10,0.5).until(EC.presence_of_all_elements_located((By.XPATH,'/html/body/div[1]/div[1]/ul/li[1]/h2/a')))
        # print element
        if element == 1 :
            self.wait_is_visible('x','/html/body/div[1]/div[1]/ul/li[1]/h2/a')
        else:
            time.sleep(3)
            self.wait_is_visible('x', '/html/body/div[1]/div[1]/ul/li[1]/h2/a')

    # 进入直播会议列表页面
    def webinar_list(self):
        self.deprint("进入直播会议列表页面")
        time.sleep(2)
        # 点击直播菜单
        self.wait_is_visible('x','//*[@id="collapse2"]/li[1]/a')

    # 点击直播列表页面的创建会议按钮
    def list_create(self):
        self.deprint("点击直播列表创建会议按钮")
        self.wait_is_visible('x','/html/body/div[1]/div[2]/div/div[2]/button')
        time.sleep(5)

    # 点击首页的创建会议按钮
    def index_create(self):
        self.deprint("点击首页创建会议按钮")
        self.wait_is_visible('x', '/html/body/div[1]/div[2]/div/button')
        time.sleep(3)

    # 选择直播会议
    def choose_meeting(self):
        self.deprint('选择一场直播中的会议')
        time.sleep(3)
        isFind = False
        for i in range(1,5):
            status1 = self.find_element_text('x','/html/body/div[1]/div[2]/div/section/ul/li['+str(i)+']/div/div[2]/p[1]/span[2]')
            try:
                if status1 == u'直播中' :
                    wtitle = self.find_element_text('x', '/html/body/div[1]/div[2]/div/section/ul/li[' + str(i) + ']/div/div[2]/p[1]/span[1]')
                    self.wait_is_visible('x','/html/body/div[1]/div[2]/div/section/ul/li['+str(i)+']/div/a')
                    self.deprint('进入直播中的会议的详情页面')
                    # return isFind
                    # break
            except:
                continue

            if isFind != True:
                self.list_create()
                self.create_meeting()
        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.driver.implicitly_wait(10)

    # 首页创建线上会
    def create_meeting(self):
        self.deprint("开始创建线上会")
        titlet = self.nowtime()
        wrtitle = u'自动化创建测试会议' + str(titlet)
        time.sleep(5)
        # 填写会议信息：会议标题
        self.element_value_input('x', '//*[@id="title"]', wrtitle)
        time.sleep(1)
        # self.element_value_input('id','title',wrtitle)
        # 主办方
        self.element_value_input('x', '//*[@id="sponser"]', u'校')
        # 选择注册表单
        self.nameofform(u"新建注册表单(9)")
        # self.element_value_input('x','/html/body/p',u'会议简介信息')
        # 选择数据权限（下拉类型的字段）
        self.element_click('x', '//*[@id="webinarModal"]/div[1]/div/div[2]/div[2]/div[8]/div[1]/div/div/div/button')
        self.element_click('x', '//*[@id="webinarModal"]/div[1]/div/div[2]/div[2]/div[8]/div[1]/div/div/div/ul/li[2]/a')
        # 点击保存按钮
        self.element_click('x', '//*[@id="save"]')

        # 保存会议后，判断去设置按钮是否显示，显示后，点击去设置
        element = WebDriverWait(self.driver, 10, 0.5).until(
            EC.presence_of_all_elements_located((By.XPATH, '//*[@id="webinarModal"]/div[1]/div/div[3]/a')))
        if element == 1:
            self.wait_is_visible('x', '//*[@id="webinarModal"]/div[1]/div/div[3]/a')
        else:
            time.sleep(20)
            self.wait_is_visible('x', '//*[@id="webinarModal"]/div[1]/div/div[3]/a')

        # 获取下一个窗口句柄，跳转到会议详情页面
        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.driver.implicitly_wait(10)
        time.sleep(5)
        vwrtitle = self.find_element_text('x', '/html/body/div[1]/div[2]/div[2]/div/div[2]/div/ul/li[1]/span')

        # 判断会议标题是否一致
        if wrtitle == vwrtitle:
            self.deprint("创建会议成功"),
        else:
            self.deprint("创建会议失败")

    # 遍历注册表单
    def nameofform(self, form_name):

        # 点击选择
        self.element_click('x', '//*[@id="webinarModal"]/div[1]/div/div[2]/div[2]/div[5]/div[1]/div/div/div/button')

        for num in range(1, 100):  # 遍历选项，选中form_name 因为遍历100遍，及100个下表元素。如果没有正确选中，很有可能找不到元素，报错。
            ele = '//*[@id="webinarModal"]/div[1]/div/div[2]/div[2]/div[5]/div[1]/div/div/div/ul/li[' + str(num) + ']/a'
            # print ele
            all_form_name = self.find_element_text("x", ele)  # 获各个注册单名称
            # print all_form_name
            if all_form_name == form_name:  # 判断对应注册单的名称，点击选择
                self.element_click("x", ele)
                break


if __name__ == '__main__':
    dr = brower()
    o = LoginPage(dr)
    o.login()
    o = ChoosePage(dr)
    time.sleep(3)
    o.click_menu_bt('8')
    o =  Webinar_IndexPage(dr)
    time.sleep(3)
    o.webinar_list()
    o.choose_meeting()
    o.quit()




