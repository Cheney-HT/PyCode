# -*- coding: utf-8 -*-
"""
 -*- coding: utf-8 -*-
Time    : 2023/7/18 9:34
AuThor  : Administrator
File    : 文件遍历.py
Project : PycharmCode
"""
f=open("联系方式.txt", encoding="utf-8")
for line in f:
    line=line.split() #切片
    height=int(line[3])
    weight=int(line[4])
    if height>=170 and weight<=50:
        print(line)