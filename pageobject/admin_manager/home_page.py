"""
======================
Author: 柠檬班-小简
Time: 2022/12/16 20:54
Project: Web_PO_V1
Company: 湖南零檬信息技术有限公司
======================
"""
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from tools.basepage import BasePage


class HomePage(BasePage):

    # 用户名称元素
    user_name_span_real = (By.XPATH, '//ul[@id="dropdown-menu-2623"]')
    # user_name_span_real = (By.XPATH, '//span[@class="el-dropdown-link el-dropdown-selfdefine "]')
    user_name_span = [By.XPATH, '//span[text()="{}"]']
    exit_link = (By.XPATH,'//li[text()="退出"]')

    #
    # def __init__(self, driver: WebDriver,timeout=20):
    #     self.driver = driver
    #     self.wait = WebDriverWait(self.driver, timeout)

   # # 获取用户名称
   #  def get_user_name(self):
   #      self.wait.until(EC.visibility_of_element_located(self.user_name_span))
   #      return self.driver.find_element(*self.user_name_span).text

    def is_user_exist(self,user_name):
        # 判断用户元素是否存在。如果存在，则返回True,如果不存在，返回False4
        self.user_name_span[1] = self.user_name_span[1].format(user_name)
        try:
            self.wait.until(EC.visibility_of_element_located(self.user_name_span))
            return True
        except:
            return False

    def user_exit(self):
        self.click(self.user_name_span_real,"点击用户名称")
        self.click(self.exit_link,"点击退出")