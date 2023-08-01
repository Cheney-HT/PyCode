# -*- coding: utf-8 -*- 
# Created By CHT  
"""
编码     : encoding="utf-8"
Time    : 2023/7/31 17:37
File    : 依赖关系.py
Project : PycharmCode
"""


class Dog:

    def __init__(self, name, type, master):
        self.name = name
        self.type = type
        self.master = master
        self.sayhi()

    def sayhi(self):  # 方法，第一个参数必须是self,self代表实例本身
        print(f"我是{self.name},一只品种是{self.type}的狗，我的主人是{self.master.name}")


class People:

    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def walk_dog(self, dog):
        print(f"主人{self.name}带着{dog.name}去遛弯")


p1 = People("胡歌", 18, "M")
d1 = Dog("毛毛", "金毛", p1)
p1.walk_dog(d1)
