# -*- coding: utf-8 -*-
import os
from selenium import webdriver
#设置驱动获取浏览器对象
def brower():
    # type: () -> object
    cur_path = os.path.abspath(os.path.dirname(__file__))
    root_path = os.path.split(cur_path)[0]
    print root_path
    root_path = os.path.split(root_path)[0]
    driver_path = root_path + "\common\common_function\chromedriver.exe"
    """五一
    driverOptions = webdriver.ChromeOptions()
    driverOptions.add_argument(r"user-data-dir=D:\chromeCache")
    """
    print driver_path
    # 五一
    # driver = webdriver.Chrome(driver_path,0,driverOptions)
    driver = webdriver.Chrome(driver_path)
    driver.implicitly_wait(10)
    driver.maximize_window()
    # driver.find_element_by_xpath("//*[@id="login"]/form/div[1]/input")
    return driver

if __name__ == '__main__':
    driver = brower()
    # dr.quit()/