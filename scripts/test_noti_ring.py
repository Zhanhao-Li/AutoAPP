import logging
import time

import allure
import pytest
from base.base_analyze import analyze_file
from base.base_driver import BaseDriver
from page.page import Page

class TestNotiRing:

    def setup(self):
        self.driver = BaseDriver.get_driver(False)
        self.page = Page(self.driver)

    def teardown(self):
        BaseDriver.quit_driver(True)

    @allure.severity("normal")
    @pytest.mark.parametrize("defa_ring", analyze_file("noti_ring_data", "noti_ring_all"))
    def test_noti_ring_all(self, defa_ring):
        self.page.start_page.click_noti_ring()
        logging.info('点击提示音和通知按钮')
        self.page.noti_ring_page.click_defa_ring()
        logging.info('点击默认通知铃声按钮')
        self.page.defa_noti_page.click_ring(defa_ring["defa_ring"])
        logging.info('\n 测试数据： \n defa_ring:{} '
                     .format(defa_ring["defa_ring"]))
        time.sleep(5)
        self.page.defa_noti_page.screenshot("./screenshot/defa_ring/noti_ring_{}.png".
                                         format(time.strftime("%Y%m%d%H%M%S")))
        assert self.page.defa_noti_page.whether_checked(defa_ring["defa_ring"])
        self.page.defa_noti_page.click_cert()
        logging.info('点击确定按钮')