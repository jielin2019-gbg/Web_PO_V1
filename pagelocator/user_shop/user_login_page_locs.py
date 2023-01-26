from selenium.webdriver.common.by import By


class LoginPage:
    user_name_input = (By.XPATH,'//input[@placeholder="请输入手机号/用户名"]')
    passwd_input = (By.XPATH,'//input[@placeholder="请输入密码"]')
    login_btn = (By.XPATH,"//a[@class='login-button']")

    popup_massage = (By.XPATH, '//p[@class="el-message__content"]')

