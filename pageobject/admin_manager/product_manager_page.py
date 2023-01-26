"""
======================
Author: 柠檬班-小简
Time: 2022/12/26 20:49
Project: Web_PO_V1
Company: 湖南零檬信息技术有限公司
======================
"""
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pagelocator.admin_manager.product_manager_page_locs import ProductManagerLocs as loc

class ProductManager:

    def __init__(self, driver: WebDriver, timeout=20):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, timeout)

    def click_new_prodct_action(self):
        self.wait.until(EC.visibility_of_element_located(loc.add_prod_button))
        self.driver.find_element(*loc.add_prod_button).click()

    def is_product_exist(self,prod_name):
        # 判断用户元素是否存在。如果存在，则返回True,如果不存在，返回False4
        loc.prod_name_loc[1] = loc.prod_name_loc[1].format(prod_name)
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loc.prod_name_loc))
            return True
        except:
            return False


