import allure
from selenium.webdriver.common.by import By
from base.base_action import BaseAction


class DefaNotiPage(BaseAction):

    cert_click = By.XPATH, "//*[@text='确定']"
    ring_click = By.XPATH, "//*[@text='{}']"

    @allure.step(title="点击默认提示铃声确定按钮")
    def click_cert(self):
        self.click(self.cert_click)

    @allure.step(title="选择默认提示铃声")
    def click_ring(self,defa_ring):
        allure.attach("所选择的默认提示铃声", defa_ring, allure.attachment_type.TEXT)
        self.click_defa_ring(self.ring_click,defa_ring)
        allure.attach("选择的默认提示铃声截图", self.allure_screenshot(),
                      allure.attachment_type.PNG)

    @allure.step(title="判断相应的默认提示铃声是否已选择")
    def whether_checked(self, defa_ring):
        return self.whether_ring_checked(self.ring_click,defa_ring)