#!/usr/bin/env python
# -*- coding:utf-8 -*-

asset_all = 0
cart_dict = {
    "电脑": {'price': 1999, 'num': 0},
    "鼠标": {'price': 10, 'num': 0},
    "游艇": {'price': 20, 'num': 0},
    "手机": {'price': 998, 'num': 0},
}

i1 = input('请输入总资产：')
asset_all = int(i1)

good = [
    {"name": "电脑", "price": 1999},
    {"name": "鼠标", "price": 10},
    {"name": "游艇", "price": 20},
    {"name": "手机", "price": 998},
]

for i in good:

    print(i['name'], i['price'])


i2 = input('请选择商品：或者按Y／y完成购买')

for j in good:
    if j['name'] == i2:
        cart_dict[i2]['num'] += 1
        # if cart_dict[]
        print(i2, cart_dict[i2])
        for i in cart_dict:
            print(cart_dict[i])