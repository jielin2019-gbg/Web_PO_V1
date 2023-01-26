
import time

import pytest
from pageobject.admin_manager.login_page import LoginPage
from pageobject.admin_manager.home_page import HomePage

error_datas = [
    {"title": "用户名错误", "user": "student123", "passwd": "123456a", "code": "lemon", "check": "账号或密码不正确"},
    {"title": "密码错误", "user": "student", "passwd": "123456a123", "code": "lemon", "check": "账号或密码不正确"},
    {"title": "验证码错误", "user": "student", "passwd": "123456a", "code": "lemon123", "check": "验证码有误或已过期"}
]


@pytest.mark.usefixtures("admin_manage_driver")
class TestLogin:
    @pytest.mark.usefixtures("admin_manage_driver")
    def test_login_success(self, admin_manage_driver):
        driver = admin_manage_driver
        LoginPage(driver).login("student", "123456a")
        # 断言
        # assert CommonAction(driver).get_url() == "http://mall.lemonban.com/admin/#/home"
        homepage = HomePage(driver, 12)
        assert homepage.is_user_exist("student")

    @pytest.mark.usefixtures("admin_manage_driver")
    @pytest.mark.usefixtures("admin_refresh_page")
    @pytest.mark.parametrize("case", error_datas)
    def test_login_failed(self, admin_manage_driver, case):
        driver = admin_manage_driver
        LoginPage(driver).login(case.get("user"), case.get("passwd"), case.get("code"))
        assert LoginPage(driver).get_errormsg_from_top_popup() == case.get("check")
