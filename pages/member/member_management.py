# -*- coding: utf-8 -*-
import time
from pages.common_pages.base import BasePage
from pages.common_pages.login_page import LoginPage
from pages.common_pages.choose_page import ChoosePage
from pages.common_pages.driver import brower
class FieldAction(BasePage):
    def new_custom_mail_field(self):
        self.element_click("id","_settingFelid")#点击属性/字段设置
        self.element_click("css","#con-basefield > div.m-tit-bar > div > div > button")#点击新增字段
        time.sleep(1)
        self.deprint(u"点击新增字段")
        self.element_value_input("x",'//*[@id="setFieldModal"]/div/div/div[2]/form/div[1]/div/input',u"自定义邮箱身份标识")#输入字段中文名称
        self.deprint(u"输入字段中文名称：自定义邮箱身份标识")
        self.element_value_input("x","//*[@id='setFieldModal']/div/div/div[2]/form/div[2]/div/input",u"zidingyiEmail")#输入字段英文名称
        self.deprint(u"输入字段中文名称：zidingyiEmail")
        self.element_click("x","//*[@id='setFieldModal']/div/div/div[2]/form/div[3]/div/div/button")#选择字段类型
        self.element_click("x","//*[@id='setFieldModal']/div/div/div[2]/form/div[3]/div/div/ul/li[2]")#选择文本字段
        self.deprint(u"字段类型：选择文本字段")
        self.element_click("x","//*[@id='setFieldModal']/div/div/div[2]/form/div[5]/div/div[1]/div/label")#选择身份标识为“是”
        self.deprint(u"是否是身份标识，选择：是")
        self.element_click("x","//*[@id='setFieldModal']/div/div/div[2]/form/div[5]/div/div[5]/div/button")#点击校验规则
        self.element_click("x","//*[@id='setFieldModal']/div/div/div[2]/form/div[5]/div/div[5]/div/ul/li[2]/a")#选择预设校验
        self.element_click("x","//*[@id='setFieldModal']/div/div/div[2]/form/div[5]/div[1]/div[6]/div/button")#选择预设校验类型
        self.element_click("x","//*[@id='setFieldModal']/div/div/div[2]/form/div[5]/div[1]/div[6]/div/ul/li[2]/a")#选择邮箱类型预设校验
        self.deprint(u"字段校验规则选择：邮箱预设校验")
        self.element_click("x","//*[@id='setFieldModal']/div/div/div[3]/button")#点击保存，保存创建的字段
        time.sleep(1)
        self.element_click("x","//*[@id='commonDialogWindow']/div/div/div[3]/button[1]")#点击确认保存
        self.deprint(u"点击保存，保存字段")
    def new_custom_list_field(self,dic_name):
        time.sleep(1)
        self.element_click("id","_settingFelid")#点击属性/字段设置
        self.element_click("css","#con-basefield > div.m-tit-bar > div > div > button")#点击新增字段
        self.deprint(u"点击新增字段")
        self.element_value_input("x",'//*[@id="setFieldModal"]/div/div/div[2]/form/div[1]/div/input',u"自定义列表字段")#输入字段中文名称
        self.deprint(u"输入字段中文名称：自定义列表字段")
        self.element_value_input("x","//*[@id='setFieldModal']/div/div/div[2]/form/div[2]/div/input",u"zidingyiList")#输入字段英文名称
        self.deprint( u"输入字段中文名称：zidingyiList")
        self.element_click("x", "//*[@id='setFieldModal']/div/div/div[2]/form/div[3]/div/div/button")#选择字段类型
        self.element_click("x", "//*[@id='setFieldModal']/div/div/div[2]/form/div[3]/div/div/ul/li[3]/a")#选择列表字段
        self.deprint(u"字段类型选择：列表字段")
        self.element_click("x","//*[@id='setFieldModal']/div/div/div[2]/form/div[5]/div[2]/div[1]/div/button")#选择点击字典表
        try:
            for num in range(1,10000):#循环获取字典表名称
                text = self.find_element_text("x","//*[@id='setFieldModal']/div/div/div[2]/form/div[5]/div[2]/div[1]/div/ul/li["+ str(num) +"]/a")#选取字典表对应的字段
                if text == dic_name:#找到对应字典表，选择该字典表
                    self.element_click("x","//*[@id='setFieldModal']/div/div/div[2]/form/div[5]/div[2]/div[1]/div/ul/li["+ str(num) +"]/a")
                    time.sleep(1)
                    break#跳出循环
        except:
            self.deprint(u"未找到需要选取的字典表")
        self.deprint(u"字典表选择"+ dic_name)
        self.element_click("x","//*[@id='setFieldModal']/div/div/div[3]/button")#点击保存，保存创建的字段
        time.sleep(1)
        self.element_click("x","//*[@id='commonDialogWindow']/div/div/div[3]/button[1]")#点击确认保存
        self.deprint(u"新增列表字段成功")
    def del_field(self,field_name):
        #变量定义为基本字段的中文名称，传入中文名称即可删除对应字段
        time.sleep(1)
        self.element_click("id", "_settingFelid")  # 点击属性/字段设置
        try:
            for num in range(1,10000):#循环获取字段名称
                text = self.find_element_text("x","//*[@id='con-basefield']/div[2]/div/div/table/tbody/tr["+ str(num) +"]/td[2]")
                if text == field_name:#中文名称相同时，删除该字段
                    self.element_click("x","//*[@id='con-basefield']/div[2]/div/div/table/tbody/tr["+ str(num) +"]/td[9]/a[2]")
                    time.sleep(1)
                    self.element_click("x","//*[@id='delModal']/div/div/div[3]/button[1]")
                    self.deprint(u"对应中文字删除成功")
                    break#跳出循环
        except:
            self.deprint(u"未找到需要删除的字段")
    def edit_form(self,form_name,choose_field1,choose_field2):
    #通过表单名称，找到表单，编辑表单，添加所有字段，删除所有字段，添加两个字段，设置为必填，然后保存
            self.element_click("x","/html/body/div[2]/div[1]/div/a[4]")#点击注册表单管理
            time.sleep(2)
            form_num = self.find_element_text("x","/html/body/div[2]/div[2]/div[1]/p/span[1]")#抓取表单数
            self.deprint(u"获得表单的总个数")
            for num in range(2,int(form_num)):
                all_form_name = self.find_element_text("x","/html/body/div[2]/div[2]/div[2]/div["+ str(num) +"]/p")#获取表单名称
                if all_form_name == form_name:#判断对应表单的名称，点击编辑按钮
                    self.deprint(u"点击编辑注册表单")
                    self.element_click("x","/html/body/div[2]/div[2]/div[2]/div["+ str(num) +"]/div[2]/a[2]/i")
                    break
            time.sleep(2)#编辑表单后，等待字段加载出来
            try:#尝试添加所有字段，直报报错，利用错误机制跳出循环
                for sign_up_num in range(1,100):
                    self.element_click("x","/html/body/div[2]/div[1]/div[2]/div[1]/ul/li/ul/li["+ str(sign_up_num) +"]/a")
            except:
                 self.deprint(u"所有字段添加完毕")
            del_list = []#列一个需要删除字段数组的位置
            for all_filed_num in range(1,sign_up_num):
                FieldName = self.find_element_AttributeText("x","/html/body/div[2]/div[1]/div[2]/div[2]/div/div["+ str(all_filed_num) +"]/div/div[1]/div/input","placeholder")
                if FieldName != u"密码":#排除密码字段序号
                    del_list.append(all_filed_num)
                    del_list.reverse()#将数组顺序反转
            for delFiledNum in del_list:#循环删除所有字段
                try:
                    self.element_click("x","/html/body/div[2]/div[1]/div[2]/div[2]/div/div["+ str(delFiledNum) +"]/div/div[2]/div[2]/a[1]")
                except:#路径有两种，利用错误机制，先尝试第一种路径，然后第二种
                    time.sleep(1)
                    self.element_click("x","/html/body/div[2]/div[1]/div[2]/div[2]/div/div["+ str(delFiledNum) +"]/div/div[2]/div/a[1]")
            for choose_num in range(1,sign_up_num-1):#循环获取字段名称
                ChooseFieldName  = self.find_element_text("x","/html/body/div[2]/div[1]/div[2]/div[1]/ul/li/ul/li["+ str(choose_num) +"]/a")
                if ChooseFieldName == choose_field1 or ChooseFieldName == choose_field2:#判断字段名，添加相应的字段
                    self.element_click("x","/html/body/div[2]/div[1]/div[2]/div[1]/ul/li/ul/li["+ str(choose_num) +"]/a")
            self.deprint(u"添加两个字段："+choose_field1 + choose_field2)
            for i in [2,3]:#选择第二个和第三个字段必填
                try:
                    self.element_click("x","/html/body/div[2]/div[1]/div[2]/div[2]/div/div["+str(i)+"]/div/div[2]/div[2]/div[1]/label")
                except:
                    self.element_click("x","/html/body/div[2]/div[1]/div[2]/div[2]/div/div["+str(i)+"]/div/div[2]/div[2]/div/label")
            self.element_click("x","/html/body/div[2]/div[1]/div[2]/div[2]/div/p/a[2]")#点击保存按钮
            time.sleep(1)
            self.element_click("x","//*[@id='commonDialogWindow']/div/div/div[3]/button[1]")#点击确认按钮
            self.deprint(u"字段添加成功")
    def get_url_sign_up(self):
        # !/usr/bin/python3.4
        # -*- coding: utf-8 -*-
        # 我的教程：http://www.cnblogs.com/TTyb/p/6046082.html
        from selenium import webdriver
        # 打开谷歌浏览器
        browser = webdriver.Chrome()
        # 打开窗口
        browser.get("https://www.baidu.com/")
        # 打开新窗口
        newwindow = 'window.open("https://www.baidu.com");'
        browser.execute_script(newwindow)
        # 切换到新的窗口
        handles = browser.window_handles
        browser.switch_to_window(handles[-1])
if __name__ == '__main__':
    dr = brower()
    o = LoginPage(dr)
    o.login()
    o = ChoosePage(dr)
    time.sleep(3)
    o.click_menu_bt('16')
    o = FieldAction(dr)
    o.edit_form(u"自动化测试专用",u"手机",u"姓名")