# -*- coding: utf-8 -*- 
# Created By CHT  
"""
编码     : encoding="utf-8"
Time    : 2023/7/19 17:31
File    : random模块.py
Project : PycharmCode
"""
import random

print(random.random())  # 返回一个0-1之间的浮点数
print(random.randrange(1, 10))  # 返回1-10之间的一个整数  不包括10
print(random.randint(1, 10))  # 返回1-10之间的一个整数  包括10
print(random.choice("123456454/*-"))  # 随机选取一个值
print(random.sample("123456454/*-", 2))  # 随机选取制定个数的值
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
random.shuffle(a)  # 打乱顺序
print(a)  # 打乱顺序
