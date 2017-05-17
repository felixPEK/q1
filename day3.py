#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 一 运算符
#   in
#   "hello" in "asdfasdfwefasdfds"
#   "li" in ['li', 'ok']

# 二 基本的数据类型
#   int

# 三 其他
#   int
#       a. 两种创建方式
#       n1 = 123 # 根据int类，创建了一个对象
#       n2 = int(123) # 根据int类，创建了一个对象
#       特有的功能在：
#       int类
#           功能1
#           功能2
#           功能3
#           __init__ 翻译过来叫初始化，类名后加一个括号，意即自动执行__init__功能
#       b. int内部优化
#             n1 = 123
#             n2 = n1
#
#             n1 = 123
#             n2 = 123
#             ===========两份内存=========
#             -5 ～ 257
#                 n1 = 123
#                 n2 = n1
#             else:
#                 n1 = 123
#                 n2 = 123
#               可以通过id来查内存地址
#       c. 长度限制
#           用int，超出了范围
#           32bit    -2**31 ～ 2**31-1
#           64bit    -2**63 ～ 2**63-1
#           long
#           byte数据类型（非基本数据类型）
#   str
#       str() 去str类里找到__init__功能
#           str类 __init__
#         s1 = "alex"
#         s1 = str('alex')
#             无参数，创建空字符串
#             一个参数，创建普通字符串
#             两个参数，str(字节, 编码) ====》

#          b. 特有功能，常用函数
#             s1 = 'alex'
#             s1.strip() 两端去除空格
#             s1.startswith() 以什么开头
#             s1.find() 从字符串中找子序列，可以是一个字符也可以是多个字符
#             s1.replace() 将字符串中某个子序列替换
#             s1.upper() 将字符串变大写
#             s1.isalpha() 判断是否字母
#             s1.isalnum() 判断是否字母，数字
#         c. 公共功能
#             索引 str类型变量[]里有一个参数,只能取一个元素
#             切片 str类型变量[]里有两个参数,可以取多个元素
#             len：
#             for循环
#         d. bytes和字符串str转换
#              1 创建字符串
#              2 转换成字符串，（字节，编码）
#              1 创建字节
#              2 转换成字节， （字符串，要编码成什么类型的字节）


#
s1 = "alex123"

print(s1[1:3])



#   list
#       list() 去list类里找到__init__功能
#           list类 __init__


a1 = 123
a = int(123)
print(a1)
# 两种写法默认相等

a2 = int('0b100',2)
print(a2)

# a => int => __init__(123) 类里的功能通称为方法

# int.__init__()
# print(a.bit_length())

# __xxx__ 带下划线的函数python内部调用的，面向对象的时候才去管它。


n1 = 123
n2 = 123

# 正常是占用两个内存地址，但python内部为了优化，-5～257范围内的数字，python认为是经常用的
# 所以赋值多个参数为同一值时，仍然用同一块内存


n = 2**128
print(n)


s1 = "alex"
s1 = str('alex')
s1 = str()


# UTF-8 编码，一个汗渍，三个字节
# 不管中文还是英文，for循环，都是一个字符一个字符显示（py3）
# py2.7 str为中文则是乱码，按照字节，循环了六次（一个汉字三个字节,一个字节8位）
name = "李璐"
for i in name:
    print(i)
    print(bytes(i,encoding='utf-8'))


# 字符串类型
# str类型有两个参数：（字节，编码）

a = "李璐"
# 将字符串转换成字节
b1 = bytes(a,encoding='utf-8')
print(b1)

b2 = bytes(a,encoding='gbk')
print(b2)



# 将字节传唤成字符串

newa1 = str(b1, encoding='utf-8')
print(newa1)

newa2 = str(b2, encoding='gbk')
print(newa2)



####################

x = str()

# 1 创建字符串
# 2 转换成字符串，（字节，编码）

m = bytes()
# 1 创建字节
# 2 转换成字节， （字符串，要编码成什么类型的字节）





############################

######### 列表 list #########

# 列表，元素的集合


# str - > 创建字符串，或者将其他的转换成字符串

# list -> 创建列表，将其他元素转换成列表
#   1.创建
li = [11,22,33,44]

li = list()

li = list([11,22,33,44])


#   2.转换

#__init__(self, seq=())
# iterable,可迭代的

s1 = "李璐"

#for循环 字符 = > 可迭代
li = list(s1)  # for循环，将循环的每一个元素，当作列表的元素

# ['李'， '璐']
print(li)



#
#元祖也可以进行for循环，意思即是元祖也可以转换，成列表

t2 = ("alex", 'laonanhai', 'seven')
l2 = list(t2)
print(l2)

####
#字典也可以进行for 循环，字典也可以进行转换，成列表

dic1 = {'k1': "alex", "k2": 'seven'}
l3 = list(dic1)
print(l3)


# b. 列表常用功能

#li = list()


# append 追加
#li.append() # 在原来的后面追加，是update原来的list

s = "alex "
s.strip()
print(s) # 原来的不改变，生成新的



# clear 清除

# li.clear

# extend 扩展，拿另一个可迭代的对象，扩充到自己的内部（字符串，列表，元祖，字典都可以迭代）

# li.extend

s = "李璐"
li = [11, 22, 3]
#li.extend(s)
print(li)


# reverse 反转，自己内部元素的反转
# li.reverse



#insert 想指定位置插入指定元素
# li.insert()


# c. 列表的公共功能

li = ["alex", "eric", "seven", 123]

#索引, 取出来的是一个元素，这个元素什么类型，索引结果是什么类型

print(li[2])

#切片， 将列表切片成含有元列表子集的新列表

print(li[2:3])

# d. 列表的元素可以是字符串，数字，列表，元祖，字典，多层嵌套
# 依然可以通过索引，取得多层嵌套下的元素
li = ["alex", "eric", "seven", 123]
li = ["alex", 123, {"k1":"v1", "k2": {"vv":123, "li": 456}}]

print(li[2]['k2']['vv'])




##########################
#######元祖 tuple #########
###########################

# t = (11,22,33)
# tuple(11,22,33)
# tuple('1123124')

# a. 创建和转换
#     t = (11,22,33)
#     t = tuple((11,22,33))
#     t = tuple([]) #字符串，列表，字典


# b.特有方法
#     count
#     index

# c. 嵌套（元素不可修改）
#     t = (11,22, 33)
#     t = (11,22,["alex", {"k1":"v1"}])
#     t[2][1]["k1"] #多层嵌套的索引

# d. 元祖的特性，不可被修改，元祖的元素不可修改, 元素的元素可以修改
#       元祖，儿子不能变，孙子可能会变

# 举例在元祖的列表元素下的字典元素添加键值对，有两种方法
t = (11,22,["alex", {"k1":"v1"}])
t[2].append('felix')
print(t)
t[2][1].update({'k2':123})
print(t)
t[2][1]["k3"] =345
print(t)



#整理：
# 一般字符串，执行一个功能，生成一个新内容，原来内容不变
# list,tuple.dict，执行一个功能，自身进行变化





##############################
#######字典 dict #############

# 1. 创建
a = {"k1":123}
a['k2'] = 345
print(a)
asd

li = [11,22,33,44]
new_dict = dict(enumerate(li,10))
print(new_dict)

# 2. 字典的内部功能
#     keys()
#     values()
#     items()
#     pop
#     clear
#     get
#     fromkeys

# get
# 方法，无@staticmethod，对象.方法

# fromkeys

# 方法，@staticmethed，类.方法

dic = {'k1':123, "k2": 456, "k4": 111}

# k1,k2 默认值123
n = dic.fromkeys(['k1','k2','k3'], "alex")
print(n)

n2 = {'k1': "alex", "k2": 'alex', "k3": "alex"}
print(n2)

