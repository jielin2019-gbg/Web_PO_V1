import os
import time

import pyautogui
from loguru import logger
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from tools.settings import pageshots_dir


class BasePage:

    def __init__(self,driver:WebDriver,timeout=20,poll_frequency=0.5):
        self.driver = driver
        self.wait = WebDriverWait(self.driver,timeout,poll_frequency)

    def wait_until_ele_visible(self,locs,page_action,all=False):
        logger.info(f"等待{locs}可见")
        try:
            if all:
                logger.info(f"等待匹配{locs}的所有个元素可见.....")
                ele = self.wait.until(EC.visibility_of_all_elements_located(locs))
            else:
                logger.info(f"等待匹配{locs}的第一个元素可见。。。")
                ele = self.wait.until(EC.visibility_of_element_located(locs))
        except:
            logger.exception("等待失败！请确认元素定位是否正确，是否在运行过程中发生了改变，是否在iframe中")
            self.save_page_shot(page_action)
            raise

        logger.info("等待成功！")
        return ele

    def save_page_shot(self,page_action):
        cur_time = time.strftime("%Y%m%d_%H%M%S",time.localtime())
        file_name = f"{page_action}_{cur_time}.png"
        filepath = os.path.join(pageshots_dir,file_name)
        self.driver.save_screenshot(filepath)
        logger.info(f"将页面截图保存至：{filepath}")

    def wait_until_page_contains_ele(self,locator, page_step):
        logger.info(f"等待元素{locator}存在于页面中。。。")
        try:
            ele = self.wait.until(EC.presence_of_element_located(locator))
        except:
            logger.exception("等待失败。。。")
            self.save_page_shot(page_step)
            raise
        logger.info("等待成功")
        return ele

    def get_element(self,locator, page_step):
        logger.info(f"查找元素{locator}。。。")
        try:
            ele = self.driver.find_element(*locator)
        except:
            logger.exception("查找元素失败。。。")
            self.save_page_shot(page_step)
            raise
        logger.info("查找元素成功")
        return ele

    def click(self,locator, page_step):
        ele = self.wait_until_ele_visible(locator,page_step)
        logger.info(f"点击元素{locator}")
        try:
            ele.click()
        except:
            logger.exception("点击元素失败,尝试用js点击")
            self.click_by_js(ele,page_step)

    def click_by_js(self,ele, page_step):
        if isinstance(ele,(tuple, list)):
            ele = self.wait_until_ele_visible(ele,page_step)
        try:
            self.driver.execute_script("arguments[0].click",ele)
            logger.info("js点击成功")
        except:
            logger.exception("js点击失败")
            self.save_page_shot(page_step)
            raise

    def input_text(self,locator, page_step,*value):
        if isinstance(locator,(tuple,list)):
            ele = self.wait_until_ele_visible(locator, page_step)
        else:
            ele = locator
        logger.info(f"在{locator}输入文本{value}")
        try:
            ele.clear()
            ele.send_keys(*value)
        except:
            logger.exception("输入文本失败")
            self.save_page_shot(page_step)
            raise

    def get_ele_text(self,locator, page_step):
        ele = self.wait_until_page_contains_ele(locator,page_step)
        # time.sleep(1)
        logger.info(f"获取元素{locator}的文本")
        try:
            value = ele.text
            logger.info(f"获取到的值为{value}")
            return value
        except:
            logger.exception("获取文本失败")
            self.save_page_shot(page_step)
            raise

    def get_ele_attr(self,locator,page_step,attr_name):
        ele = self.wait_until_page_contains_ele(locator,page_step)
        logger.info(f"获取元素{locator}的属性{attr_name}的值")
        try:
            value = ele.get_attribute(attr_name)
            logger.info(f"获取的属性值为：{value}")
        except:
            logger.exception("获取元素属性失败。")
            self.save_page_shot(page_step)
            raise

    def switch_to_iframe(self,locator,page_step):
        logger.info("切换到iframe。")
        try:
            self.wait.until(EC.frame_to_be_available_and_switch_to_it(locator))
            logger.info("切换iframe成功")
        except:
            logger.exception("切换iframe失败")
            self.save_page_shot(page_step)
            raise

    def switch_to_default(self):
        logger.info("切换到默认的html中去")
        try:
            self.driver.switch_to.default_content()
            logger.info("切换回html成功")
        except:
            logger.exception("切换失败")
            raise

    def switch_to_window(self,page_step, index=-1):
        time.sleep(0.5)
        logger.info("切换到指定窗口")
        win_handles = self.driver.window_handles
        try:
            self.driver.switch_to.window(win_handles[index])
            logger.info(f"切换窗口到{win_handles[index]}")
        except:
            logger.exception("切换窗口失败！")
            self.save_page_shot(page_step)
            raise

    def set_value_by_js(self,locator,page_step,content):
        ele = self.wait_until_ele_visible(locator,page_step)
        logger.info(f"通过js语句设置{locator}的value值设置为：{content}")
        try:
            self.driver.execute_script("arguments[0].value = arguments[1]",ele,content)
        except:
            logger.exception("无法用js设置value值。")
            self.save_page_shot(page_step)
            raise

    def select_value_by_Select(self,locator,page_step,value,type=0):
        ele = self.wait_until_ele_visible(locator, page_step)
        s = Select(ele)
        logger.info("使用Select类，对下拉列表选择值")
        try:
            if type == 0:
                s.select_by_value(value)
            elif type == 1:
                s.select_by_index(value)
            else:
                s.select_by_visible_text(value)
        except:
            logger.exception("下拉框选择失败")
            self.save_page_shot(page_step)
            raise

    def close_alert(self):
        time.sleep(0.5)
        try:
            alert = Alert(self.driver)
            alert.accept()
        except:
            logger.exception("关闭弹窗失败。")
            raise

    def scroll_ele_to_view(self,locator,page_step,top=True):
        """

        :param locator:
        :param step_page:
        :param top:
        :return:
        """
        ele = self.wait_until_ele_visible(locator,page_step)
        logger.info("将元素滚动到可见区域。")
        try:
            if top == True:
                logger.info("元素与页面顶部对齐")
                ele.location_once_scrolled_into_view
            else:
                logger.info("元素与页面底部对齐")
                self.driver.execute_script("arguments[0].scrollIntoView(false);",ele)
        except:
            logger.exception("将元素滚动到可见区域失败")
            self.save_page_shot(page_step)
            raise

    def scroll_to_find_element(self,locator,page_step,for_count,x=0,y=800):
        for index in for_count:
            try:
                WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(locator))
                logger.info("找到元素了")
                break
            except:
                logger.info(f"第{index + 1}次滚动滚动条.....")
                self.driver.execute_script(f"window.scrollBy({x},{y})")
                time.sleep(0.5)
                self.save_page_shot(page_step+f"_第{index+1}次滚动")

    def upload_file(self,file_path):
        logger.info(f"上传文件{file_path}")
        time.sleep(1)
        try:
            # 使用pyautogui输入文件地址，上传。
            pyautogui.typewrite(file_path)
            pyautogui.press(keys='ENTER', presses=3)  # ENTER 大小写都可以
        except:
            logger.exception("上传文件失败。")
            raise


if __name__ == '__main__':
    from selenium import webdriver

    driver = webdriver.Chrome()







