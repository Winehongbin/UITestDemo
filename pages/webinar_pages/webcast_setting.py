# -*- coding:utf-8 -*-
from pages.common_pages.driver import brower
from pages.common_pages.base import BasePage
from pages.common_pages.login_page import LoginPage
from pages.common_pages.choose_page import ChoosePage
from pages.webinar_pages.create_meeting import Webinar_Create
from pages.webinar_pages.index_page import Webinar_IndexPage
import time
from common.common_function.scrollbar import Scrollbar_Move

class Webcast_Setting(BasePage):

    # 进入基础设置页面
    def into_baseinfo(self):
        self.deprint('进入基础设置页面')
        time.sleep(2)
        self.wait_is_visible('x','//*[@id="collapse2"]/li[1]/a')
        time.sleep(3)

    # 设置会议标签，观看限制为审核后观看
    def edit_baseinfo(self):

        # 点击基本信息的编辑按钮
        self.wait_is_visible('x','/html/body/div[1]/div[2]/div[2]/div/div[2]/h2/a')
        #self.scrollbar('700')
        # # 设置会议为审核后观看
        # time.sleep(2)
        # self.wait_is_visible('x','/html/body/div[1]/div[2]/div[2]/div/div[2]/div/div[10]/div[1]/div[2]/label')
        # 添加会议标签
        self.scrollbar('bottom')
        time.sleep(5)
        self.wait_is_visible('x', '/html/body/div[1]/div[2]/div[2]/div/div[2]/div/div[20]/div[1]/div/div/div[2]')
        time.sleep(5)
        self.wait_is_visible('x','/html/body/div[1]/div[2]/div[2]/div/div[2]/div/div[20]/div[1]/div/div/div[3]/div[1]/span[3]')
        # 获取标签名称
        time.sleep(5)
        tagname = self.wait_is_visible('x','/html/body/div[1]/div[2]/div[2]/div/div[2]/div/div[20]/div[1]/div/div/div[1]/span')
        self.scrollbar('bottom')
        time.sleep(5)
        # 点击保存按钮
        self.wait_is_visible('x','/html/body/div[1]/div[2]/div[2]/div/div[2]/div/div[21]/button')
        time.sleep(3)
        self.scrollbar('top')
        # 获取选中以后标签的名称，并验证是否一致
        vtagname = self.wait_is_visible('x', '/html/body/div[1]/div[2]/div[2]/div/div[2]/div/div/div/div/span')
        if tagname == vtagname:
            self.deprint('标签添加成功')
        else:
            self.deprint('标签添加失败')

        # # 验证观看限制
        # vwatch = self.find_element_text('x', '/html/body/div[1]/div[2]/div[2]/div/div[2]/div/ul/li[7]/span[2]')
        # if vwatch == u"审核后观看":
        #     self.deprint("观看限制为审核后观看设置成功")
        # else:
        #     self.deprint("观看限制为审核后观看设置失败")

    def add_guest(self,guestnum):

        # 判断嘉宾是否小于3个，小于3个则进行新增嘉宾的操作
        if guestnum < 3:
            for i in range(1,4):
                addguestbtn = '/html/body/div[1]/div[2]/div[2]/div/div[3]/h2/div/a[2]'
                self.wait_is_visible('x',addguestbtn)
                time.sleep(2)
                # 填写嘉宾信息
                gname = u'校校'+ str(i)
                inputguestinfobtn='//*[@id="createGuest"]/div/div/div[2]/div/form/div[1]/div/input'
                self.element_value_input('x',inputguestinfobtn, gname)
                self.element_value_input('x', '//*[@id="createGuest"]/div/div/div[2]/div/form/div[3]/div/input',"sinobase")

                gmobile = '1990000112' + str(i)
                self.element_value_input('x','//*[@id="createGuest"]/div/div/div[2]/div/form/div[7]/div/input',gmobile)
                gemail = '123@qq.com' + str(i)
                self.element_value_input('x', '//*[@id="createGuest"]/div/div/div[2]/div/form/div[8]/div/input',gemail)
                # 点击保存按钮
                savebtn= '//*[@id="createGuest"]/div/div/div[3]/a[1]'
                self.wait_is_visible('x',savebtn)
                self.deprint('嘉宾新增成功')
                return u'嘉宾信息成功'
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
            self.deprint("从嘉宾库添加3个嘉宾信息成功")

    # 添加会议日程
    def add_agenda(self):

        # self.wait_is_visible('x', '/html/body/div[1]/div[2]/div[2]/div/div[4]/div')
        # self.scrollbarmovedown()
        # 将页面滚动条拖到底部
        # js = "var q=document.documentElement.scrollTop=100000"
        # self.driver.execute_script(js)
        self.scrollbar("100")
        self.wait_is_visible('x','/html/body/div[1]/div[2]/div[2]/div/div[4]/h2/div/a')
        self.element_value_input('x','//*[@id="myModa45"]/div/div/div[2]/div/form/div[1]/div/text-box/div/input',u'会议日程1')
        # 添加第一个嘉宾
        self.wait_is_visible('x','//*[@id="myModa45"]/div/div/div[2]/div/form/div[3]/div/a')
        self.wait_is_visible('x','//*[@id="myModa45"]/div/div/div[2]/div/form/div[3]/ng-bind-html/div[1]/div/button')
        self.wait_is_visible('x','//*[@id="myModa45"]/div/div/div[2]/div/form/div[3]/ng-bind-html/div[1]/div/ul/li[2]/a')
        # 添加第二个嘉宾
        self.wait_is_visible('x','//*[@id="myModa45"]/div/div/div[2]/div/form/div[3]/div/a/i')
        self.wait_is_visible('x','//*[@id="myModa45"]/div/div/div[2]/div/form/div[3]/ng-bind-html[2]/div[1]/div/button')
        self.wait_is_visible('x','//*[@id="myModa45"]/div/div/div[2]/div/form/div[3]/ng-bind-html[2]/div[1]/div/ul/li[2]/a')
        self.wait_is_visible('x','//*[@id="myModa45"]/div/div/div[2]/div/form/div[3]/ng-bind-html[2]/div[2]/div[1]/button')
        self.wait_is_visible('x','//*[@id="myModa45"]/div/div/div[2]/div/form/div[3]/ng-bind-html[2]/div[2]/div[1]/ul/li[2]/a')
        try:
            self.wait_is_visible('x', '//*[@id="myModa45"]/div/div/div[3]/a') # 点击确定
            self.deprint(u"添加会议日程成功")
            return u'添加会议日程成功'
        except:
            self.deprint(u"添加会议日程失败")
            return u'添加会议日程失败'


if __name__ == '__main__':
    dr = brower()
    o = LoginPage(dr)
    o.login()
    o = ChoosePage(dr)
    time.sleep(3)
    o.click_menu_bt('8')
    time.sleep(2)
    # gguestnum = Get_Guestnum(dr)
    # guestnum = int(gguestnum.get_num())
    o =  Webinar_IndexPage(dr)
    # o.index_webinar()
    o.webinar_list()
    time.sleep(3)
    o.choose_meeting()
    # wbr = Webinar_Create(dr)
    # wbr.create_meeting()
    wbr_seting = Webcast_Setting(dr)
    wbr_seting.into_baseinfo()
    wbr_seting.edit_baseinfo()

    # wbr_seting.add_guest(3)
    # time.sleep(3)
    # wbr_seting.add_agenda()
    # o.scrollbar("top")

    # scollbarmove = Scrollbar_Move(dr)
    # scollbarmove.scrollbarmovedown()
    # time.sleep(1)
#    # time.sleep(2)
    # scollbarmove.scrollbarmoveup()
    # time.sleep(2)
    # o.quit()

