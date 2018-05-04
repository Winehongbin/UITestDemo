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
    def DelField(self,FieldName):
        time.sleep(1)
        self.element_click("id", "_settingFelid")  # 点击属性/字段设置
        for num in range(1,100):
            text = self.find_element_text("x","//*[@id='con-basefield']/div[2]/div/div/table/tbody/tr["+ str(num) +"]/td[2]")
            print(text)
            if text == FieldName:
                self.element_click("x","//*[@id='con-basefield']/div[2]/div/div/table/tbody/tr["+ str(num) +"]/td[9]/a[2]")
                time.sleep(1)
                self.element_click("x","//*[@id='delModal']/div/div/div[3]/button[1]")
                break


if __name__ == '__main__':

    dr = brower()
    o = LoginPage(dr)
    o.login()
    o = ChoosePage(dr)
    time.sleep(2)
    o.click_menu_bt('16')
    o = FieldAction(dr)
    o.NewCustomEmailField()
    o.DelField(u"自定义邮箱身份标识")