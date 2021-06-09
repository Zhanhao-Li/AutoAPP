import allure
from selenium.webdriver.common.by import By
from base.base_action import BaseAction


class DispPage(BaseAction):

    search_click = By.XPATH, "//*[@content-desc='搜索']"

    @allure.step(title="点击显示页面搜索按钮")
    def click_search(self):
        self.click(self.search_click)

