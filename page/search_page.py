import allure
from selenium.webdriver.common.by import By
from base.base_action import BaseAction


class SearchPage(BaseAction):

    search_input = By.ID, "android:id/search_src_text"
    back_click = By.XPATH, "//*[@content-desc='收起']"

    @allure.step(title="在显示页输入框输入相应的内容")
    def input_search(self, content):
        allure.attach("输入框输入的内容", content, allure.attachment_type.TEXT)
        self.input(self.search_input, content)
        allure.attach("输入框输入内容截图", self.allure_screenshot(),
                      allure.attachment_type.PNG)

    @allure.step(title="在显示页点击返回按钮")
    def click_back(self):
        self.click(self.back_click)

    @allure.step(title="获取显示页输入框内容")
    def get_text(self):
        return self.get_result_text(self.search_input)