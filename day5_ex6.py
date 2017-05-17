#!/usr/bin/env python
# -*- coding:utf-8 -*-

def odd_sub_listuple(arg):
    for index,item in enumerate(arg):
        new_list = []
        for index, item in enumerate(arg):
            if index % 2 == 1:
                new_list.append(item)

    return new_list


li = [11,22,33,44,55]
tu = (11,22,33,44,55)
ret = odd_sub_listuple(li)
print(ret)

