from selenium.webdriver.common.by import By


class MainPage:
    login_page_click = (By.XPATH, '//a[text()="登录"]')
    show_user_name = (By.XPATH, "//a[@class='link-name']")

    log_off = (By.XPATH,'//a[text()="退出登录" ]')
