# -*- utf-8 -*-
from pages.common_pages.driver import brower
from pages.common_pages.base import BasePage
from pages.common_pages.login_page import LoginPage
from pages.common_pages.choose_page import ChoosePage
from pages.webinar_pages.create_meeting import Webinar_Create

from pages.webinar_pages.Guest_Manager import get_guestnum
import time

class Webcast_Setting(BasePage):


    def Add_Guest(self):

        self.wait_is_visible('x','/html/body/div[1]/div[2]/div[2]/div/div[3]/h2/div/a[1]')

        guestnumb = self.find_element_text('x','//*[@id="guestDb"]/div/div/div[3]/div')
if __name__ == '__main__':
    dr = brower()

    a = get_guestnum(dr)
    b = a.get_num()
    print b
