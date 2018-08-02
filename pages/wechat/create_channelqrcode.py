# -*- coding: utf-8 -*-
'''
Created on 2018-07-26
@author: 常丽楠
'''


from pages.common_pages.base import BasePage
from pages.common_pages.login_page import LoginPage
import time
from pages.common_pages.choose_page import ChoosePage
from pages.common_pages.driver import brower
from pages.wechat.create_material import Creat_media

codename = u'自动化新增二维码' + time.strftime("%H:%M:%S")

class Create_channelqrcode(BasePage):
    #新增渠道二维码
        def create_channel(self):
                self.find_element_click('x', '//*[@id="ul-nav-2"]/li[7]/a')  # 点击渠道二维码菜单
                time.sleep(3)
                self.find_element_click('x', '//*[@id="g-right"]/section/div/div/div/div[3]/a[1]')  # 点击新增渠道二维码按钮
                self.deprint("点击新增渠道二维码按钮")
                time.sleep(3)
                self.find_element_input('x', '//*[@id="g-right"]/section/div/div/div/div/div[1]/text-box-for-length/div/input', codename)  #输入渠道二维码名称
                self.find_element_click('x', '// *[ @ id = "g-right"] / section / div / div / div / div / div[4] / div[2] / div / div[2] / div / div / div / div[1] / a / span')  #点击从素材库选择按钮
                time.sleep(3)
                self.find_element_click('x','//*[@id="scroll"]/div[1]/ul/li[1]/div[1]/div[1]/div[4]') #选择第一个素材
                self.find_element_click('x','// *[ @ id = "chooseMaterialWindow"] / div / form / footer / button[1]')  #点击保存按钮
                time.sleep(3)
                self.scrollbar("bottom")
                self.find_element_click('x','// *[ @ id = "g-right"] / section / div / div / div / div / div[10] / div')  #保存渠道二维码信息
                time.sleep(3)


        def create_channelqrcode(self,driver):
            try:
                self.deprint("开始执行新增渠道二维码用例")
                Create_channelqrcode.create_channel(self)
                firstcode = self.find_element_text('x', '//*[@id="g-right"]/section/div/div/section/table/tbody/tr[1]/td[2]/dl/dt')
                if codename == firstcode:
                    self.deprint("新增渠道二维码用例执行完成")
                    time.sleep(2)
                    self.find_element_click('x','// *[ @ id = "g-right"] / section / div / div / section / table / tbody / tr[1] / td[9] / a[3]')  #删除刚新建的渠道二维码
                    time.sleep(2)
                    self.find_element_click('x', '// *[ @ id = "dialogBox"] / div / div / div[3] / button[1]')  #删除确认对话框点击确定
                    time.sleep(2)
                    Creat_media(driver).delete_media()
                    return u'新增渠道二维码成功'
            except:
                self.deprint("用例执行失败，重试一次")
                self.deprint("开始执行新增渠道二维码用例")
                Create_channelqrcode.create_channel(self)
                firstcode = self.find_element_text('x', '//*[@id="g-right"]/section/div/div/section/table/tbody/tr[1]/td[2]/dl/dt')
                if codename == firstcode:
                    self.deprint("新增渠道二维码用例执行完成")
                    time.sleep(2)
                    self.find_element_click('x',
                                            '// *[ @ id = "g-right"] / section / div / div / section / table / tbody / tr[1] / td[9] / a[3]')  # 删除刚新建的渠道二维码
                    time.sleep(2)
                    self.find_element_click('x',
                                            '// *[ @ id = "dialogBox"] / div / div / div[3] / button[1]')  # 删除确认对话框点击确定
                    time.sleep(2)
                    Creat_media(driver).delete_media()
                    return u'新增渠道二维码成功'
                else:
                    self.deprint("新增渠道二维码失败")



if __name__ == '__main__':
    driver = brower()
    login = LoginPage(driver)
    login.login()
    chooseP = ChoosePage(driver)
    chooseP.click_menu_bt("1")
    channelqrcode = Create_channelqrcode(driver)
    result = channelqrcode.create_channelqrcode()