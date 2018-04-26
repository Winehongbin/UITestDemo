# -*- coding: utf-8 -*-
from datetime import datetime

#页面操作基础类
class BasePage(object):
    base_url="https://uat-tenant.smarket.net.cn"

    #__init__()方法对参数进行初始化
    def __init__(self,selenium_driver,base_url=base_url,parent=None):
        self.base_url = base_url
        self.driver = selenium_driver
        self.timeout=30
        self.parent = parent
        self.url=""

    def _open(self,url):
        self.url = self.base_url + url
        self.driver.get(self.url)
        self.driver.implicitly_wait(self.timeout)

    def open(self):
        self._open(self.url)

    #退出浏览器
    def quit(self):
        self.driver.quit()

    #关闭当前页
    def close(self):
        self.driver.close()

    #定位元素并单击,对单击操作做扩展
    def element_click(self,method,location):

        if method =="x":
            self.driver.implicitly_wait(3)
            self.driver.find_element_by_xpath(location).click()
        if method =="class":
            self.driver.implicitly_wait(3)
            self.driver.find_element_by_class_name(location).click()
        if method == "id":
            self.driver.find_element_by_id(location).click()
        if method == "name":
            self.driver.implicitly_wait(3)
            self.driver.find_element_by_name(location).click()
        if method == "link":
            self.driver.implicitly_wait(3)
            self.driver.find_element_by_link_text(location).click()
        if method == "tag":
            self.driver.implicitly_wait(3)
            self.driver.find_element_by_tag_name(location).click()
        if method == "Plink":
            self.driver.implicitly_wait(3)
            self.driver.find_element_by_partial_link_text(location).click()
        if method == "css":
            self.driver.implicitly_wait(3)
            self.driver.find_element_by_css_selector(location).click()

    #定位元素并输入值，输入操作做扩展
    def element_value_input(self,method,location,value):
        global driver
        if method =="x":
            self.driver.find_element_by_xpath(location).send_keys(value)
        if method =="class":
            self.driver.find_element_by_class_name(location).send_keys(value)
        if method == "id":
            self.driver.find_element_by_id(location).send_keys(value)
        if method == "name":
            self.driver.find_element_by_name(location).send_keys(value)
        if method == "link":
            self.driver.find_element_by_link_text(location).send_keys(value)
        if method == "tag":
            self.driver.find_element_by_tag_name(location).send_keys(self.value)
        if method == "Plink":
            self.driver.find_element_by_partial_link_text(location).send_keys(self.value)
        if method == "css":
            self.driver.find_element_by_css_selector(location).send_keys(self.value)

    #定位元素并输入操作


    # 当前时间
    def deprint(self):
        dt = datetime.now()
        strnow = datetime.strftime(dt, '%Y-%m-%d %H:%M:%S')
        return strnow