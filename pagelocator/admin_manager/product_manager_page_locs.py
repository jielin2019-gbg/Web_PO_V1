"""
======================
Author: 柠檬班-小简
Time: 2022/9/24 20:04
Project: day8_PO_V3
Company: 湖南零檬信息技术有限公司
======================
"""
from selenium.webdriver.common.by import By

class ProductManagerLocs:

    # 新增产品的按钮
    add_prod_button = (By.XPATH, '//span[text()="新增"]')
    prod_name_loc = [By.XPATH, '//tr//td//span[text()="{}"]']
