from pagelocator.user_shop.home_page_locs import MainPage
from tools.basepage import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage(BasePage):

    def click_login(self):
        self.click(MainPage.login_page_click, "用户登录_点击登录")

    def exist_user_name(self):
        try:
            WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(MainPage.show_user_name))
            return True
        except:
            return False

    def show_user_name(self):
        return self.get_ele_text(MainPage.show_user_name, "用户登录_返回用户名称")

    def click_user_name(self):
        self.click(MainPage.show_user_name,"用户退出登录_点击用户名")

    def user_log_off(self):
        self.click(MainPage.log_off,"用户退出登录_点击退出登录")