#!/usr/bin/env python
# -*- coding:utf-8 -*-


li = [11,22,33,44,55,66,77,88,99,90]

l1 = []
l2 = []

for i in li:
    if i <= 66:
        l1.append(i)
    else:
        l2.append(i)
temp = {"k1": l1, "k2":l2}

print(temp)

dic = {
    "k1": [],
    "k2": []
}

for i in li:
    if i <= 66:
        dic['k1'].append(i)
    else:
        dic['k2'].append(i)