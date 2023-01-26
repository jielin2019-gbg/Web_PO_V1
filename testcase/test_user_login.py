import time

import pytest
from pageobject.user_shop.home_page import HomePage
from pageobject.user_shop.user_login_page import LoginPage

error_datas = [
    {"title": "用户名错误", "user": "helloworl", "passwd": "rabbit123", "check": "账号或密码不正确"},
    {"title": "密码错误", "user": "helloworld", "passwd": "rabbit", "check": "账号或密码不正确"},
]


# @pytest.mark.usefixtures("manage_driver")
class TestLogin:
    # @pytest.mark.usefixtures("manage_driver")
    # def test_login_success(self, manage_driver):
    #     driver = manage_driver
    #     LoginPage(driver).login("student", "123456a")
    #     # 断言
    #     # assert CommonAction(driver).get_url() == "http://mall.lemonban.com/admin/#/home"
    #     assert HomePage(driver,12).is_user_exist("student")
    @pytest.mark.usefixtures("user_manage_driver")
    @pytest.mark.usefixtures("user_refresh_page")
    def test_login_success(self, user_manage_driver):
        driver = user_manage_driver
        hp = HomePage(driver)
        lp = LoginPage(driver)
        hp.click_login()
        lp.user_login("helloworld", "rabbit123")
        # hp.exist_user_name()
        assert hp.show_user_name() == 'helloworld'
        hp.click_user_name()
        hp.user_log_off()
        time.sleep(5)

    @pytest.mark.usefixtures("user_manage_driver")
    @pytest.mark.usefixtures("user_refresh_page")
    @pytest.mark.parametrize("case", error_datas)
    def test_login_failed(self, user_manage_driver, case):
        driver = user_manage_driver
        hp = HomePage(driver)
        lp = LoginPage(driver)
        hp.click_login()
        lp.user_login(case.get("user"), case.get("passwd"))
        # hp.exist_user_name()
        assert lp.get_errormsg_from_top_popup() == case.get("check")
