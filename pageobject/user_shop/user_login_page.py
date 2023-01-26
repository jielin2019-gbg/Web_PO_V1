from time import sleep

from pagelocator.user_shop.user_login_page_locs import LoginPage as LP

from tools.basepage import BasePage


class LoginPage(BasePage):

    def user_login(self,user, passwd):
        # 输入账号
        # self.driver.find_element(*self.user_input).send_keys(user)
        self.input_text(LP.user_name_input,"用户登录页面_输入用户名",user)
        # 输入密码
        # self.driver.find_element(*self.passwd_input).send_keys(passwd)
        self.input_text(LP.passwd_input, "用户登录页面_输入密码", passwd)
        # 点击登陆按钮
        # self.driver.find_element(*self.login_button).click()
        self.click(LP.login_btn,"用户登录页面_点击登录按钮")

    def get_errormsg_from_top_popup(self):
        # self.wait.until(EC.visibility_of_element_located(self.errormsg_top))
        return self.get_ele_text(LP.popup_massage,"用户登录页面_获取页面顶部报错提示")