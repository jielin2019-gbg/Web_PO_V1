"""
======================
Author: 柠檬班-小简
Time: 2022/12/26 21:21
Project: Web_PO_V1
Company: 湖南零檬信息技术有限公司
======================
"""
from faker import Faker
faker = Faker("zh-cn")


new_prod = {
    "category":("服饰鞋包", "鞋类", "皮鞋"),
    "group": "商城热卖",
    "sku":["100", "88", "99", faker.pystr(10,15), "5", "2"],
    "delivery": "包邮",
    "cn_name": f"py54自动化应用{faker.pystr(5,8)}",
    "cn_sale": "好用，实在",
    "cn_info": "py54很厉害，大家多多少少都有点儿阳了,,,"
}