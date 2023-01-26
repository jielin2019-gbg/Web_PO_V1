import pytest

from pageobject.user_shop.action_page import OperationPage
from pageobject.user_shop.home_page import HomePage
from pageobject.user_shop.user_login_page import LoginPage

@pytest.mark.usefixtures('user_manage_driver')
class TestUserPurchaseProd:
    def test_purchase_prod(self,user_manage_driver):
        driver = user_manage_driver
        HomePage(driver).click_login()
        LoginPage(driver).user_login("helloworld", "rabbit123")
        op = OperationPage(driver)
        op.purchase_prod("测试衣服1")
        order_num = op.get_order_number()
        op.payment_callback()
        assert op.whether_the_order_exists(order_num)

