# -*- coding: utf-8 -*- 
# Created By CHT  
"""
编码     : encoding="utf-8"
Time    : 2023/7/29 15:37
File    : 打印素数.py
Project : PycharmCode
"""
# 素数：大于1的整数，除了1和其本身，不能被其他数整除 例：3,5,7
# 求1-100之间的素数
su = []  # 定义一个列表存放素数
for i in range(2, 100):
    is_su = True  # 假设i是素数
    for j in range(2, i):
        if i % j == 0:  # 能整除，代表不是素数
            is_su = False  # 证伪不是素数
    if is_su == True:  # 是素数
        print(f"{i}是素数")
        su.append(i)
print(f"1-100之间的所有素数集合：{su}")
