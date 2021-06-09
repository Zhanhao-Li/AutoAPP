import allure
from selenium.webdriver.common.by import By
from base.base_action import BaseAction


class NotiRingPage(BaseAction):

    defa_ring_click = By.XPATH, "//*[@text='默认通知铃声']"

    @allure.step(title="点击默认通知铃声按钮")
    def click_defa_ring(self):
        self.click(self.defa_ring_click)


