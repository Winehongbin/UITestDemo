# -*- coding: utf-8 -*-
from datetime import datetime
# from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import selenium.webdriver.support.ui as ui
from selenium.webdriver.support.select import Select
import time

#页面操作基础类
class BasePage(object):
    base_url="https://tenant.smarket.net.cn"
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
    """
    #定位元素并单击,对单击操作做扩展
    driver.implicitly_wait() :隐形等待，设定时间是秒
    find_element_by_xpath():按xpath定位元素
    find_element_by_class_name():按name定位元素
    find_element_by_id():按id定位元素
    find_element_by_link_text（）:按文本链接定位
    find_element_by_tag_name():html 本质就是tag来定义实现不同的功能，每一个元素都是一个tag。

    """
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
            self.driver.find_element_by_tag_name(location).send_keys(value)
        if method == "Plink":
            self.driver.find_element_by_partial_link_text(location).send_keys(value)
        if method == "css":
            self.driver.find_element_by_css_selector(location).send_keys(value)
    #发现元素并单击
    def find_element_click(self,method,location):
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
    # 发现元素，返回文本值
    def find_element_text(self,method,location):
        if method =="x":
            self.driver.implicitly_wait(3)
            text = self.driver.find_element_by_xpath(location).text
            return text
        if method =="class":
            self.driver.implicitly_wait(3)
            text = self.driver.find_element_by_class_name(location).text
            return text
        if method == "id":
            text = self.driver.find_element_by_id(location).text
            return text
        if method == "name":
            self.driver.implicitly_wait(3)
            text = self.driver.find_element_by_name(location).text
            return text
        if method == "link":
            self.driver.implicitly_wait(3)
            text = self.driver.find_element_by_link_text(location).text
            return text
        if method == "tag":
            self.driver.implicitly_wait(3)
            text = self.driver.find_element_by_tag_name(location).text
            return text
        if method == "Plink":
            self.driver.implicitly_wait(3)
            text = self.driver.find_element_by_partial_link_text(location).text
            return text
        if method == "css":
            self.driver.implicitly_wait(3)
            text = self.driver.find_element_by_css_selector(location).text
            return text
    #通过输入框的属性获取属性值
    def find_element_AttributeText(self,method,location,attributeName):
        if method == "x":
            attributeValue = self.driver.find_element_by_xpath(location).get_attribute(attributeName)
            return attributeValue
        if method =="class":
            attributeValue = self.driver.find_element_by_class_name(location).get_attribute(attributeName)
            return attributeValue
        if method == "id":
            attributeValue = self.driver.find_element_by_id(location).get_attribute(attributeName)
            return attributeValue
        if method == "name":
            attributeValue = self.driver.find_element_by_name(location).get_attribute(attributeName)
            return attributeValue
        if method == "link":
            attributeValue = self.driver.find_element_by_link_text(location).get_attribute(attributeName)
            return attributeValue
        if method == "tag":
            attributeValue = self.driver.find_element_by_tag_name(location).get_attribute(attributeName)
            return attributeValue
        if method == "Plink":
            attributeValue = self.driver.find_element_by_partial_link_text(location).get_attribute(attributeName)
            return attributeValue
        if method == "css":
            attributeValue = self.driver.find_element_by_css_selector(location).get_attribute(attributeName)
            return attributeValue
    #发现元素，并输入值
    def find_element_input(self,method,location,value):
        if method =="x":
            # self.driver.find_element_by_xpath(location).clear()
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
            self.driver.find_element_by_tag_name(location).send_keys(value)
        if method == "Plink":
            self.driver.find_element_by_partial_link_text(location).send_keys(value)
        if method == "css":
            # self.driver.find_element_by_css_selector(location).clear()
            self.driver.find_element_by_css_selector(location).send_keys(value)
    #显性等待
    """
    显性等待，
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC

    # 显性等待（2），https://www.cnblogs.com/yoyoketang/p/6517477.html 可参考
    # element = WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_css_selector(css_path))
    """
    def dominant_wait(self,method,location):
        if method == "x":
            element = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, location)))
            element.click()
        if method == "css":
            element = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, location)))
            element.click()
    # 一直等待某元素可见，默认超时10秒，ui需要import selenium.webdriver.support.ui as ui
    # def wait_is_visible(self,method,location):
    #
    #     isFind = False
    #     for n in range(0, 20):
    #         time.sleep(0.5)
    #         # 如果找个元素，打印内容，同时break跳出循环
    #         element = None
    #         if method == "x":
    #             self.driver.implicitly_wait(3)
    #             element = self.driver.find_element_by_xpath(location)
    #         if method == "class":
    #             self.driver.implicitly_wait(3)
    #             element = self.driver.find_element_by_class_name(location)
    #         if method == "id":
    #             element = self.driver.find_element_by_id(location)
    #         if method == "name":
    #             self.driver.implicitly_wait(3)
    #             element = self.driver.find_element_by_name(location)
    #         if method == "link":
    #             self.driver.implicitly_wait(3)
    #             element = self.driver.find_element_by_link_text(location)
    #         if method == "tag":
    #             self.driver.implicitly_wait(3)
    #             element = self.driver.find_element_by_tag_name(location)
    #         if method == "Plink":
    #             self.driver.implicitly_wait(3)
    #             element = self.driver.find_element_by_partial_link_text(location)
    #         if method == "css":
    #             self.driver.implicitly_wait(3)
    #             element = self.driver.find_element_by_css_selector(location)
    #
    #         if element:
    #             # print "找到了"
    #             element.click()
    #             isFind = True
    #             break
    #     if isFind != True:
    #         print "没找到元素"
    # 一直等待某个元素消失，默认超时10秒
    def is_not_visible(locator, timeout=10):
        try:
            ui.WebDriverWait(driver, timeout).until_not(EC.visibility_of_element_located((By.XPATH, locator)))
            return True
        except TimeoutException:
            return False
    #句柄的获得
    def switch_handle(self,value):
        try:
            if value == "0":
                asd = driver.window_handles
                driver.switch_to_window(asd[0])
            if value == "-1":
                # -1就是当前的窗口
                qwe = driver.window_handles
                driver.switch_to_window(qwe[-1])
            if value == "-2":
                qwe = driver.window_handles
                driver.switch_to_window(qwe[-2])
        except IOError:
                print "handle值有误！"
    #按一定格式获取当前时间，需要from datetime import datetime
    def deprint(self,content):
        dt = datetime.now()
        print datetime.strftime(dt, '%Y-%m-%d %H:%M:%S')+"："+content
    #按YYYY-MM-DD HH:MM:SS格式获取当前时间，并返回
    def nowtime(self):
        dt = datetime.now()
        time=datetime.strftime(dt,'%Y-%m-%d %H:%M:%S')
        return time
        print time
    #按一定格式获取当前时间，需要from datetime import datetime
    def printime(self):
        dt = datetime.now()
        strnow = datetime.strftime(dt, '%Y-%m-%d %H_%M_%S')
        return strnow
    def Select_Value(self,location,value):
        sel = self.driver.find_element_by_xpath(location)
        Select(sel).select_by_value(value)

    #20秒内每间隔0.5秒寻找一次元素
    def wait_is_visible(self, method, location):
        isFind = False
        for n in range(0, 20):
            time.sleep(0.5)
            # 如果找个元素，打印内容，同时break跳出循环
            element = None
            if method == "x":
                self.driver.implicitly_wait(3)
                element = self.driver.find_element_by_xpath(location)
            if method == "class":
                self.driver.implicitly_wait(3)
                element = self.driver.find_element_by_class_name(location)
            if method == "id":
                element = self.driver.find_element_by_id(location)
            if method == "name":
                self.driver.implicitly_wait(3)
                element = self.driver.find_element_by_name(location)
            if method == "link":
                self.driver.implicitly_wait(3)
                element = self.driver.find_element_by_link_text(location)
            if method == "tag":
                self.driver.implicitly_wait(3)
                element = self.driver.find_element_by_tag_name(location)
            if method == "Plink":
                self.driver.implicitly_wait(3)
                element = self.driver.find_element_by_partial_link_text(location)
            if method == "css":
                self.driver.implicitly_wait(3)
                element = self.driver.find_element_by_css_selector(location)

            if element:
                # print "找到了"
                element.click()
                isFind = True
                break
        if isFind != True:
            print "没找到元素"

if __name__ == '__main__':
    A = BasePage(1)
    A.deprint("需要打印的内容")
    time=A.nowtime()
    print time