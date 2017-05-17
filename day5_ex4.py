#!/usr/bin/env python
# -*- coding:utf-8 -*-

def has_blank(arg):

    # if isinstance(arg, str) or isinstance(arg, list) or isinstance(tuple):
        for i in arg:
            if " " in i:
                ret = True
                break
        return ret

temp =  'asdfsdf '

ret1 = has_blank(temp)
print(ret1)

