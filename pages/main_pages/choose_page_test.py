# -*- coding: utf-8 -*-
import time
from pages.common_pages.base import BasePage
from pages.common_pages.driver import brower
from pages.common_pages.login_page import LoginPage
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoSuchWindowException
from selenium.common.exceptions import TimeoutException
class ChoosePageTest(BasePage):

    #测试每个app是否正常进入主页面
    def click_menu_bt(self, button_pos):
        winHandles = self.driver.window_handles
        for handle in winHandles:
            print u"开始循环时句柄" + handle
        time.sleep(3)
        # handleNow = self.driver.current_window_handle  # 获得当前窗口
        # print u"当前句柄" + handleNow
        # self.driver.switch_to_window(handleNow)
        all_handles = self.driver.window_handles
        self.driver.switch_to.window(all_handles[0])
        self.driver.implicitly_wait(30)
        self.driver.set_page_load_timeout(20)
        self.driver.maximize_window()
        try:
            css_path = "#sortContainer > a:nth-child(" + str(button_pos) + ")"  # 把按钮位置设为参数获取
            self.wait_is_visible('css', css_path)  #点击应用按钮
        except TimeoutException:
            self.driver.switch_to.window(self.driver.window_handles[-1])
            self.close()
            return int(0)


        time.sleep(3)
        # self.driver.switch_to.window(self.driver.window_handles[-1])
        flag = 0
        try:
            if button_pos == 1:
                print self.driver.window_handles[-1]
                self.driver.switch_to.window(self.driver.window_handles[-1])
                #获取应用页面的数据统计元素
                elem = self.find_element_text('x', '//*[@id="g-right"]/section/div/div[4]/div[1]')
                #elem = self.find_element_text('x', '//*[@id="g-right"]/section/div/div[2]/div[1]')
                time.sleep(10)
                self.deprint(u"测试应用：" + elem)
                if elem == '数据统计':
                    # 访问成功
                    # flag = 1
                    self.close()
                    return int(1)
                else:
                    # 访问失败
                    # flag = 0
                    self.close()
                    return int(0)
            elif button_pos == 2:
                print self.driver.window_handles[-1]
                self.driver.switch_to.window(self.driver.window_handles[-1])
                # 获取应用页面的创建场景元素
                elem = self.find_element_text('x', '//*[@id="main"]/div[3]/div[3]/h2/a')
                time.sleep(10)
                self.deprint(u"测试应用：" + elem)
                if elem == '创建场景':
                    # flag = 1
                    self.close()
                    return int(1)
                else:
                    # flag = 0
                    self.close()
                    return int(0)
            elif button_pos == 3:
                print self.driver.window_handles[-1]
                self.driver.switch_to.window(self.driver.window_handles[-1])
                # 获取应用页面的登陆按钮元素
                elem = self.find_element_text('x', '/html/body/div/form/div/div[2]/button')
                time.sleep(10)
                self.deprint(u"测试应用：" + elem.replace(' ',''))
                if elem.replace(' ','') == '登录':
                    # flag = 1
                    self.close()
                    return int(1)
                else:
                    # flag = 0
                    self.close()
                    return int(0)
            elif button_pos == 4:
                print self.driver.window_handles[-1]
                self.driver.switch_to.window(self.driver.window_handles[-1])
                # 获取应用页面的还没注册九枝兰?元素
                elem = self.find_element_text('x', '/html/body/main/div/div/div/div/div[2]/div/div[2]/span')
                time.sleep(10)
                self.deprint(u"测试应用：" + elem.replace(' ',''))
                if elem.replace(' ','') == '还没注册九枝兰?':
                    # flag = 1
                    self.close()
                    return int(1)
                else:
                    # flag = 0
                    self.close()
                    return int(0)
            elif button_pos == 5:
                print self.driver.window_handles[-1]
                self.driver.switch_to.window(self.driver.window_handles[-1])
                # 获取应用页面的展位管理元素
                elem = self.find_element_text('x', '/html/body/div[2]/div/div[1]/div/ul/li/a/span')
                time.sleep(10)
                self.deprint(u"测试应用：" + elem.replace(' ',''))
                if elem.replace(' ','') == '展位管理':
                    # flag = 1
                    self.close()
                    return int(1)
                else:
                    # flag = 0
                    self.close()
                    return int(0)
            #数据监测工具有问题，页面不能访问
            elif button_pos == 6:
                print self.driver.window_handles[-1]
                self.driver.switch_to.window(self.driver.window_handles[-1])
                # 获取应用页面的回到首页元素
                elem = self.find_element_text('x', '/html/body/div/a')
                time.sleep(10)
                self.deprint(u"测试应用：" + elem.replace(' ',''))
                if elem.replace(' ','') == '回到首页':
                    # flag = 1
                    time.sleep(2)
                    self.close()
                    return int(1)
                else:
                    # flag = 0
                    time.sleep(2)
                    self.close()
                    return int(0)
            elif button_pos == 7:
                print self.driver.window_handles[-1]
                self.driver.switch_to.window(self.driver.window_handles[-1])
                elem = self.find_element_text('x', '//*[@id="mainRight"]/div[2]/div[1]/div[1]/span')
                time.sleep(10)
                self.deprint(u"测试应用：" + elem.replace(' ',''))
                if elem.replace(' ','') == '历史数据统计':
                    # flag = 1
                    self.close()
                    return int(1)
                else:
                    # flag = 0
                    self.close()
                    return int(0)
            elif button_pos == 8:
                print self.driver.window_handles[-1]
                self.driver.switch_to.window(self.driver.window_handles[-1])
                elem = self.find_element_text('x', '/html/head/title')
                time.sleep(10)
                self.deprint(u"测试应用：" + elem.replace(' ',''))
                if elem.replace(' ','') == '线下会':
                    # flag = 1
                    self.close()
                    return int(1)
                else:
                    # flag = 0
                    self.close()
                    return int(0)
            elif button_pos == 9:
                print self.driver.window_handles[-1]
                self.driver.switch_to.window(self.driver.window_handles[-1])
                elem = self.find_element_text('x', '//*[@id="collapse5"]/li[3]/a')
                time.sleep(10)
                self.deprint(u"测试应用：" + elem.replace(' ',''))
                if elem.replace(' ','') == '数据权限设置':
                    # flag = 1
                    self.close()
                    return int(1)
                else:
                    # flag = 0
                    self.close()
                    return int(0)
            elif button_pos == 10:
                print self.driver.window_handles[-1]
                self.driver.switch_to.window(self.driver.window_handles[-1])
                elem = self.find_element_text('x', '/html/body/div[2]/div[1]/ul/li[7]/h2/a')
                time.sleep(10)
                self.deprint(u"测试应用：" + elem.replace(' ',''))
                if elem.replace(' ','') == '签到应用下载':
                    # flag = 1
                    self.close()
                    return int(1)
                else:
                    # flag = 0
                    self.close()
                    return int(0)
            elif button_pos == 11:
                print self.driver.window_handles[-1]
                self.driver.switch_to.window(self.driver.window_handles[-1])
                elem = self.find_element_text('x', '/html/body/div[2]/div[1]/main/div[1]/div[1]/div[2]/button')
                time.sleep(10)
                self.deprint(u"测试应用：" + elem.replace(' ',''))
                if elem.replace(' ','') == '新建表单':
                    # flag = 1
                    self.close()
                    return int(1)
                else:
                    # flag = 0
                    self.close()
                    return int(0)
            elif button_pos == 12:
                print self.driver.window_handles[-1]
                self.driver.switch_to.window(self.driver.window_handles[-1])
                elem = self.find_element_text('x', '/html/body/div[1]/div[2]/main/div/div[1]/div/div[2]/div/div[2]/a/span')
                time.sleep(10)
                self.deprint(u"测试应用：" + elem.replace(' ',''))
                if elem.replace(' ','') == '新建问卷':
                    # flag = 1
                    self.close()
                    return int(1)
                else:
                    # flag = 0
                    self.close()
                    return int(0)
            elif button_pos == 13:
                print self.driver.window_handles[-1]
                self.driver.switch_to.window(self.driver.window_handles[-1])
                elem = self.find_element_text('x', '/html/body/div[2]/div[2]/div[2]/a')
                time.sleep(10)
                self.deprint(u"测试应用：" + elem.replace(' ',''))
                if elem.replace(' ','') == '新建抽奖':
                    # flag = 1
                    self.close()
                    return int(1)
                else:
                    # flag = 0
                    self.close()
                    return int(0)
            elif button_pos == 14:
                print self.driver.window_handles[-1]
                self.driver.switch_to.window(self.driver.window_handles[-1])
                elem = self.find_element_text('x', '/html/body/div[1]/div[2]/main/div/div[1]/div/div[2]/div/button/span')
                time.sleep(10)
                self.deprint(u"测试应用：" + elem.replace(' ',''))
                if elem.replace(' ','') == '新建投票':
                    # flag = 1
                    self.close()
                    return int(1)
                else:
                    # flag = 0
                    self.close()
                    return int(0)
            elif button_pos == 15:
                print self.driver.window_handles[-1]
                self.driver.switch_to.window(self.driver.window_handles[-1])
                elem = self.find_element_text('x', '/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/button')
                time.sleep(10)
                self.deprint(u"测试应用：" + elem.replace(' ',''))
                if elem.replace(' ','') == '新建论坛':
                    # flag = 1
                    self.close()
                    return int(1)
                else:
                    # flag = 0
                    self.close()
                    return int(0)
            elif button_pos == 16:
                print self.driver.window_handles[-1]
                self.driver.switch_to.window(self.driver.window_handles[-1])
                elem = self.find_element_text('x', '/html/body/section/div[1]/header/div/botton')
                time.sleep(10)
                self.deprint(u"测试应用：" + elem.replace(' ',''))
                if elem.replace(' ','') == '添加新产品线':
                    # flag = 1
                    self.close()
                    return int(1)
                else:
                    # flag = 0
                    self.close()
                    return int(0)
            elif button_pos == 17:
                print self.driver.window_handles[-1]
                self.driver.switch_to.window(self.driver.window_handles[-1])
                elem = self.find_element_text('x', '/html/body/div[2]/div[2]/div[2]/div[2]/div/button')
                time.sleep(10)
                self.deprint(u"测试应用：" + elem.replace(' ',''))
                if elem.replace(' ','') == '查看其他用户':
                    # flag = 1
                    self.close()
                    return int(1)
                else:
                    # flag = 0
                    self.close()
                    return int(0)
            elif button_pos == 18:
                print self.driver.window_handles[-1]
                self.driver.switch_to.window(self.driver.window_handles[-1])
                elem = self.find_element_text('x', '/html/body/div/div[1]/div[2]/div[4]/div[2]/div/button[1]')
                time.sleep(10)
                self.deprint(u"测试应用：" + elem.replace(' ',''))
                if elem.replace(' ','') == '上传文件':
                    # flag = 1
                    self.close()
                    return int(1)
                else:
                    # flag = 0
                    self.close()
                    return int(0)
            elif button_pos == 19:
                print self.driver.window_handles[-1]
                self.driver.switch_to.window(self.driver.window_handles[-1])
                elem = self.find_element_text('x', '/html/body/div[2]/div[2]/div[1]/a')
                time.sleep(10)
                self.deprint(u"测试应用：" + elem.replace(' ',''))
                if elem.replace(' ','') == '创建新供应商':
                    # flag = 1
                    self.close()
                    return int(1)
                else:
                    # flag = 0
                    self.close()
                    return int(0)
            elif button_pos == 20:
                print self.driver.window_handles[-1]
                self.driver.switch_to.window(self.driver.window_handles[-1])
                elem = self.find_element_text('x', '/html/body/div[1]/div[3]/div[1]/div[2]/div[1]/div[2]/button')
                time.sleep(10)
                self.deprint(u"测试应用：" + elem.replace(' ',''))
                if elem.replace(' ','') == '新建任务':
                    # flag = 1
                    self.close()
                    return int(1)
                else:
                    # flag = 0
                    self.close()
                    return int(0)
            elif button_pos == 21:
                print self.driver.window_handles[-1]
                self.driver.switch_to.window(self.driver.window_handles[-1])
                elem = self.find_element_text('x', '/html/body/div[1]/div[3]/div[1]/div[1]')
                time.sleep(10)
                self.deprint(u"测试应用：" + elem.replace(' ',''))
                if elem.replace(' ','') == '短信列表':
                    # flag = 1
                    self.close()
                    return int(1)
                else:
                    # flag = 0
                    self.close()
                    return int(0)
            elif button_pos == 22:
                print self.driver.window_handles[-1]
                self.driver.switch_to.window(self.driver.window_handles[-1])
                elem = self.find_element_text('x', '/html/body/div[1]/div[1]/div[2]/div[3]/div[2]/a')
                time.sleep(10)
                self.deprint(u"测试应用：" + elem.replace(' ',''))
                if elem.replace(' ','') == '新建栏目':
                    # flag = 1
                    self.close()
                    return int(1)
                else:
                    # flag = 0
                    self.close()
                    return int(0)
            elif button_pos == 23:
                print self.driver.window_handles[-1]
                self.driver.switch_to.window(self.driver.window_handles[-1])
                elem = self.find_element_text('x', '/html/body/div[2]/div[2]/div[1]/a')
                time.sleep(10)
                self.deprint(u"测试应用：" + elem.replace(' ',''))
                if elem.replace(' ','') == '创建新用户':
                    # flag = 1
                    self.close()
                    return int(1)
                else:
                    # flag = 0
                    self.close()
                    return int(0)
            elif button_pos == 24:
                print self.driver.window_handles[-1]
                self.driver.switch_to.window(self.driver.window_handles[-1])
                elem = self.find_element_text('x', '/html/body/div[2]/div[2]/div[2]/a')
                time.sleep(10)
                self.deprint(u"测试应用：" + elem.replace(' ',''))
                if elem.replace(' ','') == '新增全局角色':
                    # flag = 1
                    self.close()
                    return int(1)
                else:
                    # flag = 0
                    self.close()
                    return int(0)
            elif button_pos == 25:
                print self.driver.window_handles[-1]
                self.driver.switch_to.window(self.driver.window_handles[-1])
                elem = self.find_element_text('x', '/html/body/div[2]/div[2]/div[1]/h2')
                time.sleep(10)
                self.deprint(u"测试应用：" + elem.replace(' ', ''))
                if elem.replace(' ', '') == '模块管理':
                    # flag = 1
                    self.close()
                    return int(1)
                else:
                    # flag = 0
                    self.close()
                    return int(0)
            elif button_pos == 26:
                print self.driver.window_handles[-1]
                self.driver.switch_to.window(self.driver.window_handles[-1])
                elem = self.find_element_text('x', '//*[@id="g-right"]/div/div[1]/h2')
                time.sleep(10)
                self.deprint(u"测试应用：" + elem.replace(' ', ''))
                if elem.replace(' ', '') == '全局字典表管理':
                    # flag = 1
                    self.close()
                    return int(1)
                else:
                    # flag = 0
                    self.close()
                    return int(0)
        except NoSuchElementException:
            self.driver.switch_to.window(self.driver.window_handles[-1])
            self.close()
            return int(0)
        except NoSuchWindowException:
            self.driver.switch_to.window(self.driver.window_handles[-1])
            self.close()
            return int(0)


    #循环遍历每个应用
    def cyclic_test_app(self,num):
        actual_result = 2
        actual_dict = {}
        n = 1
        while n < num:
            #数据监测工具、智能分析、数据看板、客户管理、文件管理页面加载有问题，暂跳过，待研究原因
            if n == 6 or n == 7 or n == 8 :
                n = n + 1
                continue
            else :
                actual_result=self.click_menu_bt(n)
            time.sleep(3)
            # actual_result = self.click_menu_bt(n)
            #将进入应用界面的结果记录下来返回
            if actual_result == 0 or actual_result == 1:
                if n == 1:
                    actual_dict['wx'] = actual_result
                elif n == 2:
                    actual_dict['cj'] = actual_result
                elif n == 3:
                    actual_dict['DSPtf'] = actual_result
                elif n == 4:
                    actual_dict['SEMzs'] = actual_result
                elif n == 5:
                    actual_dict['tjzn'] = actual_result
                elif n == 6:
                    actual_dict['sjjcgj'] = actual_result
                elif n == 7:
                    actual_dict['znfx'] = actual_result
                elif n == 8:
                    actual_dict['sjkb'] = actual_result
                elif n == 9:
                    actual_dict['xsh'] = actual_result
                elif n == 10:
                    actual_dict['xxh'] = actual_result
                elif n == 11:
                    actual_dict['bdgl'] = actual_result
                elif n == 12:
                    actual_dict['wj'] = actual_result
                elif n == 13:
                    actual_dict['cj'] = actual_result
                elif n == 14:
                    actual_dict['tp'] = actual_result
                elif n == 15:
                    actual_dict['wtl'] = actual_result
                elif n == 16:
                    actual_dict['cpgl'] = actual_result
                elif n == 17:
                    actual_dict['khgl'] = actual_result
                elif n == 18:
                    actual_dict['wjgl'] = actual_result
                elif n == 19:
                    actual_dict['gysgl'] = actual_result
                elif n == 20:
                    actual_dict['yjgl'] = actual_result
                elif n == 21:
                    actual_dict['dxgl'] = actual_result
                elif n == 22:
                    actual_dict['wzgl'] = actual_result
                elif n == 23:
                    actual_dict['cygl'] = actual_result
                elif n == 24:
                    actual_dict['jsgl'] = actual_result
                elif n == 25:
                    actual_dict['mkgl'] = actual_result
                elif n == 26:
                    actual_dict['zdbgl'] = actual_result
                # continue
            n = n + 1

        return  actual_dict



if __name__ == '__main__':
    dr = brower()
    o = LoginPage(dr)
    o.login()
    o = ChoosePageTest(dr)
    time.sleep(3)
    # actual_dict=o.cyclic_test_app(26)
    o.click_menu_bt(25)
    # o.quit()