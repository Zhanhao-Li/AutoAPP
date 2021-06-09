from selenium.webdriver.support.wait import WebDriverWait


class BaseAction:

    def __init__(self, driver):
        self.driver = driver

    def override_find_element(self, feature, timeout=10, poll_frequency=0.5):
        return WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll_frequency).\
            until(lambda driver:driver.find_element(*feature))

    def override_find_ring_element(self, feature, defa_ring, timeout=10, poll_frequency=0.5):
        return WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll_frequency).\
            until(lambda driver:driver.find_element(feature[0], feature[1].format(defa_ring)))

    def find_toast(self, msg, timeout=10, poll_frequency=0.2):
        return WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll_frequency).\
            until(lambda driver: driver.find_element_by_xpath
            ("//*[contains(@text, '%s')]" % msg))

    def click(self, feature):
        self.override_find_element(feature).click()

    def click_defa_ring(self, feature, defa_ring):
        self.override_find_ring_element(feature, defa_ring).click()

    def input(self, feature, content):
        self.override_find_element(feature).send_keys(content)

    def screenshot(self, img_path):
        self.driver.get_screenshot_as_file(img_path)

    def allure_screenshot(self):
        self.driver.get_screenshot_as_png()

    def get_result_text(self, feature):
        return self.override_find_element(feature).text

    def whether_ring_checked(self, feature, defa_ring):
        return self.override_find_ring_element(feature, defa_ring).get_attribute("checked")