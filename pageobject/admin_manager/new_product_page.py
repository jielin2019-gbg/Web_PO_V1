"""
======================
Author: 柠檬班-小简
Time: 2022/12/26 20:49
Project: Web_PO_V1
Company: 湖南零檬信息技术有限公司
======================
"""

from pagelocator.admin_manager.new_product_page_locs import NewProductPageLoc as loc
from tools.basepage import BasePage


class NewProductPage(BasePage):

    # 选择产品图片
    def add_prod_img(self):
        # 点击+号，进入选择图片。
        # self.wait.until(EC.visibility_of_element_located(loc.add_prod_image_button))
        # self.driver.find_element(*loc.add_prod_image_button).click()
        self.click(loc.add_prod_image_button,"新增产品_添加图片")
        # 选择第一张图片。
        # self.wait.until(EC.visibility_of_element_located(loc.first_image))
        # self.driver.find_element(*loc.first_image).click()
        self.click(loc.first_image, "新增产品_选择第一个图片")
        self.click(loc.select_one_image_sure, "新增产品_选择第一个图片_点击确认")
        # self.driver.find_element(*loc.select_one_image_sure).click()

    # 产品的一级，二级，三级分类。
    def select_prod_category(self,first,second,third):
        # 元素定位替换
        loc.select_first_category[1] = loc.select_first_category[1].format(first)
        loc.select_second_category[1] = loc.select_second_category[1].format(second)
        loc.select_third_category[1] = loc.select_third_category[1].format(third)
        # 先把下分类列表点出来
        # self.wait.until(EC.visibility_of_element_located(loc.add_prod_category_input))
        # self.driver.find_element(*loc.add_prod_category_input).click()
        self.click(loc.add_prod_category_input,"新增产品列表_点出下拉列表")
        # 先选一级，再选二级，再选三级
        # self.wait.until(EC.visibility_of_element_located(loc.select_first_category))
        # self.driver.find_element(*loc.select_first_category).click()
        self.click(loc.select_first_category, "新增产品列表_点出下拉列表_第一级")
        self.click(loc.select_second_category, "新增产品列表_点出下拉列表_第二级")
        self.click(loc.select_third_category, "新增产品列表_点出下拉列表_第三级")
        # self.wait.until(EC.visibility_of_element_located(loc.select_second_category))
        # self.driver.find_element(*loc.select_second_category).click()
        # self.wait.until(EC.visibility_of_element_located(loc.select_third_category))
        # self.driver.find_element(*loc.select_third_category).click()

    # 产品分组
    def select_prod_group(self,group_name):
        # 元素定位替换
        loc.group_name[1] = loc.group_name[1].format(group_name)
        # 将分组下拉列表点出来
        # self.wait.until(EC.visibility_of_element_located(loc.add_prod_group))
        # self.driver.find_element(*loc.add_prod_group).click()
        self.click(loc.add_prod_group,"新增产品_点出分组列表")
        # 选择分组
        # self.wait.until(EC.visibility_of_element_located(loc.group_name))
        # self.driver.find_element(*loc.group_name).click()
        self.click(loc.group_name, "新增产品_选择分组")
        # 点击收起
        # self.driver.find_element(*loc.add_prod_group).click()
        self.click(loc.product_group_fold, "新增产品_收起分组列表")

    # 设置库存规模（有6个值要设置）
    def add_prod_sku(self,values_list):
        """
        :param values_list: 列表类型。而且列表中的值的顺序，与页面当中库存规模所需值的顺序保持一致。
        :return:
        """
        # self.wait.until(EC.visibility_of_element_located(loc.add_prod_storage))
        # 得到页面上6个输入框
        # eles = self.driver.find_elements(*loc.add_prod_storage)
        eles = self.wait_until_ele_visible(loc.add_prod_storage, "新增产品_等待输入框出现", all=True)
        for index, input_ele in enumerate(eles):
            # 元素的索引是第几，那么就从列表当中取对应索引的值，输入。
            # input_ele.send_keys(values_list[index])
            self.input_text(input_ele,f"设置第{index+1}个参数",values_list[index])

    # 选择物流信息
    def select_prod_delivery(self):
        # 先把下拉列表点出来的
        # self.wait.until(EC.visibility_of_element_located(loc.add_prod_delivery))
        # self.driver.find_element(*loc.add_prod_delivery).click()
        self.click(loc.add_prod_delivery,"新增产品_点出物流信息")
        # 选择包邮
        # self.wait.until(EC.visibility_of_element_located(loc.delivery_free))
        # self.driver.find_element(*loc.delivery_free).click()
        self.click(loc.delivery_free, "新增产品_选择包邮")

    # 添加产品中文详情
    def add_prod_cn_info(self,cn_name,cn_sale,cn_info):
        # 中文名称
        # self.wait.until(EC.visibility_of_element_located(loc.add_prod_cn_name))
        # self.driver.find_element(*loc.add_prod_cn_name).send_keys(cn_name)
        self.input_text(loc.add_prod_cn_name,"新增产品_输入中文名称",cn_name)
        # 中文卖点
        # self.wait.until(EC.visibility_of_element_located(loc.add_prod_cn_sail_feature))
        # self.driver.find_element(*loc.add_prod_cn_sail_feature).send_keys(cn_sale)
        self.input_text(loc.add_prod_cn_sail_feature, "新增产品_输入中文卖点", cn_sale)
        # 中文描述 -- 先切入iframe，再输入描述信息，再退出iframe
        # self.driver.switch_to.frame(self.driver.find_element(*loc.add_product_description_iframe))
        self.switch_to_iframe(loc.add_product_description_iframe,"新增产品_切换到iframe")
        # self.driver.find_element(*loc.add_product_description_p).send_keys(cn_info)
        self.input_text(loc.add_product_description_p, "新增产品_输入中文名称", cn_info)
        # self.driver.switch_to.default_content()
        self.switch_to_default()

    # 提交产品
    def sure_add_prod(self):
        # self.wait.until(EC.visibility_of_element_located(loc.sure_add_prod_button))
        # self.driver.find_element(*loc.sure_add_prod_button).click()
        self.click(loc.sure_add_prod_button,"新增产品_提交产品")

if __name__ == '__main__':
    # 初始化会话对象
    from selenium import webdriver
    driver = webdriver.Chrome()
    # 右键  run file in python console
