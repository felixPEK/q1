#!/usr/bin/env python
# -*- coding:utf-8 -*-

########创建set

s = set()

s = {11, 22, 33, 44}


########转换

l1 = [11, 22, 11 ,22]
l2 = (11, 223, 11, 22)
l3 = "123"

s = set(l2)
print(s)


########set提供的方法

########add 添加一个元素

########clear 清空

########differents，       A中存在，B不存在，返回一个新的值，变量接收

########differents_update，A中存在，B不存在，A更新


########discard 移除指定的元素，不存在不报错

########remove 移除指定的元素，不存在报错
se = {11, 22, 33, 44}
se.discard(44)
print(se)
se.remove(33)
print(se)


########intersection, 取交集
se = {11, 22, 33}
be = {22, 95, "随便"}


ret = se.intersection(be)
print(ret)

########intersection_update, 取交集
se = {11, 22, 33}
be = {22, 95, "随便"}


se.intersection_update(be)

print(se)


########isdisjoint() 有交集是false，没有交集是true
se = {11, 22, 33}
ret = se.isdisjoint(be)
print(ret)

########issubset() 是否参数的子set

se = {11, 22, 33, 44}
be = {11, 22}
ret = se.issubset(be)
print(ret)
ret = be.issubset(se)
print(ret)

########issuperset()，是否参数的父set

se = {11, 22, 33, 44}
be = {11, 22}
ret = se.issuperset(be)
print(ret)

########pop() 随机取值（set 无序而且不重复的元素集合

se = {11, 22, 44, 55}
ret = se.pop()
print(ret)
print(se)



########symetric_different() 对称交集

se = {11, 22, 33 ,44}
be = {11, 22, 77, 55}
r1 = se.difference(be)
r2 = be.difference(se)
print(r1)
print(r2)
ret = se.symmetric_difference(be)
print(ret)

########symetric_difference_udpate() 对成交集，并更新set


########union() 并集，并在一起

ret = se.union(be)
print(ret)



########udpate（）循环里面的东西，添加到set里面




########################
########################
########三元运算########


########简单if else
if 1 == 1:
    name = "alex"
    print(name)
else:
    name = "eric"
    print(name)
########写成三元运算

name = "alex" if 1 == 1 else  "eric"

print(name)






########str  一次性创建， 不能被修改，只要修改，其实是再创建

########list 链表，下一个元素的位置，上一个元素位置

########

a = 'alex'


########深浅拷贝########


########数字和字符串########

import copy
n1 = 123

print(id(n1))

n2 =copy.copy(n1) ########浅拷贝

print(id(n2))


n3 = copy.deepcopy(n1) ########深拷贝
print(id(n3))

########结论，只要是拷贝，不管深浅拷贝，字符串，数字的id永远是一样的########

########列表，字典，元素########

########有多少层都拷贝，除了最后一层


n1 = {"k1": "wu", "k2": 123, "k3":["alex", 678]}

n2 = copy.copy(n1)

print(id(n1), id(n2))
print(id(n1['k3']),id(n2['k3']))


n3 = copy.deepcopy(n1)

print(id(n1), id(n3))
print(n3)




########函数########

########面向过程编程########

########函数式编程########

########遇到def ，这一段代码不执行，全部放入内存

########定义函数

def xx():
    print("alex")

def oo():
    print("eric")
########执行函数

xx()
oo()


########1。def 2。函数名 3。() 参数 4。:  5。返回值
########如果不加返回值，默认返回值为none
def email():
    print("我要发邮件了")
    return "123"

ret = email()
print(ret)


def email1():
    if True:
        return True
    else:
        return False

ret1 = email1()
print(ret1)

if ret1 == True:
    print("Oh yeah!")
else:
    print("darn it!")


########函数的参数，普通参数########
########参数，形式参数，实际参数########
def kuaidi(p): #此处p为形式参数
    # 站起来
    # 转身
    # 。。。
    #print(p)
    if p == '15131255555':
        return True
    else:
        return False


ret = kuaidi("15131255555") # 此处手机号为实际参数

if ret:
    print("成功")

ret2 = kuaidi('15131255565')
print(ret2)

########邮件例子########
"""
def email(p):
    import smtplib
    from email.mime.text import MIMEText
    from email.utils import formataddr

    msg = MIMEText('this is a test mail send using python', 'plain', 'utf-8')
    msg['From'] = formataddr(['bonze2000', 'bonze2000@163.com'])
    msg['To'] = formataddr(['faye.89c51', '4621237@qq.com'])
    msg['Subject'] = "主题python"

    server = smtplib.SMTP("smtp.163.com", 25)
    server.login("bonze2000@163.com", "woyaomit2014")
    server.sendmail('bonze2000@163.com',[p,], msg.as_string())
    server.quit()

# email("heigao@icloud.com")


def email_v2(mailaddr,text, subject):
    import smtplib
    from email.mime.text import MIMEText
    from email.utils import formataddr
    ret = True
    try:
        msg = MIMEText(text, 'plain', 'utf-8')
        msg['From'] = formataddr(['bonze2000', 'bonze2000@163.com'])
        msg['To'] = formataddr(['faye.89c51', '4621237@qq.com'])
        msg['Subject'] = subject

        server = smtplib.SMTP("smtp.163.com", 25)
        server.login("bonze2000@163.com", "woyaomit2014")
        server.sendmail('bonze2000@163.com',[mailaddr,], msg.as_string())
        server.quit()
    except:
        ret = False

    return ret

rr = email_v2("4621237@qq.com", 'OK', "this is subject")

if rr:
    print("mail sent successfully")
else:
    print("mail didn't send")

rr1 = email_v2(mailaddr = '4621237@qq.com', text = 'OK', subject = "this is a subject")

# email("yanfei.bupt@gmail.com", 'Are you going to receive this or not?', "走国一定强")

# while True:
#     mailaddress = input('邮箱地址')
#     content = input('内容')
#     subject = input('主题')
#     email_v2(mailaddress, content, subject)
"""


########

# """
# 1. def 函数名（形式参数）：
#         函数体
#         return "123
#
# 2、执行参数
#     函数名（实参）
#
# 3、形参、实参（默认，按照顺序）
#
# 4、指定形参传入实参，可以不按照顺序
# 5、函数可以又默认参数
#
# """"


########默认参数要放在最前面，如果有的话

def drive(p,name):
    temp = name + "开车去东北"
    return temp

ret = drive(11,"老张")
print(ret)

ret = drive(11,"康师傅")
print(ret)

# ret3 = drive(11,)
# print(ret3)


def f1(a):
    print(a,type(a))

f1(123)
f1("123")
f1([123])


########动态参数, 加* 传多少个参数都能接收到，参数变成元组的元素

def f2(*a):
    # a = (123, )
    # a = (123, 456,)
    print(a, type(a))

f2(123,456,1234, [11,22,33],{"k1":"v1"})


def f3(**a): #动态参数二， 形式参数加**，传参数按照key=value，把传入的参数转换成字典，
    print(a, type(a))

f3(k1=123, k2=345)


def f4(p,*a, **aa):  #如果有默认参数，则第一个参数自动赋值给默认参数，默认参数在最前面,两个星的放在最后，一个星的放在中间
    print(a, type(a))
    print(aa, type(aa))

f4(11,22,33, k1=123, k2=456)



########通常动态参数一写成 *args ,动态参数二写成**kwargs

########为动态参数传入列表，元组，字典


def f5(*args):
    print(args,type(args))

li = [11,22,33,44]
f5(li) #不加*，把列表作为一个元素放入元组

f5(*li) #加*，把列表的每个元素作为元素放入元组

tu = (11,22,33,44)

f5(tu)


def f6(**kwargs):
    print(kwargs, type(kwargs))

dic = {"k1": 123}
f6(k1=dic)

f6(**dic)  #当形式参数有**，实际参数传参数也可以带俩星，

# *args *列表
# **kwargs **字典


########全局变量、局部变量########
########全局变量用大写，局部变量用小写########



P = "alex" #全局变量
def func1():
    a = 123 #局部变量
    P = "eric" #没有修改全局变量，此处是定义了一个局部变量p
    print(a)

def func2():
    a = 456
    global P #想要修改全局变量，需要声明全局变量
    P = "eric"
    print(P)
    print(a)



func1()
func2()

