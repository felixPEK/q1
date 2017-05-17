#!/usr/bin/env python
# -*- coding:utf-8 -*-

def obj_len(arg):

    if isinstance(arg, str) or isinstance(arg, list) or isinstance(tuple):
        if len(arg) > 5:
            return True
        else:
            return False

    return None

# temp = [1234,'123edas1',"",1234543,1231234,1232]
temp = "12345"
ret = obj_len(temp)
print(ret)