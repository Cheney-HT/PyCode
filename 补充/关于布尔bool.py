# -*- coding: utf-8 -*- 
# Created By CHT  
"""
编码     : encoding="utf-8"
Time    : 2023/8/15 10:06
File    : 关于布尔bool.py
Project : PycharmCode
"""
print(bool("haha"))  # True
print(bool("哈哈"))  # True
print(bool(10086))  # True
print(bool(1))  # True
print(bool(0))  # False
print(bool(-1))  # True
print(bool(""))  # False
print(bool(None))  # False
print(bool([]))  # False

# 在python中，只要表示空的东西，都是False；只有有东西就是True
