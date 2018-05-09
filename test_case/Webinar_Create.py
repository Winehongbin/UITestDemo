# -*- coding: utf-8 -*-

from pages.common_pages.base import BasePage
from pages.webinar_pages.index_page import Webinar_IndexPage
from pages.common_pages.login_page import LoginPage
from pages.common_pages.driver import brower
from pages.common_pages.choose_page import ChoosePage
import time
from pages.webinar_pages.create_meeting import Webinar_Create
from pages.webinar_pages.Webcast_Setting import Webcast_Setting
if __name__ == '__main__':
    dr = brower()
    o = LoginPage(dr)
    o.login()
    o = ChoosePage(dr)
    time.sleep(3)
    o.click_menu_bt('8')
    o =  Webinar_IndexPage(dr)
    time.sleep(3)
    o.Index_Webinar()
    wbr = Webinar_Create(dr)
    wbr.Create_Meeting()
    # guestset = Webcast_Setting(dr)
    # guestset.Add_Guest()
    wbr.Publish_Meeting()
    wbr.Cancle_Meeting()