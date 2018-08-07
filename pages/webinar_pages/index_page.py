# -*- coding: utf-8 -*-
from pages.common_pages.base import BasePage
from pages.common_pages.login_page import LoginPage
import time
from pages.common_pages.choose_page import ChoosePage
from pages.common_pages.driver import brower
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
class Webinar_IndexPage(BasePage):

    # 打开线上会的首页
    def index_webinar(self):
        self.deprint("进入线上会首页")
        # self.wait_is_visible('x','/html/body/div[1]/div[1]/ul/li[1]/h2/a')
        element = WebDriverWait(self.driver,10,0.5).until(EC.presence_of_all_elements_located((By.XPATH,'/html/body/div[1]/div[1]/ul/li[1]/h2/a')))
        # print element
        if element == 1 :
            self.wait_is_visible('x','/html/body/div[1]/div[1]/ul/li[1]/h2/a')
        else:
            time.sleep(3)
            self.wait_is_visible('x', '/html/body/div[1]/div[1]/ul/li[1]/h2/a')

    # 进入直播会议列表页面
    def webinar_list(self):
        self.deprint("进入直播会议列表页面")
        time.sleep(2)
        # 点击直播菜单
        self.wait_is_visible('x','//*[@id="collapse2"]/li[1]/a')

    # 点击直播列表页面的创建会议按钮
    def list_create(self):
        self.deprint("点击直播列表创建会议按钮")
        self.wait_is_visible('x','/html/body/div[1]/div[2]/div/div[2]/button')
        time.sleep(5)
    def publiccomment(self):
        # 线上会会中发表评论
        time.sleep(5)
        self.driver.implicitly_wait(30)
        # 在发表评论输入框中输入aaaa
        self.find_element_input('x','//*[@id="askContentInput"]','aaaa')
        # 点击发送按钮
        self.wait_is_visible('x','//*[@id="sendQuestion"]')

    # 点击首页的创建会议按钮
    def index_create(self):
        self.deprint("点击首页创建会议按钮")
        self.wait_is_visible('x', '/html/body/div[1]/div[2]/div/button')
        time.sleep(3)
    def Is_AllInfo(self):
        # 此方法用于判断线上会会中报名时，报名人员信息是否完整
        # 判断姓名是否完整
        time.sleep(3)
        name=self.find_element_AttributeText('x','//*[@id="body-box"]/div[1]/div/div[2]/div[1]/div[1]/div/input','value')
        print "name:",name
        if name=="":
            self.find_element_input('x','//*[@id="body-box"]/div[1]/div/div[2]/div[1]/div[1]/div/input','yaya')
        # 判断手机是否完整
        phone = self.find_element_AttributeText('x', '//*[@id="body-box"]/div[1]/div/div[2]/div[1]/div[2]/div/input',
                                                   'value')
        if phone == "":
            self.find_element_input('x', '//*[@id="body-box"]/div[1]/div/div[2]/div[1]/div[2]/div/input', '15960167982')
        email=  self.find_element_AttributeText('x', '//*[@id="body-box"]/div[1]/div/div[2]/div[1]/div[3]/div/input',
                                                   'value')
        if email == "":
            self.find_element_input('x', '//*[@id="body-box"]/div[1]/div/div[2]/div[1]/div[3]/div/input', '111111@qq.com')
        idcard = self.find_element_AttributeText('x', '//*[@id="body-box"]/div[1]/div/div[2]/div[1]/div[4]/div/input',
                                                'value')
        if idcard == "":
            self.find_element_input('x', '//*[@id="body-box"]/div[1]/div/div[2]/div[1]/div[4]/div/input',
                                    '123456789012345678')
        username = self.find_element_AttributeText('x', '//*[@id="body-box"]/div[1]/div/div[2]/div[1]/div[5]/div/input',
                                                 'value')
        if username == "":
            self.find_element_input('x', '//*[@id="body-box"]/div[1]/div/div[2]/div[1]/div[5]/div/input',
                                    'yaya')
    def Get_EnterMeeting(self,current_handle):
        # 获取参会人员入会信息
        all_handles=self.driver.window_handles
        for i in all_handles:
            if i ==current_handle:
                self.driver.switch_to.window(i)
                self.driver.refresh()
                # 点击详细数据按钮
                self.scrollbar("bottom")
                # 点击详细数据按钮
                self.wait_is_visible('x','//*[@id="collapse4"]/li[2]/a')
                # 点击文件下载按钮
                self.wait_is_visible('x', '/html/body/div[1]/div[2]/div[2]/div/ul/li[4]/a')
                try:
                    count=self.find_element_text('x','/html/body/div[1]/div[2]/div[2]/div/div[3]/ul/li/div[3]/h2[1]')
                    if count!=0:
                        # 点击报名参会人员按钮
                        self.wait_is_visible('x','/html/body/div[1]/div[2]/div[2]/div/ul/li[1]/a')
                        time.sleep(3)

                        text=self.find_element_text('x','/html/body/div[1]/div[2]/div[2]/div/div[3]/table/tbody/tr[1]/td[14]/span')
                        if text=="是":
                            return "success"
                        else:
                            return "fail"
                except:
                    return "fail"

    def Is_TrueQuark(self,meeting_handle):
        # 验证是否中奖
        all_handle=self.driver.window_handles
        for i in all_handle:
            if i==meeting_handle:
                self.driver.switch_to.window(i)
                # 获取中奖名单文本，应获取:恭喜您，中奖了！
                self.find_element_text('x','//*[@id="mCSB_1_container"]/div[6]/div[2]/div[1]')

    def Is_Quark(self):
        # 验证抽奖
        # 点击全部添加按钮
        self.wait_is_visible('x','//*[@id="nonitembased"]/div[1]/div[1]/p[2]/button')
        # 点击开始抽奖按钮
        self.wait_is_visible('x','//*[@id="nonitembased"]/div[1]/div[3]/button')
        # 等待3秒后点击结束抽奖
        time.sleep(3)
        # 点击结束抽奖按钮
        self.wait_is_visible('x','//*[@id="nonitembased"]/div[1]/div[3]/button')

    def Click_FileDown(self):
        # 开始点击文件下载按钮
        self.wait_is_visible('x','/html/body/div[2]/div[2]/div[2]/div[5]/div/div[3]/a/img')
        # 点击文件的下载按钮
        self.wait_is_visible('x','//*[@id="mCSB_1_container"]/div[8]/ul/li/a[2]')
        time.sleep(3)

    def Click_QuestButton(self):
        current_handle=self.driver.current_window_handle
        # 开始点击问卷的按钮
        self.wait_is_visible('x','/html/body/div[2]/div[2]/div[2]/div[5]/div/div[1]/a/img')
        # 切换到新开的窗口中
        self.driver.switch_to.window(self.driver.window_handles[-1])
        time.sleep(1)
        # 点击提交按钮
        self.wait_is_visible('x','//*[@id="questionContainer"]/div[2]/input')
        self.driver.close()
        self.driver.refresh()
        return current_handle
    def Click_VoteCommitBut(self):
        # 点击投票的提交按钮
        self.wait_is_visible('x','//*[@id="body-box"]/div[1]/div/div[2]/div[1]/div[1]/div/input')
        # 点击右上角的关闭按钮
        self.wait_is_visible('x','//*[@id="dialog_vote2242"]/div/a')
    def login_newcustom(self):
        # 新用户的登陆报名按钮
        time.sleep(5)
        self.driver.implicitly_wait(30)
        # 执行登陆报名按钮
        self.wait_is_visible('x', '/html/body/div[3]/div/div[3]')
        time.sleep(10)
        self.driver.implicitly_wait(30)
        # 点击注册按钮
        self.wait_is_visible('x','//*[@id="con_one_1"]/div[7]/div/div[2]/a')
        self.find_element_input('x','//*[@id="body-box"]/div[1]/div/div[2]/div[1]/div[1]/div/input','yaya')
        self.randome_phone()
        self.random_email()
        self.random_idcard()
        self.random_username()
        # 执行注册按钮
        self.wait_is_visible('x', '/html/body/div[3]/div[2]/form/div[3]/div[1]/input')
    def random_username(self):
        # 开始随机生成用户名
        text_username='u'+str(self.randomidcard())
        # 在用户名输入框中输入随机生成的用户名
        self.find_element_input('x','//*[@id="body-box"]/div[1]/div/div[2]/div[1]/div[5]/div/input',text_username)

    def random_idcard(self):
        # 开始随机生成身份证
        ranidcard=self.randomidcard()
        text_idcard=random.randint(00000,99999)+ranidcard
        # 在身份证输入框中输入随机生成的身份证
        self.find_element_input('x','//*[@id="body-box"]/div[1]/div/div[2]/div[1]/div[4]/div/input',text_idcard)

    def randomidcard(self):
        # 返回生成13位的数值
        t=time.time()
        return int(round(t*1000))
    def random_email(self):
        # 输入随机邮箱值
        randomemail=self.randomemail()
        self.find_element_input('x','//*[@id="body-box"]/div[1]/div/div[2]/div[1]/div[3]/div/input',randomemail)

    def randome_phone(self):
        # 生成随机手机号码函数
        list=['131','130','132','155','156','135','136','137','138','139','150','151','152','158','159','182','183','184','157','187','188','147','178','185','186','145','176','185','133','153','180','181','189','177']
        while(True):
            # 输入随机的手机号
            phone=self.randomphone()
            for i in list:
                ranphone=i+phone
                # 输入随机的手机号码
                self.find_element_input('x','/html/body/div[3]/div[2]/form/div[1]/div[1]/input',ranphone)
                # 输入注册的密码
                self.find_element_input('x', '/html/body/div[3]/div[2]/form/div[1]/div[1]/input[1]', '123123')
                try:
                    text=self.find_element_text('x','/html/body/div[3]/div[2]/form/div[1]/div[2]/p')
                    if text=="您输入的手机已注册，请登陆":
                    # 说明手机此时已不能报名
                        continue
                    else:
                        break
                except:
                    break


    def randomphone(self):
        # 获取随机的手机后8位
        text=random.randint(0,99999999)
        return text
    def randomemail(self):
        return int(time.time())
    def login_meeting(self):
        # 老用户的登陆报名按钮
        time.sleep(5)
        self.driver.implicitly_wait(30)
        # 执行登陆报名按钮
        self.wait_is_visible('x','/html/body/div[3]/div/div[3]')
        time.sleep(10)
        self.driver.implicitly_wait(30)
        # 输入手机号和密码
        self.find_element_input('x','//*[@id="con_one_1"]/div[1]/input','15960167982')
        self.find_element_input('x','//*[@id="con_one_1"]/div[3]/input','123123')
        # 点击登陆按钮
        self.wait_is_visible('x','//*[@id="con_one_1"]/input')
        time.sleep(5)
        self.driver.implicitly_wait(30)
        self.Is_AllInfo()
        # 进入到报名页面
        self.scrollbar("bottom")
        self.wait_is_visible('x','//*[@id="body-box"]/div[1]/div/div[2]/div[2]/input')
        time.sleep(5)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.driver.implicitly_wait(30)
        current_handle=self.driver.current_window_handle
        return current_handle
    def return_offmeeting(self,current_handle,content):
        # 回到线上会会场页面，继续发言
        all_handles=self.driver.window_handles
        for i in all_handles:
            if i==current_handle:
                self.driver.switch_to.window(i)
                self.driver.refresh()
                # 输入test值
                self.find_element_input('x','//*[@id="askContentInput"]',content)
                # 点击发送按钮
                self.wait_is_visible('x','//*[@id="sendQuestion"]')
    def Click_JYButton(self):
        time.sleep(1)
        # 点击禁言按钮
        self.wait_is_visible('x','//*[@id="qaList"]/div[2]/div/div[2]/ul/div/li[1]/section/div[2]/div[3]/a[4]')
        # 选择禁言10分钟
        self.wait_is_visible('x','//*[@id="qaList"]/div[2]/div/div[2]/ul/div/li[1]/div/p[2]')
        current_handle=self.driver.current_window_handle
        return current_handle
    def Click_JJButton(self):
        # 点击解禁按钮
        time.sleep(1)
        # 点击禁言按钮
        self.wait_is_visible('x', '//*[@id="qaList"]/div[2]/div/div[2]/ul/div/li[1]/section/div[2]/div[3]/a[4]')
        # 选择解禁
        self.wait_is_visible('x', '//*[@id="qaList"]/div[2]/div/div[2]/ul/div/li[1]/div/p[1]')
        pass
    def Click_hdButton(self):
        # 点击互动问答按钮
        time.sleep(3)
        self.driver.implicitly_wait(30)
        # 点击互动问答按钮
        self.wait_is_visible('x','//*[@id="accordion"]/div/ul/li[7]/a')

    def enter_meeting_hd(self):
        # 进入线上会会中互动
        time.sleep(5)
        self.driver.implicitly_wait(30)
        # 点击进入会中互动按钮
        self.wait_is_visible('x','/html/body/div[1]/div[1]/div[1]/div[2]/div[1]/a[4]')
        self.driver.switch_to.window(self.driver.window_handles[-1])
    def XHBL_content(self,flag):
        time.sleep(5)
        self.driver.implicitly_wait(30)
        # 循环遍历发言内容
        Ediv=self.driver.find_element_by_xpath('//*[@id="qaList"]/div[2]/div/div[2]/ul/div')
        Elis = Ediv.find_elements_by_tag_name('li')
        if flag=="1":
            for i in Elis:
                if "test" in i.text:
                    return "fail"
            return "success"
        elif flag=="2":
            for i in Elis:
                if "hello" in i.text:
                    return "success"
            return "fail"
    def switch_window(self,current_handle):
        # 切换到会议详情页面并刷新
        self.driver.implicitly_wait(30)
        time.sleep(5)
        # 切换到会议详情页面并刷新
        all_handles=self.driver.window_handles
        for i in all_handles:
            if i ==current_handle:
                self.driver.switch_to.window(i)
                self.driver.refresh()
    def detail_data(self):
        time.sleep(5)
        self.driver.implicitly_wait(30)
        # 点击详细数据按钮
        self.wait_is_visible('x','//*[@id="collapse4"]/li[2]/a')
        time.sleep(3)
        # 点击操作按钮
        self.wait_is_visible('x','/html/body/div[1]/div[2]/div[2]/div/div[3]/table/tbody/tr/td[15]/a')
        time.sleep(5)
        # 滚动条拖到最下面
        self.scrollbar("bottom")
        # 获取观看设备是否为pc
        time.sleep(4)
        text=self.find_element_text('x','/html/body/div[1]/div[2]/div[2]/div/div[2]/div/div[3]/div[2]/div[1]/table/tbody/tr[1]/td[7]')
        return text
    # 选择直播会议
    def choose_meeting(self):
        self.deprint('选择一场直播中的会议')
        time.sleep(3)
        for i in range(1,5):
            status1 = self.find_element_text('x','/html/body/div[1]/div[2]/div/section/ul/li['+str(i)+']/div/div[2]/p[1]/span[2]')
            self.deprint(status1)
            if status1 == u'直播中' :
                wtitle = self.find_element_text('x', '/html/body/div[1]/div[2]/div/section/ul/li[' + str(i) + ']/div/div[2]/p[1]/span[1]')
                self.wait_is_visible('x','/html/body/div[1]/div[2]/div/section/ul/li['+str(i)+']/div/a')
                self.deprint('进入直播中的会议的详情页面')
                break
            else:
                continue
        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.driver.implicitly_wait(10)
        return wtitle

if __name__ == '__main__':
    dr = brower()
    o = LoginPage(dr)
    o.login()
    o = ChoosePage(dr)
    time.sleep(3)
    o.click_menu_bt('8')
    o =  Webinar_IndexPage(dr)
    time.sleep(3)
    o.webinar_list()
    o.choose_meeting()
    o.quit()




