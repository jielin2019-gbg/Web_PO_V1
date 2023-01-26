"""
======================
Author: 柠檬班-小简
Time: 2022/12/16 20:45
Project: Web_PO_V1
Company: 湖南零檬信息技术有限公司
======================
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from tools.basepage import BasePage


class LoginPage(BasePage):

    # def __init__(self, driver: WebDriver, timeout=15):
    #     self.driver = driver
    #     self.wait = WebDriverWait(self.driver,timeout)

    # 用户名输入框
    user_input = (By.XPATH, '//input[@placeholder="用户名"]')
    # 密码输入框
    passwd_input = (By.XPATH, '//input[@placeholder="密码"]')
    # 验证码输入框
    code_input = (By.XPATH, '//input[@placeholder="验证码"]')
    # 登陆按钮
    login_button = (By.XPATH, '//input[@value="登录"]')
    # 错误提示弹出框
    errormsg_top = (By.XPATH, '//p[@class="el-message__content"]')
    # errormsg_top = (By.XPATH, '//p')


    def login(self,user, passwd,code="lemon"):
        # 输入账号
        # self.driver.find_element(*self.user_input).send_keys(user)
        self.input_text(self.user_input,"登录页面_输入用户名",user)
        # 输入密码
        # self.driver.find_element(*self.passwd_input).send_keys(passwd)
        self.input_text(self.passwd_input, "登录页面_输入密码", passwd)
        # 输入验证码
        # self.driver.find_element(*self.code_input).send_keys(code)
        self.input_text(self.code_input, "登录页面_输入验证码", code)
        # 点击登陆按钮
        # self.driver.find_element(*self.login_button).click()
        self.click(self.login_button,"登录页面_点击登录按钮")

    def get_errormsg_from_top_popup(self):
        # self.wait.until(EC.visibility_of_element_located(self.errormsg_top))
        # return self.driver.find_element(*self.errormsg_top).text
        return self.get_ele_text(self.errormsg_top,"登录页面_获取页面顶部报错提示")