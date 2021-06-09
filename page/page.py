from page.defa_noti_page import DefaNotiPage
from page.disp_page import DispPage
from page.noti_ring_page import NotiRingPage
from page.search_page import SearchPage
from page.start_page import StartPage


class Page:

    def __init__(self, driver):
        self.driver = driver

    @property
    def start_page(self):
        return StartPage(self.driver)

    @property
    def disp_page(self):
        return DispPage(self.driver)

    @property
    def search_page(self):
        return SearchPage(self.driver)

    @property
    def noti_ring_page(self):
        return NotiRingPage(self.driver)

    @property
    def defa_noti_page(self):
        return DefaNotiPage(self.driver)