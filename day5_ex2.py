#!/usr/bin/env python
# -*- coding:utf-8 -*-

#
# def func1(a1, a2):
#     result = a1 + a2
#     return result
#
# r = func1(13,2)
# print(r)
#
#
# def func2(a):
#     if a.istitle():
#         return True
#     else:
#         return False
#
# r = func2("Hello")
# print(r)
#
#
# def func3(s):
#     ret = 0
#     for i in s:
#         if i == "r":
#             ret += 1
#     return ret
#
#
# r = func3("asldjfwoevnqoeirjorqwje;vnasdklvnr")
# print(r)
#
# ret = " ".isspace()
# print(ret)


a = "123knlsasdfasvasdv/.,; w,e; rqd     "

def func(arg):
    num_alpha = 0
    num_num = 0
    num_space = 0
    num_other = 0
    for i in arg:
        if i.isalpha() == True:
            num_alpha += 1
        elif i.isalnum() == True:
            num_num += 1
        elif i.isspace() == True:
            num_space += 1
        else:
            num_other += 1


    return num_alpha, num_num, num_space, num_other

result = func(a)
print(result)