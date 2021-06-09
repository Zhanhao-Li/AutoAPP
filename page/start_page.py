import allure
from selenium.webdriver.common.by import By
from base.base_action import BaseAction


class StartPage(BaseAction):

    disp_click = By.XPATH, "//*[@text='显示']"
    noti_ring_click = By.XPATH, "//*[@text='提示音和通知']"

    @allure.step(title="点击显示按钮")
    def click_disp(self):
        self.click(self.disp_click)

    @allure.step(title="点击提示音和通知按钮")
    def click_noti_ring(self):
        self.click(self.noti_ring_click)