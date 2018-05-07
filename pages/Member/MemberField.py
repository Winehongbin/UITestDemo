# -*- coding: utf-8 -*-
import time
from pages.common_pages.base import BasePage
from pages.common_pages.login_page import LoginPage
from pages.common_pages.choose_page import ChoosePage
from pages.common_pages.driver import brower
class FieldAction(BasePage):
    def NewCustomEmailField(self):
        self.element_click("id","_settingFelid")#点击属性/字段设置
        self.element_click("css","#con-basefield > div.m-tit-bar > div > div > button")#点击新增字段
        self.element_value_input("x",'//*[@id="setFieldModal"]/div/div/div[2]/form/div[1]/div/input',u"自定义邮箱身份标识")#输入字段中文名称
        self.element_value_input("x","//*[@id='setFieldModal']/div/div/div[2]/form/div[2]/div/input",u"zidingyiEmail")#输入字段英文名称
        self.element_click("x","//*[@id='setFieldModal']/div/div/div[2]/form/div[3]/div/div/button")#选择字段类型
        self.element_click("x","//*[@id='setFieldModal']/div/div/div[2]/form/div[3]/div/div/ul/li[2]")#选择文本字段
        self.element_click("x","//*[@id='setFieldModal']/div/div/div[2]/form/div[5]/div/div[1]/div/label")#选择身份标识为“是”
        self.element_click("x","//*[@id='setFieldModal']/div/div/div[2]/form/div[5]/div/div[5]/div/button")#点击校验规则
        self.element_click("x","//*[@id='setFieldModal']/div/div/div[2]/form/div[5]/div/div[5]/div/ul/li[2]/a")#选择预设校验
        self.element_click("x","//*[@id='setFieldModal']/div/div/div[2]/form/div[5]/div[1]/div[6]/div/button")#选择预设校验类型
        self.element_click("x","//*[@id='setFieldModal']/div/div/div[2]/form/div[5]/div[1]/div[6]/div/ul/li[2]/a")#选择邮箱类型预设校验
        self.element_click("x","//*[@id='setFieldModal']/div/div/div[3]/button")#点击保存，保存创建的字段
        time.sleep(1)
        self.element_click("x","//*[@id='commonDialogWindow']/div/div/div[3]/button[1]")#点击确认保存
    def NewCustomListField(self,DicName):
        time.sleep(1)
        self.element_click("id","_settingFelid")#点击属性/字段设置
        self.element_click("css","#con-basefield > div.m-tit-bar > div > div > button")#点击新增字段
        self.element_value_input("x",'//*[@id="setFieldModal"]/div/div/div[2]/form/div[1]/div/input',u"自定义列表字段")#输入字段中文名称
        self.element_value_input("x","//*[@id='setFieldModal']/div/div/div[2]/form/div[2]/div/input",u"zidingyiList")#输入字段英文名称
        self.element_click("x", "//*[@id='setFieldModal']/div/div/div[2]/form/div[3]/div/div/button")#选择字段类型
        self.element_click("x", "//*[@id='setFieldModal']/div/div/div[2]/form/div[3]/div/div/ul/li[3]/a")#选择列表字段
        self.element_click("x","//*[@id='setFieldModal']/div/div/div[2]/form/div[5]/div[2]/div[1]/div/button")#选择点击字段表
        try:
            for num in range(1,10000):#循环获取字段名称
                text = self.element_click("x","//*[@id='setFieldModal']/div/div/div[2]/form/div[5]/div[2]/div[1]/div/ul/li["+ str(num) +"]/a")#选取字典表对应的字段
                print(text)
                
                if text == DicName:#中文名称相同时，删除该字段
                    self.element_click("x","//*[@id='setFieldModal']/div/div/div[2]/form/div[5]/div[2]/div[1]/div/ul/li["+ str(num) +"]/a")
                    time.sleep(1)
                    break#跳出循环
        except:
            print u"未找到需要选取的字典表"
        self.element_click("x","//*[@id='setFieldModal']/div/div/div[3]/button")#点击保存，保存创建的字段
        time.sleep(1)
        self.element_click("x","//*[@id='commonDialogWindow']/div/div/div[3]/button[1]")#点击确认保存
    def DelField(self,FieldName):
        time.sleep(1)
        self.element_click("id", "_settingFelid")  # 点击属性/字段设置
        try:
            for num in range(1,10000):#循环获取字段名称
                text = self.find_element_text("x","//*[@id='con-basefield']/div[2]/div/div/table/tbody/tr["+ str(num) +"]/td[2]")
                print(text)
                if text == FieldName:#中文名称相同时，删除该字段
                    self.element_click("x","//*[@id='con-basefield']/div[2]/div/div/table/tbody/tr["+ str(num) +"]/td[9]/a[2]")
                    time.sleep(1)
                    self.element_click("x","//*[@id='delModal']/div/div/div[3]/button[1]")
                    break#跳出循环
        except:
            print u"未找到需要删除的字段"
if __name__ == '__main__':
    dr = brower()
    o = LoginPage(dr)
    o.login()
    o = ChoosePage(dr)
    time.sleep(3)
    o.click_menu_bt('16')
    o = FieldAction(dr)
#    o.NewCustomEmailField()
    o.NewCustomListField(u"省市")
    o.DelField(u"自定义邮箱身份标识")
    o.DelField(u"自定义列表字段")