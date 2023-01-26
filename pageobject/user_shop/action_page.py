import time

import requests

from pagelocator.user_shop import action_page_locs as locs
from pagelocator.user_shop.home_page_locs import MainPage
from tools.basepage import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class OperationPage(BasePage):

    def purchase_prod(self,product_name):
        self._place_order(product_name)
        self._submit_order_and_pay()

    def _place_order(self,product_name):
        self.input_text(locs.search_box,"输入商品名称",product_name)
        self.click(locs.search_btn,"点击搜索按键")
        locs.select_product[1] = locs.select_product[1].format(product_name)
        self.click(locs.select_product,"点击要下单的商品")
        self.click(locs.buy_now,"点击立即购买")

    def _submit_order_and_pay(self):
        self.click(locs.submit_order,"点击提交订单")
        self.click(locs.wechat_payment,"点击微信支付")
        self.click(locs.pay_immediately,"点击立即支付")

    def get_order_number(self):
        self.click(locs.my_order,"点击我的订单")
        self.click(locs.wait_payment,"点击待支付")
        order_num = self.get_ele_text(locs.get_order_num,"获取订单号")
        setattr(OperationPage,"order_num",order_num)
        return order_num

    def payment_callback(self):
        url = "http://mall.lemonban.com:8107/notice/pay/3"
        data = {
                    "payNo":"{}".format(getattr(OperationPage,"order_num")),
                    "bizPayNo":str(int(time.time()*1000)),
                    "isPaySuccess": True
                }
        headers = {'locale': 'zh_CN'}
        res = requests.post(url=url,json = data, headers=headers)
        print("支付回调：",res.text)

    def whether_the_order_exists(self,ele):
        self.click(locs.to_be_shipped,"选择待发货")
        locs.confirm_order_no[1] = locs.confirm_order_no[1].format(ele)
        return self.wait_until_page_contains_ele(locs.confirm_order_no,"待发货存在该订单号")
















