from selenium.webdriver.common.by import By
#请输入商品名称框
search_box = (By.XPATH,'//div[@class="search-input-box" ]//input[@placeholder="请输入商品名称"]')
#点击搜索
search_btn = (By.XPATH,'//div[@class="search-msg"]//input[@class="search-btn"and @value="搜索"]')
#点击要下单的商品
select_product = [By.XPATH,'//div[text()="{}"]']
#点击立即购买
buy_now = (By.XPATH,'//a[@class="buy-now"]')

#点击提交订单按钮
submit_order = (By.XPATH,'//a[text()="提交订单"]')
#点击微信支付
wechat_payment = (By.XPATH,'//span[text()="微信支付"]')
#点击立即支付按钮
pay_immediately = (By.XPATH,'//a[text()="立即付款"]')

#点击我的订单
my_order =(By.XPATH,'//span[contains(text(),"我的订单")]')
#点击待支付
wait_payment = (By.XPATH,'//span[contains(text(),"待支付")]')

#获取订单号
get_order_num = (By.XPATH,'//span[@class="num"]')

#点击待发货
to_be_shipped = (By.XPATH,'//span[contains(text(),"待发货")]')

confirm_order_no = [By.XPATH,'//span[text()="{}"]']