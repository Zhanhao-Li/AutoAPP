import logging
import time
import allure
import pytest
from base.base_analyze import analyze_file
from base.base_driver import BaseDriver
from page.page import Page

class TestDisp:

    def setup(self):
        self.driver = BaseDriver.get_driver(False)
        self.page = Page(self.driver)

    def teardown(self):
        BaseDriver.quit_driver(True)

    @allure.severity("normal")
    @pytest.mark.parametrize("search_content",analyze_file("disp_data", "disp_search"))
    def test_disp_search(self, search_content):
        self.page.start_page.click_disp()
        logging.info('点击显示按钮')
        time.sleep(5)
        self.page.disp_page.click_search()
        logging.info('点击搜索按钮')
        self.page.search_page.input_search(search_content["search_content"])
        logging.info('\n 测试数据： \n search_content:{} '
                     .format(search_content["search_content"]))
        self.page.search_page.screenshot("./screenshot/search/search_{}.png".
                                         format(time.strftime("%Y%m%d%H%M%S")))
        assert self.page.search_page.get_text() == search_content["search_content"]
        self.page.search_page.click_back()
        logging.info('点击返回按钮')