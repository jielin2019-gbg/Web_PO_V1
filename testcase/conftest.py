
import pytest
from selenium import webdriver

from pageobject.admin_manager.login_page import LoginPage
from tools.settings import admin_info


@pytest.fixture(scope="class")
def user_manage_driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("Http://mall.lemonban.com:3344/")
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def user_refresh_page(user_manage_driver):
    user_manage_driver.refresh()


@pytest.fixture(scope="class")
def admin_manage_driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://mall.lemonban.com/admin/#/login")
    yield driver
    driver.quit()


@pytest.fixture(scope="class")
def admin_manage_login(admin_manage_driver):
    driver = admin_manage_driver
    LoginPage(driver).login(*admin_info)
    yield driver


@pytest.fixture(scope="function")
def admin_refresh_page(admin_manage_driver):
    admin_manage_driver.get("http://mall.lemonban.com/admin/#/login")
