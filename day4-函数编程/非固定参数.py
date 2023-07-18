# -*- coding: utf-8 -*- 
# Created By CHT  
"""
编码     : encoding="utf-8"
Time    : 2023/7/18 15:20
File    : 非固定参数.py
Project : PycharmCode
"""


def information(name, age, *args, **kwargs):
    print(name, age, args, kwargs)
    print("姓名:", name)
    print("年龄:", age)
    print("性别:",args[0])
    print("地址:", kwargs.get("addr"))


"""
*args 将多个传入的参数转成一个元祖形式
**kwargs 将传入的参数转为字典形式
"""
information("huge", 22, "Man", "Girl", 121212121, addr="beijing", hobby="篮球")
