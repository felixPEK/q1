#!/usr/bin/env python
# -*- coding:utf-8 -*-

def list_cut(arg):
    if len(arg) > 2:
        return arg[0:2]

    return arg

temp = [11,22]
print(list_cut(temp))