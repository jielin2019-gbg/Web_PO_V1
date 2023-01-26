import time

from selenium import webdriver
from pywinauto.keyboard import SendKeys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
""""""


from faker import Faker
fk=Faker(locale='zh_cn')


driver=webdriver.Chrome()

#隐性等待
driver.implicitly_wait(10)
#显示等待
wait=WebDriverWait(driver,10)
#访问柠檬商城后台
driver.get("http://mall.lemonban.com/admin/#/login")
driver.maximize_window()

#输入账号
driver.find_element(By.XPATH,'//input[@placeholder="用户名"]').send_keys("student")
#输入密码
driver.find_element(By.XPATH,'//input[@placeholder="密码"]').send_keys("123456a")
#输入验证码
driver.find_element(By.XPATH,'//input[@placeholder="验证码"]').send_keys("lemon")
#点击登陆按钮
driver.find_element(By.XPATH,'//input[@value="登录"]').click()


#点击产品管理模块
driver.find_element(By.XPATH,'//div[@class="el-submenu__title"]//span[text()="产品管理"]').click()
#点击子模块：产品管理模块
driver.find_element(By.XPATH,'//ul[@role="menu"]//span[text()="产品管理"]').click()
#点击新增
driver.find_element(By.XPATH,'//span[text()="新增"]').click()
#点击商品图片
driver.find_element(By.XPATH,'//div[@class="mul-pic-upload"]//i[@class="el-icon-plus"]').click()
# #点击上传图片
# driver.find_element(By.XPATH,'//div[@id="tab-upload"]').click()
# #点击上传图片按钮
# driver.find_element(By.XPATH,'//div[@class="upload-img-preview"]//i[@class="el-icon-plus"]').click()
# time.sleep(1)
# send_keys(r'E:\my_dog.jpg')
# send_keys('{ENTER}')
# time.sleep(2)
# #点击确认上传按钮
# driver.find_element(By.XPATH,'//button//span[text()="确定上传"]').click()

# 点击选择图片
driver.find_element(By.XPATH,'//div[@id="tab-pick"]').click()
#图片输入框：输入图片名称
driver.find_element(By.XPATH,'//input[@placeholder="图片名称"]').send_keys("my_dog")
#点击查询
driver.find_element(By.XPATH,'//span[text()="查询"]').click()
time.sleep(5)
#选择上传的图片
driver.find_element(By.XPATH,'//img[@src="http://mall.lemonban.com:8108/2022/07/b72610b8daa24c89b7b70f79a1dcba7c.jpg"]').click()
# 点击确定按钮
driver.find_element(By.XPATH,'//div[@class="el-badge item"]//span[text()="确 定"]').click()


#点击产品输入框
driver.find_element(By.XPATH,'//div[@class="el-cascader"]//input[@placeholder="请选择"]').click()
#点击食品饮料
driver.find_element(By.XPATH,'//span[text()="食品饮料"]').click()
#点击食品
driver.find_element(By.XPATH,'//span[text()="食品"]').click()
#点击休闲食品
driver.find_element(By.XPATH,'//span[text()="休闲食品"]').click()
# 再次点击产品输入框，让弹框消失。
driver.find_element(By.XPATH,'//div[@class="el-cascader"]//input[@placeholder="请选择"]').click()


time.sleep(1)
#点击产品分组输入框
driver.find_element(By.XPATH,'//label[text()="产品分组"]/following-sibling::div//input[@placeholder="请选择"]').click()
#点击每日上新
driver.find_element(By.XPATH,'//span[text()="每日上新"]').click()
time.sleep(2)
#y轴滑动800像素
driver.execute_script("window.scrollTo(0,800)")
time.sleep(2)
# #点击添加规格按钮
# driver.find_element(By.XPATH,'//span[text()="添加规格"]').click()
# time.sleep(1)
# #点击规格名输入框
# driver.find_element(By.XPATH,'//label[text()="商品规格"]/following-sibling::div//input[@class="el-input__inner"]').click()
# #点击颜色
# driver.find_element(By.XPATH,'//span[text()="颜色"]').click()
# #点击规格值输入框
# driver.find_element(By.XPATH,'//input[@class="el-select__input"]').click()
# #点击金色
# driver.find_element(By.XPATH,'//span[text()="金色"]').click()
# #点击确定
# driver.find_element(By.XPATH,'//button/preceding-sibling::button//span[text()="确 定"]').click()

#批量设置
eles=driver.find_elements(By.XPATH,'//tr//input[@class="el-input__inner"]')
num=fk.random_int(min=1000000000,max=9999999999)
a=0
for i in eles:
    a+=1
    i.clear()
    time.sleep(2)
    if a == 1:
        i.send_keys("80")
    elif a == 2:
        i.send_keys("120")
    elif a == 3:
        i.send_keys("100")
    elif a == 4:
        i.send_keys(f'{num}')
    elif a == 5:
        i.send_keys("10")
    else:
        i.send_keys("20")

#运费设置
driver.find_element(By.XPATH,'//button[@type="button"]/preceding-sibling::div//input').click()
#点击包邮
driver.find_element(By.XPATH,'//span[text()="包邮"]').click()

#y轴滑动像素1600
driver.execute_script("window.scrollTo(800,1600)")

#输入商品名称
driver.find_element(By.XPATH,'//input[@placeholder="商品名称"]').send_keys("帅气的狗头")
#输入产品卖点
driver.find_element(By.XPATH,'//textarea[@placeholder="产品卖点"]').send_keys("py49期UI自动化")

#点击插入
driver.find_element(By.XPATH,'//button[@id="mceu_33-open"]//span[text()="插入"]').click()
time.sleep(1)
#点击图片
driver.find_element(By.XPATH,'//span[text()="图片"]').click()
time.sleep(1)
#输入图片地址
img="http://img11.360buyimg.com/imgzone/jfs/t1/88023/34/6007/532691/5df0aecbEb409e30f/d6434715ba97fe4b.jpg"
driver.find_element(By.XPATH,'//input[@class="mce-textbox"]').send_keys(img)
time.sleep(2)
#输入图片描述
driver.find_element(By.XPATH,'//input[@class="mce-textbox mce-abs-layout-item mce-last"]').send_keys("帅气的狗头")
#点击确定
driver.find_element(By.XPATH,'//span[text()="确定"]').click()
time.sleep(2)

#y轴滑动像素2500
driver.execute_script("window.scrollTo(1600,2500)")
#点击确定
driver.find_element(By.XPATH,'//button[@class="el-button el-button--primary"]//span[text()="确 定"]').click()
time.sleep(3)
#点击商品名称输入框
driver.find_element(By.XPATH,'//input[@placeholder="商品名称"]').send_keys("帅气的狗头")
#点击搜索按钮
ele='//div[@class="el-form-item__content"]//button[@class="el-button el-button--primary el-button--small"]'
driver.find_element(By.XPATH,ele).click()

time.sleep(5)
driver.quit()
