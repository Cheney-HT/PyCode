# -*- coding: utf-8 -*- 
# Created By CHT  
"""
编码     : encoding="utf-8"
Time    : 2023/7/31 10:56
File    : 类.py
Project : PycharmCode
"""


class Dog:
    d_type = "金毛"  # 属性，类属性，类变量 ，公共属性

    # 定义私有属性
    def __init__(self, name, age):  # 初始化方法，构造方法，构造函数，实例化时自动执行，进行一些初始化工作
        print(name, age)
        # 把name,age存到实例里，需要与实例绑定
        self.name = name
        self.age = age

    def sayhi(self):  # 方法，第一个参数必须是self,self代表实例本身
        print(f"我是{self.name},年龄{self.age}岁,品种是：{self.d_type}")  # self. 调用自己的属性


# 实例化
d = Dog("杨洋", 5)
# 调用类属性-公共属性
d.sayhi()
print(Dog.d_type)
# 调用实例属性 ,只能通过的实例调用
print(d.name)


class People:
    nationality = "CN"

    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex


p1 = People("huge", 18, "nan")
p2 = People("lilianjie", 30, "nan")
p2.nationality = "M"  # 实例属性改变不会影响公共属性

print(p1.nationality)
print(p2.nationality)
