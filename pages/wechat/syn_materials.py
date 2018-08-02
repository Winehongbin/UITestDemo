# -*- coding: utf-8 -*-
'''
Created on 2018-07-09
@author: 常丽楠
'''


from pages.common_pages.base import BasePage
from pages.common_pages.login_page import LoginPage
import time
from pages.common_pages.choose_page import ChoosePage
from pages.common_pages.driver import brower

class Syn_materials(BasePage):
    #同步微信素材
        def syn_materials(self):
            try:
                self.deprint("开始执行同步微信素材用例")
                self.wait_is_visible('x', '//*[@id="ul-nav-2"]/li[1]/a')  # 点击素材管理菜单
                time.sleep(3)
                self.scrollbar("bottom")
                self.wait_is_visible('x', '// *[ @ id = "spansyncfuns"]')  # 点击同步微信素材
                time.sleep(20)
                tips = self.find_element_text('x', '//*[@id="spansyncfuns"]')
                if '本次共同步素材数据' in tips:
                    self.deprint("同步微信素材用例执行完成")
                    return u'同步素材数据成功'
            except:
                self.deprint("用例执行失败，重试一次")
                self.deprint("开始执行同步微信素材用例")
                self.wait_is_visible('x', '//*[@id="ul-nav-2"]/li[1]/a')  # 点击素材管理菜单
                time.sleep(3)
                self.scrollbar("bottom")
                self.wait_is_visible('x', '// *[ @ id = "spansyncfuns"]')  # 点击同步微信素材
                time.sleep(20)
                tips = self.find_element_text('x', '//*[@id="spansyncfuns"]')
                if '本次共同步素材数据' in tips:
                    self.deprint("同步微信素材用例执行完成")
                    return u'同步微信素材成功'
                else:
                    self.deprint("同步微信素材失败")

if __name__ == '__main__':
    driver = brower()
    login = LoginPage(driver)
    login.login()
    chooseP = ChoosePage(driver)
    chooseP.click_menu_bt("1")
    syn = Syn_materials(driver)
    result = syn.syn_materials()