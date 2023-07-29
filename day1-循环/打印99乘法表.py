# -*- coding: utf-8 -*- 
# Created By CHT  
"""
编码     : encoding="utf-8"
Time    : 2023/7/29 15:12
File    : 打印99乘法表.py
Project : PycharmCode
"""

for i in range(1, 10):
    for j in range(1, 10):
        # for j in range(1, i+1):
        if j <= i:  # 控制一行打印的个数
            print(f"{i}*{j}={i * j}  ", end="")  # end打印结束符
    print()  # 打印空值
