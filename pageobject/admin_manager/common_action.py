"""
======================
Author: 柠檬班-小简
Time: 2022/12/16 21:28
Project: Web_PO_V1
Company: 湖南零檬信息技术有限公司
======================
"""
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

class CommonAction:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def get_url(self):
        time.sleep(1)
        return self.driver.current_url

    def switch_first_nav(self):
        # 切换一级导航
        pass