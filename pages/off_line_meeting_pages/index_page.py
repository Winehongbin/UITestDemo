# -*- coding: utf-8 -*-
from pages.common_pages.base import BasePage
from pages.common_pages.login_page import LoginPage
import time
from pages.common_pages.choose_page import ChoosePage
from pages.common_pages.driver import brower
from datetime import datetime
# from pages.questionnaire_page.new_questionnaire_page import NewQuestionnairePage
class IndexPage(BasePage):


    # 点击创建会议
    def click_createunderline(self):
        self.wait_is_visible('css','body > div.g-container.ng-scope > div.g-left.s-left > ul > li.ng-scope.has-page.active > h2 > a')
        self.deprint("点击创建会议")
        self.driver.switch_to.window(self.driver.window_handles[-1])   # 获取下一个窗口句柄，跳转
        self.wait_is_visible('css','#g-right > div > div.clearfix.ng-scope > div.contact-stats-box.w715 > div.event-stats-l > div > button') #点击创建会议
        self.driver.implicitly_wait(30)
        self.deprint("点击创建会议完成")

    #点击会议列表菜单
    def click_linelist(self,list_pos):
        self.deprint("点击会议列表")
        self.driver.implicitly_wait(10)
        css_path = "/html/body/div[2]/div[1]/ul/li[" + str(list_pos) + "]/h2/a"   #点击会议列表
        self.wait_is_visible('x', css_path)
        self.driver.refresh()
        self.deprint("点击第一场会议")
        self.driver.implicitly_wait(30)
        self.wait_is_visible('x','//*[@id="g-right"]/div/div[3]/table/tbody/tr[1]/td[2]/a')  #点击第一场会议
        self.driver.implicitly_wait(30)
    #     点击线下会会议列表按钮
    # def click_offlinelist(self):
    #     self.wait_is_visible('x','/html/body/div[2]/div[1]/ul/li[2]/h2/a')
    #     点击会议列表中的创建新的会议按钮
    # def click_newofline(self):
    #     self.wait_is_visible('x','//*[@id="g-right"]/div/div[1]/div/botton')
    # 时间戳函数
    def time_romfun(self):
        nowtime = datetime.now().strftime('%Y%m%d%H%M%S')
        return nowtime
    # 开始创建新的会议
    # def create_newoffline(self):
    #     # 输入具体的会议名称
    #     self.element_value_input('x','//*[@id="seminarName"]','自动化会议'+self.time_romfun())
    #     # 注册表单选择启用，二级下拉框选择新建注册表单(9)并点击
    #     self.wait_is_visible('x','//*[@id="createSeminarScroller"]/form/div[8]/div[1]/div/button')
    #     # 选择启动选项并点击
    #     self.wait_is_visible('x','//*[@id="createSeminarScroller"]/form/div[8]/div[1]/div/ul/li[1]/a')
    #     # 二级菜单点击
    #     self.wait_is_visible('x','//*[@id="createSeminarScroller"]/form/div[8]/div[2]/div/button')
    #     # 选择新建注册表单(9)
    #     self.wait_is_visible('x','//*[@id="createSeminarScroller"]/form/div[8]/div[2]/div/ul/li[2]/a')
    #     # 微信公众号选择自有微信号
    #     self.wait_is_visible('x','//*[@id="createSeminarScroller"]/form/div[9]/div[1]/div/button')
    #     # 选择自有公众号
    #     self.wait_is_visible('x','//*[@id="createSeminarScroller"]/form/div[9]/div[1]/div/ul/li[3]/a')
    #     # 微信公众号点击并选择自动化测试号
    #     self.wait_is_visible('x','//*[@id="createSeminarScroller"]/form/div[9]/div[2]/div/button')
    #     self.wait_is_visible('x','//*[@id="createSeminarScroller"]/form/div[9]/div[2]/div/ul/li[2]/a')
    #     # 点击创建按钮
    #     self.wait_is_visible('x','//*[@id="createSeminar"]/div/div/div[3]/button')
        # 点击编辑按钮并设置标签
    # def click_editbutton(self):
    #     # 获取当前的handles
    #     current_handle=self.driver.current_window_handle
    #     # 点击编辑按钮
    #     self.wait_is_visible('x','//*[@id="g-right"]/div/div[1]/div[1]/div/a')
    #     # 滚动条拖到最下面，找到标签并点击
    #     self.scrollbar("bottom")
    #     # 点击标签输入框
    #     self.wait_is_visible('x','//*[@id="g-right"]/div/div[2]/div/div/div/div[12]/div/div/div/div/div[2]')
    #     # 选择1标签
    #     self.wait_is_visible('x','//*[@id="g-right"]/div/div[2]/div/div/div/div[12]/div/div/div/div/div[3]/div[1]/span[1]')
    #     # 点击保存按钮
    #     self.wait_is_visible('x','//*[@id="g-right"]/div/input')
    #     return current_handle
    # 点击报名表单按钮
    # def click_BMBD(self):
    #     # 点击报名表单按钮
    #     self.wait_is_visible('x','/html/body/div[2]/div[2]/ul[2]/li[3]/a/strong')
    #     # 点击开始报名按钮
    #     self.wait_is_visible('x','//*[@id="g-right"]/div/div[1]/div[2]/table/tbody/tr/td[9]/a[4]')
    #     点击pc按钮并登陆报名
    # def click_PCAndBM(self):
    #     # 获取当前打开的窗口信息
    #     current_handle=self.driver.window_handles
    #     # 点击pc按钮，此时新开了页面
    #     self.wait_is_visible('x','/html/body/div[2]/div[1]/div[2]/div[1]/p/a[1]')
    #     all_handles=self.driver.window_handles
    #     for i in all_handles:
    #         if i not in current_handle:
    #             # 切换到新开窗口
    #             self.driver.switch_to.window(i)
    #             # 点击我要报名
    #             self.wait_is_visible('x','/html/body/div[3]/div/div/a')
    #             # 输入手机号码
    #             self.element_value_input('x','//*[@id="con_one_1"]/div[1]/input','15960167982')
    #             # 输入密码
    #             self.element_value_input('x','//*[@id="con_one_1"]/div[3]/input','123123')
    #             # 点击登陆按钮
    #             self.wait_is_visible('x','//*[@id="con_one_1"]/input')
    #             # 点击我要报名按钮
    #             self.wait_is_visible('x','/html/body/div[3]/div/div/a')
    #             # 填写姓名
    #             self.element_value_input('x','//*[@id="body-box"]/form/div[1]/input','yaya')
    #             # 填写邮箱
    #             self.element_value_input('x','//*[@id="body-box"]/form/div[3]/input','111111@qq.com')
    #             # 填写身份证
    #             self.element_value_input('x','//*[@id="body-box"]/form/div[4]/input','111111111111111111')
    #             # 填写用户名
    #             self.element_value_input('x','//*[@id="body-box"]/form/div[5]/input','auto')
    #             self.scrollbar("bottom")
    #             # 点击提交按钮
    #             self.wait_is_visible('x','//*[@id="body-box"]/form/input')
    #             切换handle
    # def switch_handle(self,current_handle,SYHandle):
    #     text2=""
    #     Model_handle=""
    #     all_handles = self.driver.window_handles
    #     for i in all_handles:
    #         if i == current_handle:
    #             self.driver.switch_to.window(i)
    #             Model_handle=self.driver.current_window_handle
    #             # 点击参会人员按钮
    #             self.wait_is_visible('x','/html/body/div[2]/div[2]/ul[1]/li[2]/a')
    #             try:
    #                 # 判断报名人员是否为刚刚报名人员
    #                 text=self.find_element_text('x','//*[@id="g-right"]/div/div[5]/table/tbody/tr/td[3]/div/a')
    #                 if text=="yaya":
    #                     self.deprint("说明报名成功")
    #                     # 此时点击用户名称，进入查看报名人员详情互动记录显示进入专题站、登录、浏览表单、提交表单、报名互动信息
    #                     text=self.Click_Enteroffline('//*[@id="g-right"]/div/div[5]/table/tbody/tr/td[3]/div/a','//*[@id="g-right"]/div/div[4]/div[2]/div/table/tfoot/tr/th/div/div[1]/div/button','//*[@id="g-right"]/div/div[4]/div[2]/div/table/tfoot/tr/th/div/div[1]/div/ul/li[2]/a','//*[@id="g-right"]/div/div[4]/div[2]/div/table/tbody',"1")
    #                     if text=="成功":
    #                         text2 = "成功"
    #                     else:
    #                         text2="失败"
    #                 else:
    #                     text2="失败"
    #             except:
    #                 text2="失败"
    #             finally:
    #                 return text2,Model_handle
    # def Model_Detail(self,SYHandle):
    #     text1=""
    #     all_handles1 = self.driver.window_handles
    #     for i in all_handles1:
    #         if i == SYHandle:
    #             self.driver.switch_to.window(i)
    #             # 点击线下会按钮
    #             ChoosePage(self.driver).click_menu_bt("10")
    #             Model_handle = self.driver.current_window_handle
    #             # 进入到新打开的窗口中，点击联系人按钮
    #             self.wait_is_visible('x', '/html/body/div[2]/div[1]/ul/li[3]/h2/a')
    #             # 在姓名处输入需要查询的到会人
    #             self.element_value_input('x',
    #                                      '//*[@id="g-right"]/div/div[1]/div[3]/div[2]/div[1]/div[1]/div/div[3]/input',
    #                                      'yaya')
    #             # 点击筛选按钮
    #             self.wait_is_visible('x', '//*[@id="g-right"]/div/div[1]/div[3]/div[2]/div[3]/div/input[1]')
    #             time.sleep(3)
    #             # 判断最右边的共几位联系人是否不为0
    #             text = self.find_element_text('x', '//*[@id="g-right"]/div/div[1]/div[4]/div[2]/div/div[2]/span[2]')
    #             if text != "0":
    #                 self.deprint("说明联系人中含有此人")
    #                 text1 = self.find_element_text('x',
    #                                                '//*[@id="g-right"]/div/div[1]/div[5]/table/tbody/tr/td[5]/div/a')
    #                 if text1 == "yaya":
    #                     self.deprint("说明联系人中确实含有名字叫yaya的用户")
    #             #         接下来点击此用户，查看其线下会模块联系人详情显示进入专题站、报名标签触发记录信息
    #                     xpath='//*[@id="g-right"]/div/div[1]/div[5]/table/tbody/tr/td[5]/div/a'
    #                     xpath1='//*[@id="g-right"]/div/div[6]/div[2]/div/div/table/tfoot/tr/th/div/div[1]/div/button/span'
    #                     xpath2='//*[@id="g-right"]/div/div[6]/div[2]/div/div/table/tfoot/tr/th/div/div[1]/div/ul/li[2]/a'
    #                     xpath3='//*[@id="g-right"]/div/div[6]/div[2]/div/div/table/tbody'
    #                     try:
    #
    #                         text=self.Click_Enteroffline(xpath,xpath1,xpath2,xpath3,"2")
    #                         if text=="成功":
    #                             text1="成功"
    #                     except:
    #                         text1="失败"
    #                     finally:
    #                         return text1

    # def Click_Enteroffline(self,xpath,xpath1,xpath2,xpath3,flag):
    #     # 点击参会人员姓名
    #     self.wait_is_visible('x',xpath)
    #     # 切换到新开的窗口中
    #     self.driver.switch_to.window(self.driver.window_handles[-1])
    #     self.scrollbar("1500")
    #     # 将互动记录中的显示条数更改为10条
    #     self.wait_is_visible('x',xpath1)
    #     self.wait_is_visible('x',
    #                          xpath2)
    #     # 获取所有的互动类型，进行匹配
    #     # 获取了互动记录表格元素
    #     tableelement = self.driver.find_element_by_xpath('x', xpath3)
    #     trelements = tableelement.find_elements_by_tag("tr")
    #     # arrrylist将保存所有互动类型的值
    #     arrrylist = []
    #     for i in trelements:
    #         arrrylist.append(i.find_elements_by_tag("td")[1].text)
    #     # 此时进行匹配
    #     if flag=="1":
    #         if "提交表单" in arrrylist:
    #             arrrylist.remove("提交表单")
    #             text = "1"
    #         else:
    #             text = "0"
    #         if "报名" in arrrylist:
    #             arrrylist.remove("报名")
    #             text1 = "1"
    #         else:
    #             text1 = "0"
    #         if "浏览表单" in arrrylist:
    #             arrrylist.remove("浏览表单")
    #             text2 = "1"
    #         else:
    #             text2 = "0"
    #         if "进入访问专题站	" in arrrylist:
    #             arrrylist.remove("进入访问专题站")
    #             text3 = "1"
    #         else:
    #             text3 = "0"
    #         if text == "1" and text1 == "1" and text2 == "1" and text3 == "1":
    #             return "成功"
    #         else:
    #             return "失败"
    #     elif flag=="2":
    #         if "进入访问专题站	" in arrrylist:
    #             arrrylist.remove("进入访问专题站")
    #             text3 = "1"
    #         else:
    #             text3="0"
    #         if text3=="1":
    #             return "成功"
    #         else:
    #             return "失败"
    # def click_nameDetail(self,current_handle):
    #     text=""
    #     text1=""
    #     text2=""
    #     text3=""
    #     all_handles=self.driver.window_handles
    #     for i in all_handles:
    #         if i ==current_handle:
    #             self.driver.switch_to.window(i)
    #             self.driver.refresh()
    #             # 找到刚刚的联系人，点击进去查看详情
    #
    #             self.wait_is_visible('x','//*[@id="g-right"]/div/div[5]/table/tbody/tr/td[3]/div/a')
    #             # 切换到新开的窗口中
    #             self.driver.switch_to.window(self.driver.window_handles[-1])
    #             self.scrollbar("1500")
    #             # 将互动记录中的显示条数更改为10条
    #             self.wait_is_visible('x','//*[@id="g-right"]/div/div[4]/div[2]/div/table/tfoot/tr/th/div/div[1]/div/button')
    #             self.wait_is_visible('x','//*[@id="g-right"]/div/div[4]/div[2]/div/table/tfoot/tr/th/div/div[1]/div/ul/li[2]/a')
    #             # 获取所有的互动类型，进行匹配
    #             # 获取了互动记录表格元素
    #             tableelement=self.driver.find_element_by_xpath('x','//*[@id="g-right"]/div/div[4]/div[2]/div/table/tbody')
    #             trelements=tableelement.find_elements_by_tag("tr")
    #             # arrrylist将保存所有互动类型的值
    #             arrrylist=[]
    #             for i in trelements:
    #                 arrrylist.append(i.find_elements_by_tag("td")[1].text)
    #             # 此时进行匹配
    #             if "提交表单" in arrrylist:
    #                 arrrylist.remove("提交表单")
    #                 text="1"
    #             else:
    #                 text="0"
    #             if "报名" in arrrylist:
    #                 arrrylist.remove("报名")
    #                 text1="1"
    #             else:
    #                 text1="0"
    #             if "浏览表单" in arrrylist:
    #                 arrrylist.remove("浏览表单")
    #                 text2="1"
    #             else:
    #                 text2="0"
    #             if "进入访问专题站	" in arrrylist:
    #                 arrrylist.remove("进入访问专题站")
    #                 text3="1"
    #             else:
    #                 text3="0"
    #             if text=="1" and text1=="1" and text2=="1" and text3=="1":
    #                 return "成功"
    #             else:
    #                 return "失败"
    #
    #     pass

    # def New_Quest(self,current_hanlde):
    #     # 新建问卷
    #     all_handles=self.driver.window_handles
    #     for i in all_handles:
    #         if i ==current_hanlde:
    #             self.driver.switch_to.window(i)
    #             self.driver.refresh()
    #             # 点击左下角按钮
    #             self.wait_is_visible('x','/html/body/div[2]/div[2]/a[1]')
    #             # 选中互动环节
    #             self.wait_is_visible('x','//*[@id="setFiled"]/div/div/div[2]/div[4]/div[7]/label')
    #     #         点击确定按钮
    #             self.wait_is_visible('x','//*[@id="setFiled"]/div/div/div[3]/input')
    #     #         点击互动环节
    #             self.wait_is_visible('x','/html/body/div[2]/div[2]/ul[2]/li[6]/a/strong')
    #             # 点击新建互动按钮
    #             self.wait_is_visible('x','//*[@id="g-right"]/div/div[1]/div/div/a')
    #             # 点击新建问卷按钮
    #             self.wait_is_visible('x','//*[@id="g-right"]/div/div[1]/div/div/ul/li[1]/a')
    #             # NewQuestionnairePage(self.driver).creat_new_questionnaire_with_time()
    #             # NewQuestionnairePage(self.driver).edit_questionnaire_subject()
    # def Get_PCLink(self):
    #     text=self.find_element_text('x','/html/body/div[1]/div[2]/main/div/div[1]/div[2]/div[2]/div[2]/span')
    #     url1 = text.get_attribute('innerText')  # 获取链接内容，链接内容后携带了【获取链接】部分文本
    #     url2 = url1[0:28]  # 截取文本，去掉【获取链接】
    #     print "截取前的链接地址：" + url1
    #     print "投票链接地址为：" + url2
    #     js = 'window.open("' + url2 + '")'  # 新开创建打开投票链接地址
    #     self.driver.execute_script(js)
    #     time.sleep(1)
    #     self.driver.switch_to.window(self.driver.window_handles[-1])  # 切换到新开的窗口
    #     return self.driver.current_window_handle
#     def Set_Award(self,current_handle):
# #         设置领奖点
#         all_handles=self.driver.window_handles
#         for i in all_handles:
#             if i ==current_handle:
#                 self.driver.switch_to.window(i)
#                 self.driver.refresh()
#                 # 点击设置领奖点按钮
#                 self.wait_is_visible('x','//*[@id="g-right"]/div/div[2]/div[1]/div/div[3]/a[2]')
#                 # 开启领奖点
#                 self.wait_is_visible('x','//*[@id="startPoint"]/div/div/div[2]/form/div[1]/div/div/div/div/span[2]')
#                 # 点击创建新的单选框
#                 self.wait_is_visible('x','//*[@id="startPoint"]/div/div/div[2]/form/div[3]/div[1]/div/label')
#                 # 输入领奖点名称
#                 self.element_value_input('x','//*[@id="startPoint"]/div/div/div[2]/form/div[3]/div[2]/input','北京')
#                 # 点击确定按钮
#                 self.wait_is_visible('x','//*[@id="startPoint"]/div/div/div[3]/button[1]')
#     def Sub_Quest(self,current_handle):
#     #     提交问卷
#         all_handles=self.driver.window_handles
#         for i in all_handles:
#              if i ==current_handle:
#                  self.driver.switch_to.window(i)
#                  self.driver.refresh()
#     #             点击提交按钮
#                  self.wait_is_visible('x','//*[@id="questionContainer"]/div[2]/input')
#     def Add_One(self,current_handle):
#         all_handles=self.driver.window_handles
#         for i in all_handles:
#             if i ==current_handle:
#                 self.driver.switch_to.window(i)
#                 self.driver.refresh()
#                 # 点击签到点
#                 self.wait_is_visible('x','/html/body/div[2]/div[2]/ul[2]/li[5]/a')
#                 text=self.find_element_text('x','//*[@id="g-right"]/div/div[2]/div[3]/div[2]/div/table/tbody/tr/td[2]/span')
#                 return text
#         pass
    def SubMitQuest(self):
        # 该报名人员浏览并提交该问卷
        # 点击电脑图标
        self.wait_is_visible('x','//*[@id="g-right"]/div/div[2]/div[1]/div/div[3]/a[5]')
        self.driver.switch_to.window(self.driver.window_handles[-1])
        # 点击提交按钮
        self.wait_is_visible('x','//*[@id="questionContainer"]/div[2]/input')

if __name__ == '__main__':



    dr = brower()
    o = LoginPage(dr)
    o.login()

    o = ChoosePage(dr)
    time.sleep(3)
    o.click_menu_bt('9')

    o = IndexPage(dr)
    #o.click_linelist()
    o.click_linelist('2')
    o.quit()