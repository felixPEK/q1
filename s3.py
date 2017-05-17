#!/usr/bin/env python
# -*- coding:utf-8 -*-

f = open('ha.log', 'r+', encoding='utf-8')
print(f.tell())
data = f.read(2)
print(f.tell())
print(type(data),data)

print(f.tell())
f.write('泰国人')
print(f.tell())
data = f.read()
print(f.tell())
print(data)
f.close()