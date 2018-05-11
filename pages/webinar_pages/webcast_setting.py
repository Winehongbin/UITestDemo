# -*- coding:utf-8 -*-
from pages.common_pages.driver import brower
from pages.common_pages.base import BasePage
from pages.common_pages.login_page import LoginPage
from pages.common_pages.choose_page import ChoosePage
from pages.webinar_pages.create_meeting import Webinar_Create
from pages.webinar_pages.index_page import Webinar_IndexPage
from pages.webinar_pages.guest_manager import Get_Guestnum
import time

class Webcast_Setting(BasePage):


    def add_guest(self,guestnum):

        # 判断嘉宾是否小于3个，小于3个则进行新增嘉宾的操作
        if guestnum < 3:
            for i in range(1,4):
                addguestbtn = '/html/body/div[1]/div[2]/div[2]/div/div[3]/h2/div/a[2]'
                self.wait_is_visible('x',addguestbtn)
                time.sleep(2)
                gname = u'校校'+ str(i)
                inputguestinfobtn='//*[@id="createGuest"]/div/div/div[2]/div/form/div[1]/div/input'
                self.element_value_input('x',inputguestinfobtn, gname)
                savebtn= '//*[@id="createGuest"]/div/div/div[3]/a[1]'
                self.wait_is_visible('x',savebtn)
                print self.deprint('嘉宾新增成功')
                time.sleep(3)
        else:

            # 从嘉宾库添加3个嘉宾信息
            addfromguestsBtn = '/html/body/div[1]/div[2]/div[2]/div/div[3]/h2/div/a[1]'
            self.wait_is_visible('x', addfromguestsBtn)
            time.sleep(3)
            guestbtn1 = '//*[@id="guestDb"]/div/div/div[2]/ul/li[1]/div[2]/div[3]/ul/li[2]/span[2]'
            guestbtn2 = '//*[@id="guestDb"]/div/div/div[2]/ul/li[2]/div[2]/div[3]/ul/li[2]/span[2]'
            guestbtn3 = '//*[@id="guestDb"]/div/div/div[2]/ul/li[3]/div[2]/div[3]/ul/li[2]/span[2]'
            guestbtn4 = '//*[@id="guestDb"]/div/div/div[3]/a[1]'
            self.wait_is_visible('x', guestbtn1)
            self.wait_is_visible('x', guestbtn2)
            self.wait_is_visible('x', guestbtn3)
            self.wait_is_visible('x', guestbtn4)
            time.sleep(2)
            print self.deprint("从嘉宾库添加3个嘉宾信息成功")
#
if __name__ == '__main__':
    dr = brower()
    o = LoginPage(dr)
    o.login()
    o = ChoosePage(dr)
    time.sleep(3)
    o.click_menu_bt('8')
    gguestnum = Get_Guestnum(dr)
    guestnum = int(gguestnum.get_num())
    time.sleep(3)
    o =  Webinar_IndexPage(dr)
    o.index_webinar()
    time.sleep(3)
    wbr = Webinar_Create(dr)
    wbr.create_meeting()
    guest_add = Webcast_Setting(dr)
    guest_add.add_guest(guestnum)

