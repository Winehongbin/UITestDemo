# -*- coding: utf-8 -*-
from pages.common_pages.base import BasePage
import time
class enter_meeting(BasePage):
    """进入线上会会中互动页面"""
    def Click_entermeeting(self):
        self.wait_is_visible('x','/html/body/div[1]/div[1]/div[1]/div[2]/div[1]/a[4]')
        # 切换到新开的窗口中
        self.driver.switch_to.window(self.driver.window_handles[-1])
        time.sleep(1)
    def Public_Vote(self):
        # 开始发布投票
        # 点击投票按钮
        self.wait_is_visible('x','//*[@id="accordion"]/div/ul/li[3]/a')
        # 点击发布按钮
        self.wait_is_visible('x','//*[@id="con-keyword"]/ul/li[1]/div/div/div/button[1]')

if __name__ == '__main__':
    pass