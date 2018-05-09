# -*- coding: utf-8 -*-
import os
from selenium import webdriver
#设置驱动获取浏览器对象

def brower():

    # type: () -> object
    cur_path = os.path.abspath(os.path.dirname(__file__)) #os.path.basename(path):返回所给路径path的最底层路径名或者是文件名；
    # os.path.dirname(__file__):返回脚本的路径
    root_path = os.path.split(cur_path)[0]  #os.path.split(curPath)[0]:path分割成目录
    root_path = os.path.split(root_path)[0]
    driver_path = root_path + "\common\common_function\chromedriver.exe"
    """
    driverOptions = webdriver.ChromeOptions()
    driverOptions.add_argument(r"user-data-dir=D:\chromeCache")
    driver = webdriver.Chrome(driver_path,0,driverOptions)
    """
    driver = webdriver.Chrome(driver_path)
    driver.implicitly_wait(10)
    driver.maximize_window()  #放大窗口
    return driver

if __name__ == '__main__':
    driver = brower()
