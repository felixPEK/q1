#!/usr/bin/env python
# -*- coding:utf-8 -*-


def f7(arg):
    ret = {}
    for keys, values in arg.items():
        if len(values) > 2:
            ret[keys] = values[0:2]
        else:
            ret[keys] = values

    return ret






dic = {"k1": "v1v1", "k2":[11,22,33,44], "k3":'v3'}
r = f7(dic)
print(r)

