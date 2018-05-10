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

        #从嘉宾库添加嘉宾信息
        print self.deprint("从嘉宾库添加嘉宾信息")
        addfromguestsbtn = '/html/body/div[1]/div[2]/div[2]/div/div[3]/h2/div/a[1]'
        self.wait_is_visible('x',addfromguestsbtn)
        time.sleep(3)

        #从嘉宾库选择弹窗中，点选3个嘉宾后保存
        # self.wait_is_visible('x','//*[@id="guestDb"]/div/div/div[2]/ul/li[1]/label')
        # self.wait_is_visible('x','//*[@id="guestDb"]/div/div/div[2]/ul/li[2]/label')
        # self.wait_is_visible('x', '//*[@id="guestDb"]/div/div/div[2]/ul/li[3]/label')
        # self.wait_is_visible('x','//*[@id="guestDb"]/div/div/div[3]/a[1]')

        # 判断嘉宾是否大于3个，若大于，则直接点选3个嘉宾，若小于3个，则取消弹出的嘉宾选择窗口，再进行新增嘉宾的操作（正在修改为循环语句）

        # num = 0
        # i = 1
        # while guestnum < 3:
        #     print guestnum
        #     if num >= 3 :
        #         break
        #     else:
        if guestnum >= 3 :
            #大于3个，则直接点选3个嘉宾
            time.sleep(3)
            guestbtn1='//*[@id="guestDb"]/div/div/div[2]/ul/li[1]/div[2]/div[3]/ul/li[2]/span[2]'
            guestbtn2='//*[@id="guestDb"]/div/div/div[2]/ul/li[2]/div[2]/div[3]/ul/li[2]/span[2]'
            guestbtn3='//*[@id="guestDb"]/div/div/div[2]/ul/li[3]/div[2]/div[3]/ul/li[2]/span[2]'
            guestbtn4='//*[@id="guestDb"]/div/div/div[3]/a[1]'
            self.wait_is_visible('x',guestbtn1)
            self.wait_is_visible('x',guestbtn2)
            self.wait_is_visible('x',guestbtn3)
            self.wait_is_visible('x',guestbtn4)
            #break
        else:

            # 若小于3个嘉宾，则点击取消按钮后，新增嘉宾
            self.wait_is_visible('x','//*[@id="guestDb"]/div/div/div[3]/a[2]')
            # 点击新增嘉宾按钮
            self.wait_is_visible('x','/html/body/div[1]/div[2]/div[2]/div/div[3]/h2/div/a[2]')
            time.sleep(2)
            self.element_value_input('x','//*[@id="createGuest"]/div/div/div[2]/div/form/div[1]/div/input',u'校校')
            self.wait_is_visible('x','//*[@id="createGuest"]/div/div/div[3]/a[1]')
            #num = num + 1
            #guestnum = guestnum +1
#
if __name__ == '__main__':
    dr = brower()
    o = LoginPage(dr)
    o.login()
    o = ChoosePage(dr)
    time.sleep(3)
    o.click_menu_bt('8')
    o =  Webinar_IndexPage(dr)
    time.sleep(3)
    wbr = Webinar_Create(dr)
    wbr.create_meeting()
    gguestnum = Get_Guestnum(dr)
    guestnum = gguestnum.get_num()
    guest_add = Webcast_Setting(dr)
    guest_add.add_guest(guestnum)

