#!/usr/bin/env python
# -*- coding:utf-8 -*-

def fbnq():
    i = 0
    sum_f = 0
    while i < 10:
        i += 1
        sum_f = sum_f + i
        print(i)
    return sum_f

t = fbnq()
print(t)