#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 上期回顾
#
# 三元运算
#
# name = "name1" if 条件 esle "name2"
#
# 深浅拷贝
# 1、数字、字符串
#     深浅，都一样
# 2、其他
#     前拷贝：只拷贝第一层
#     深拷贝：不拷贝最后一层
#
# set集合
#     无序、不重复
#     交集、并集、差集
#
# 函数
#     1、def
#     2、函数名、参数
#     3、函数功能
#     4、执行函数
#     5、参数
#         普通参数
#         指定参数
#         默认参数，写在最后 def f(a1,a2, a3, a4 = '123')
#         动态
#             *args => 元祖 *
#             **kwargs => 字典 **
#
# def f1(123):
#     功能
#
# 全局变量
#     global



# lambda 表达式

def f1(a):
    return 123


# if else
# 三元运算

# def xxx
# lambda

f2 = lambda: 123


# f1与f2实现功能一样

def f3(a1, a2):
    return a1 + a2


f4 = lambda b1, b2: b1 + b2

a = f3(3, 4)
print(a)
b = f4(3, 4)
print(b)

# f3与f4实现功能一样


################################
#####python 内置函数#############
################################

# abs() 取绝对值

i = abs(-123)
print(i)

# all() 循环参数，如果每个元素都是真值，则返回值为真

r = all([True, True, False])
print(r)

# 每个元素都为真True
# 假: 0,None,空字符串，空列表，空元祖，空字典
# print(bool(0))
# print(bool(-1))
# print(bool(None))
# print(bool("1234"))
# print(bool([]))

a1 = all(["123", " ", [11, ], ""])
print(a1)

# any() 循环参数，只要有一个为真，则返回值为真

i = any(["123", " ", [11, ], ""])
print(i)


# ascii() 对象的类中找 __repr__, 获取返回值
class Foo:
    def __repr__(self):
        return "hello"


obj = Foo()

r = ascii(obj)
print(r)
# ascii(对象)



######bin()######## 二进制
######hex()######## 十六进制
######oct()######## 十进制
######int()######## 十进制

r = bin(11)
print(r)
r = hex(11)
print(r)
r = oct(11)
print(r)
r = int(0b1011)
print(r)

i = int('0xe', base=16)
print(i)

########bool,判断真假，把一个对象转换成bool值，None，""[],{}转换成false


########bytes 字节

########bytearray 字节列表，

#######字节、字符串

# bytes("xxxx", encoding='utf8')


########chrd() 接受一个数字,找到代指的ascii字符
########ord() 给一个字符，找到代指该字符的ascii数值


# 一个字节，8位，2**8， 256， A B C....

i = chr(69)
print(i)

t = ord('B')
print(t)

############生成随机验证码###########

# 生成一个随机数
# 数字转换成字母：chr(数字)

import random

i = random.randrange(65, 91)
print(i)

c = chr(i)
print(c)

temp = ""
for i in range(6):
    num = random.randrange(0, 4)
    if num == 3 or num == 1:
        rad2 = random.randrange(0, 10)
        temp += str(rad2)
    else:
        rad1 = random.randrange(65, 91)
        c1 = chr(rad1)
        temp += c1

print(temp)


########callable()表示一个对象是否可以被执行######

def f1():
    return 123


f2 = 123
r = callable(f1)
print(r)

r2 = callable(f2)
print(r2)

#############classmethod以后讲


#############compile() 将字符串接收，编译函数

#############complex() 复数用不着


#############delattr() 反射 （设计模式，工厂模式）
#############hasattr()
#############getattr()
#############setattr()

#############dict() 字典

#############dir() 列出基本类型所有内置功能

li = []
# c1 = dir(li)
print(c1)

#############help() 列出基本类型内置功能，并简单解释



#############divmod()

a = 10 / 3
print(a)
r = divmod(10, 3)
print(r)

############enumerte()



############eval() 执行一个字符串形式的表达式,有返回值
############exec() 将字符串作为代码执行，没有返回值，只用来执行python代码

a = 1 + 3
print(a)

a = "1 + 3"
print(a)

ret = eval("1 + 3")
print(ret)

ret2 = eval("a + 70", {"a": 99})  # 可以计算带参数的表达式，需要加一个字典用于赋值
print(ret2)


# exec("for i in range(10): print(i)")


#########filter()过滤，符合条件的获取，不符合的筛除##########

####syntax：filter(函数，可以迭代的对象)

#####循环可迭代的对象，获取每一个参数，函数（参数）

def f1(x):
    if x > 22:
        return  True

ret = filter(f1, [11,22,34,55])
for i in ret:
    print(i)

#####eg2
def f1(x):
    if x > 22:
       return True


ret = filter(lambda  x: x > 22, [11,22,33,44])

for i in ret:
    print(i)



#########map(函数，可迭代的对象)
#########

[1,2,3,4,5]

def f2(x):
    return x + 100
ret = map(f2,[1,2,3,4,5])

print(ret)
for i in ret:
    print(i)


ret2 = map(lambda x: x + 100, [1,2,3,4,5])
print(ret2)
for i in ret2:
    print(i)


########float不说################
########format不说将来说########


########forzenset()冻结的set，不说了########


########globals()表示获取当前代码里所有的全局变量########

########locals()获取所有的局部变量########


def f1():
    name = 123
    print(locals())
#    print(globals())

f1()




########hash()算一个东西的hash值，用于字典的key的保存,对key做一个优化########

dic = {
    "asldfjwqlekfjlkvjasd;jvqw;eklfjla;sdfj" : 1,
}

i = hash('asldfjwqlekfjlkvjasd;jvqw;eklfjla;sdfj')
print(i)



########help()########

########hex()########

########id()########

########list()########

########isinstance() 判断某个对象是否某个类创建的########

li = [11, 22]
r = isinstance(li, list)
print(r)

########range() 不创建，只有当循环的时候才创建########

nums = range(10)

for i in nums:
    print(i)


########iter()迭代器 后面说，next()后面说

obj = iter([11,22, 33,44])


########max()最大值, min()最小值########

li = [11, 122, 213, 112, 3322]
r = max(li)
print(r)

zx = min(li)
print(zx)


########object()后面说 ###############

########open()文件操作########


########pow() 求指数的########

i = pow(3, 10)
print(i)


########property()后面说，属性########

########repr() ascii() 返回########

########reversed() 反转

########round()四舍五入########
r = round(3.3)
r1 = round(3.6)
print(r,r1)

########slice()切片########

########sorted()########

########staticmethod()########



########sum() 求和########

r = sum([11,22,33,44])
print(r)

########vars()当前对象里有多少个变量########

########zip(), 将多个组组成一个新的组，每个元素有每个对象的元素构成########

li = [11,22,33,44]
li2 = ["a",'BB', "C", "E"]
li3 = [11,22,3,5]
r = zip(li, li2, li3)
print(r)
for i in r:
    print(i)



########__import__() 导入用的，可以给导入的模块取个别名########

# import getpass
# import ramdom


########sorted排序, 数字按大小，字符串按字符按位从小到大比较，先数字，再符号，再后字母，然后中文########

li = [11, 211, 22, 3, 4]
new_li = sorted(li)
print(new_li)

char = ['赵', '1', '223d', '2234', '22345','sdfas', "_",'123']
new_char = sorted(char)
print(new_char)

########open()文件操作########
# 一、打开文件
# 二、操作文件
# 三、关闭文件

#open(文件名，模式，编码)

# f = open('ha.log', 'r')
# date = f.read()
# f.close()
# print(date)
#
# print(type(date))
# b = bytes(date, encoding='utf8')
########基本打开方式，r w x a########

# r 只读模式
f = open("ha.log", "r")
#f.write("asdfwefsdf") #只读无法写
f.close()


# w 只写模式, 不可读，不存在则创建，存在则清空内容

f = open('ha1.log', 'w')
f.write("1d1d12d")
f.close()

# 清空

f = open('ha1.log', 'w')
f.close()

# x 只写，不可读，不存在则创建，存在则报错

# f = open('ha2.log','x')
# f.write('454')
# f.close()


# a, 追加模式，不可读，不存在则创建，存在则只追加内容

# f = open("ha2.log", 'a')
# f.write("555")
# f.close()




########

# 1. 只读，rb, 以字节方式打开，不需要加encoding

f = open("ha.log", 'rb')#, encoding='utf-8')
data = f.read()
f.close()
print(type(data))

# 2. 只写，wb，以二进制方式取写
f = open('ha.log', 'wb')
str_data = "中国人"
bytes_data = bytes(str_data, encoding ='utf8')
f.write(bytes(bytes_data))
f.close()

# 3. 只写 xb
# 4。追加 ab

########普通打开方式
########python内部将01001010 转换成字符串，通过字符串操作
######## 01010010100111 python解释器 程序员


########二进制打开方式（字节bytes）


########既想读又想写用+

########r+, 可读写
########读写只指到末尾
########写的时候指针指到最后

f = open('ha.log', 'r+', encoding='utf-8')
print(f.tell())
data = f.read(2)
print(f.tell())
print(type(data),data)

print(f.tell())
f.write('泰国人')
print(f.tell())
data = f.read(1)
print(f.tell())
print(data)
f.close()

########w+，写读, 先清空，在写之后就可以读了
########先清空，之后写的才能读，写，指针到最后


f = open("ha3.log", "w+", encoding='utf8')
f.write("何莉莉")
f.seek(0)
data3 = f.read()
f.close()
print(data3)


########x+，写读，和w+，如果存在这个文件则报错
########写时，追加，放在最后
# f = open("ha3.log", "x+", encoding='utf8')
# f.write("何莉莉")
# f.seek(0)
# data3 = f.read()
# f.close()
# print(data3)


########a+，写读，打开的同时，已经将指针移到最后

f = open("ha4.log", 'a+', encoding="utf8")
data = f.read()
f.seek(0)
print(data)
f.close()
print(data)


#f.tell() 获取指针的位置
#f.seek() 调整指针的位置


########共有的特性，seek，读取


########r+b
########w+b
########x+b
########a+b
########bytes


########文件操作########


########flush()将内存里的内容刷到硬盘########
f1 = open("ha.log", "r+")
f1.write("所宁紧缩的眉头")
f1.flush()

########read()

f1.read()
#读取所有的内容
#read(1) 字符
#read(1) 字节


########readline()仅读取一行数据########

########truncate()截取########

f1 = open("ha.log", "r+", encoding='utf8')
print(f1.tell())
print(f1.seek(6))

f1.truncate()
f1.close()

########文件常用基本操作########
########close()关闭文件########
########fileno() io操作，检测文本／socket有没有变化（不重要）########
########flush()刷新文件，刷到硬盘########
########isatty()（不重要）########
########read()读取，可以加参数########
########readline()读取一行（从第一行开始），指针到该行末尾########
########seek()########
########tell()########
########trunkcate()截取########
########write() 写########

# f1 = open("ha.log", "r+",encoding = "utf-8")
# f1.write("所宁静锁的眉头")


f = open("ha.log", 'r', encoding='utf8')
f.read()


########python2.7 同时打开两个文件########
with open('ha1.log', 'r') as obj1, open('ha3.log', 'r') as obj2:
    pass


# with open('源文件', 'r') as obj1,open("新文件", "w") as obj2:
#     pass
