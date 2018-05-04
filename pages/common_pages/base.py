# -*- coding: utf-8 -*-
from datetime import datetime
# from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import selenium.webdriver.support.ui as ui
#页面操作基础类
class BasePage(object):
    base_url="https://tenant.smarket.net.cn"
    #__init__()方法对参数进行初始化  五一
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
    def wait_is_visible(self,method,locator, timeout=20):

        try:
            if method == 'x':
                element = ui.WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((By.XPATH, locator)))
                element.click()
            if method == 'css':
                element = ui.WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((By.CSS_SELECTOR, locator)))
                element.click()
            return True

        #TimeoutException 需要from selenium.common.exceptions import TimeoutException
        except TimeoutException:
             return False
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
    def deprint(self):
        dt = datetime.now()
        strnow = datetime.strftime(dt, '%Y-%m-%d %H:%M:%S')
        return strnow
    #按一定格式获取当前时间，需要from datetime import datetime
    def printime(self):
        dt = datetime.now()
        strnow = datetime.strftime(dt, '%Y-%m-%d %H_%M_%S')
        return strnow