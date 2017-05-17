#!/usr/bin/env python
# -*- coding:utf-8 -*-

li = [11,22,33,44]
enu = enumerate(li)
new_list = []
for index, item in enumerate(li):
    if index % 2 == 0:
        new_list.append(item)

print(new_list)
