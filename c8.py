#!/usr/bin/env python
# -*- coding:utf-8 -*-

#1. 模版

###file => settings => Editor => file and code template => python script => 右上方
#!/usr/bin/env python
# -*- coding:utf-8 -*-

#2. 文件大小

###file => settings => editor => color and font => font => save as .. => 18

#3. 运行
#   a. 点击要运行的文件，右键run
#   b.
#       view => toolbar
#       选中要执行的文件
#       点击 运行
#   c. 在当前文件空白处，右键，run、


#4. 切换py版本
# file => settings => project interpreter -> 选择版本

# from __future__ import division
# val = 9 / 2
#
# print val

# == 等于 - 比较对象是否相等
# != 不等于 - 比较两个对象是否不相等
# <> 不等于
# > 大于 - 返回x是否大于y
# < 小于 - 返回x是否小于y。比较运算符返回1表示真，返回0表示假。等价于True 和alse
#
# >= 大于等于 - 返回x是否大于等于y
#
# <= 小于等于 - 返回x是否小于y

# =   简单的赋值运算符
# +=  加法赋值运算符
# -=  减法赋值运算符
# *=  乘法赋值运算符
# /=  除法赋值运算符
# %=  取模赋值运算符
# **= 幂赋值运算符
# //= 取整除赋值运算符


# start = 1
# #start = start + 1
# start += 1
# print start


# 逻辑运算符
# and
# or
# not


# 成员运算符
# in
# not in

# s = "Alex SB"
# ret = "SB" in s
# print ret

# li = ['alex', 'eric', 'rain']
# ret = 'alex' in li
# print ret

#数据类型，相应的数据类型有对应的可操作函数
#"超能力"，城堡， 每个人都把所有的能力都存在包里自己背着，会占用很大内存，负担很大
# 而所有的能力都存在"城堡"／模版里，那么将会减少内存占用。
# 类和对象
temp = "hey"

print(temp)

temp_new = temp.upper()
print(temp_new)

#upper这个功能存在类里面

# 如何找相应的超能力, 获得数据类型，按住ctrl，点选类型，跳转到该类型的"超能力"／功能

# 查看对象的类，或对象所具备的功能,
# 1 前一行提到，按住ctrl，鼠标选中类型
# 2 dir(数据类型)
# 3 help, type
# 4 type


chengbao = type(temp)
print(chengbao)

str

print(temp.upper())
print(temp.lower())




temp = "alex"
t = type(temp)
print(t)
print(dir(t))


temp = "alex"
#help(type(temp))
#   身份运算，先不说


# 基本数据类型
#     数字  int
#     字符串 str
#     布尔值 bool
#     列表  list
#     元祖  tuple
#     字典  dict
#     所有字符串或者数字、字典 所具备的方法存在相对应的 类里

# 基本数据类型的常用功能

# int 数字

# __add__ 加法
print(dir(int))

n1 = 123
n2 = 456
print(n1 + n2)

print(n1.__add__(n2))


#bit_length
#数字的二进制最少可以占几位

n1 = 31
print(n1.bit_length())


###str
# capitalize 首字母变大写

a1 = "alex"
ret = a1.capitalize()

print(ret)

# center 内容居中

a1 = "alex"
ret = a1.center(20,'*')
print(ret)

# count 子序列的个数, "子序列的内容"，从第几个字符开始(从0开始），到第几个结束,空格也算字符

a1 = "alex is alph"
ret = a1.count('al',0,10)
print(ret)


# endswith 判断是否以某个字符结尾的,"判断的字符"，从第几个字符开始（大于等于0，也就是从0开始），小于几的，也就是到第几个结束，空格也算字符

a1 = "alexa"
ret = a1.endswith('a',0,1)

print(ret)


# expandtabs 将tab换成空格，一个tab换成8个空格, tabsize是将tab替换成多少个空格

content = "hello\tworld\t999"
print(content.expandtabs(20))


# find 寻找子序列的位置，如果没找到，返回-1，找到第一个返回位置

s = "alex hello"
print(s.find('ex'))

# format 字符串的格式化

s = "hello {0}, age {1}"
print(s)

# {0} {1}为占位符

new1 = s.format('alex',19)
print(new1)


# index获取子序列的位置，如果没有找到报错
# 不如find好用


# 函数根据括号里有没有内容分为没有传参数，可以传参数，该不该传参数，可以看源码

# isalnum 判断是否字母和数字

a = "alex99"
print(a.isalnum())

# isspace 判断是不是空格

# istitle 判断是不是标题，（首字母是大写）

# isupper 判断是不是全部大写

# join 连接 join(self,iterable),用字符将列表连接起来

li = ["alex", 'eric']
s = ".".join(li)
print(s)



# lstrip 去掉左边空格
s = "   alex    "
news = s.lstrip()
print(news)

news2 = s.rstrip() # 去掉右边空格
print(news2)


# partition 将字符串以子集为坐标，分割字符串，并生成一个元祖类型
s = "alex SB alex"

ret = s.partition('SB')
print(ret)   #('alex ', 'SB', ' alex') 元祖

# replace 替换字符串,语法，旧的，新的，替换几个
s = "alex SB alex"
ret = s.replace("alex","eric",2)
print(ret)


# rfind 从右向左找


# rindex 从右向左找


# rjust 向右找齐，把字符传放再最右，可以传参数，1，该行一共多少个字符（宽度），2，右边以什么单个字符填充，默认空格

a1 = "alex ssewod "
ret = a1.rjust(30)
print(ret)


# rsplit 做分割,以所写字符做分割，得到一个列表，从右向左

s = "alexalex"
ret = s.split('e')
print(ret)

# rstrip 把右边空白移出

# split 从左向右做分割

# splitline根据换行符做分割

# startswith 判断是否以某个字符开始

# strip 移出两边的空白

# swapcase 大写变小写，小写变大写
s = "aLeX"
print(s.swapcase())


# title 将字符串变成标题,首字母大写

s = "the school"
ret = s.title()
print(ret)


# upper字符串变大写

# zfill 原字符串右对齐，填充0，不太用的到


# 索引和切片

# alex是一个字符串，a，l，e，x都是一个字符
s = "alex"

print(s[0:4])
# 大于等于前一个值，小于后一个值

# 索引

print(s[0])
print(s[1])
print(s[2])
print(s[3])

# 长度
ret = len(s)

# 循环

# while循环
start = 0
while start < len(s):
    temp = s[start]
    print(temp)
    start += 1

# for循环，循环序列里的每一个元素

# break continue再for循环依然可以运用

for item in s:
    if item == "l":
        continue
    print(item)

for item in s:
    if item == "l":
        break
    print(item)



#####   列表  ######
####字符串作为元素，形成一个集合
name = "alex"
age = "18"
name_list = ["alex", "eric", "elle", "aubrey", "tony"]

print(name_list)

# 索引
print(name_list[0])

# 切片
print(name_list[0:2])

print(name_list[0:len(name_list)])


# for 循环

for i in name_list:
    print(i)


# 列表所提供的功能

# append追加功能,追加并更新原列表

name_list.append('Seven')
print(name_list)



# count数某一个元素的数量
print(name_list.count('Seven'))


# iterable可迭代的，
temp = [111,22,33,44]


# extend, 批量的扩展更新原列表，
name_list.extend(temp)
print(name_list)

# index 查询某个元素的索引值
print(name_list.index('eric'))


# insert 再某个索引位置插入一个值

name_list.insert(1,'SB')

print(name_list)

# pop 移除最后一个值，同时还可以将最后一个值赋值给变量

a1 = name_list.pop()
print(a1)
print(name_list)


# remove 移除某个元素,只移除左边数找到的第一个

name_list.remove('Seven')
print(name_list)

# reverse 反转
name_list.reverse()
print(name_list)

# sort 简单的排序

# name_list.sort()
# print(name_list)

# 如何删除指定索引位置的元素,使用 del

print(name_list)
del name_list[1]

print(name_list)
del name_list[0:2]
print(name_list)



##############################
######  元祖 tuple    ########
### 元祖和列表几乎一样，差距在于列表中的元素可以修改，元祖不可以修改

name_tuple = ('alex', 'eric')

# 索引
print(name_tuple)

# len 长度
print(name_tuple[len(name_tuple)-1])

# 切片
print(name_tuple[0:1])

# for循环

for i in name_tuple:
    print(i)

# 删除'tuple' object doesn't support item deletion

# del name_tuple[0]


# tuple提供的功能

# count 计算元素出现的个数

print(name_tuple.count('alex'))


# index 获取指定元素的索引位置

print(name_tuple.index('alex'))




###########################
######  dict 字典 ##########
### 定义一个字典#######
# 字典的每一个元素，键值对,一个key，一个value
# 列表的索引是系统自动添加，对应字典的key是自己定义，而非默认系统添加


user_info = {
    "name": "alex",
    "age": 74,
    "gender": 'M'
}

# 索引， 不再是数字，而是key
print(user_info['age'])

# user_info = {
#     0: "alex",
#     1: 74,
#     2: "M"
# }

# 0 name         "alex"
# 1 age          74
# 2 gender       "M"

# 没有切片

# 循环,默认值输出key

for i in user_info:
    print(i)


# key, values, items
print(user_info.keys())
print(user_info.values())
print(user_info.items())

for i in user_info.keys():
    print(i)

for i in user_info.values():
    print(i)

for k,v in user_info.items():
    print(k)
    print(v)
    print(k, v)


# clear 清除所有内容
# user_info.clear()
# print(user_info)

# get 根据key获取值，如果key不存在，那么可以指定一个默认值（用的最多）

val = user_info.get('age')
print(val)


# 通过索引也可以取值，但是通过索引取值，如果key不存在，索引会报错，而get不会
val = user_info.get('age111', 73)
print(val)


# copy 稍后再说


# has_key 检查字典中指定key是否存在, py3里没有了，但是可以用下面的方法来判断
# print(user_info.has_key('age'))
ret = 'age' in user_info.keys()
print(ret)


# pop 移除指定的item


# popitem只能从尾部移除




# update 更新字典，将另一个字典加入其中
test = {
    'a1': 123,
    "a2": 456
}
user_info.update(test)
print(user_info)


# 字典删除

del user_info['a1']
print(user_info)






# for循环 ，上面已经教过

# enumerate, 自动生成一列，默认0开始自增1
# -*- coding:UTF-8 -*-
li = ["电脑", "鼠标垫", "U盘", "游艇"]

# for key, item in enumerate(li):
#     print(item)
#
# inp = input("请输入商品:")
# # 字符串转换成数字，用int
# inp_num = int(inp)
# print(li[inp_num-1])
#
#
# li = ["电脑", "鼠标垫", "U盘", "游艇"]
# inp = input("请输入商品:")
#
# ret = li.index(inp)
print(ret)


# range和xrange
# py2.7
# range用来获取指定范围内的数 range(0,10000000)

# xrange， 用来获取指定范围内的数，xrange(0,10000000)

# print(range(1,10))
# for i in range(1,1000):
#     print(i)

for i in range(10,0, -1):
    print(i)

li = ['alex', 'eric']

leng = len(li)

for i in range(0,leng):
    print(i,li[i])