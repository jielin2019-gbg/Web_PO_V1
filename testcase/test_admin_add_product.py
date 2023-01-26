import time

import pytest

from pageobject.admin_manager.new_product_page import NewProductPage
from pageobject.admin_manager.product_manager_page import ProductManager
from testdata.new_prod_data import new_prod


@pytest.mark.usefixtures("admin_manage_driver")
class TestAdminAddProduct:

    def test_add_product_success(self,admin_manage_login):
        driver = admin_manage_login
        time.sleep(10)
        driver.get("http://mall.lemonban.com/admin/#/prodInfo")

        npp = NewProductPage(driver)
        npp.add_prod_img()
        npp.select_prod_category(*new_prod.get("category"))
        npp.select_prod_group(new_prod.get("group"))
        npp.add_prod_sku(new_prod.get("sku"))
        npp.select_prod_delivery()
        npp.add_prod_cn_info(new_prod.get("cn_name"), new_prod.get("cn_sale"), new_prod.get("cn_info"))
        npp.sure_add_prod()
        assert ProductManager(driver).is_product_exist(new_prod.get("cn_name"))

