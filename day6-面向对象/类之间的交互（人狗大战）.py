# -*- coding: utf-8 -*- 
# Created By CHT  
"""
编码     : encoding="utf-8"
Time    : 2023/7/31 17:06
File    : 类之间的交互（人狗大战）.py
Project : PycharmCode
"""


class Dog:
    def __init__(self, name, bite_val, health_val):
        self.name = name
        self.bite_val = bite_val
        self.health_val = health_val

    def bite(self, person):
        person.health_val -= self.bite_val
        print(f"{self.name}咬了{person.name},{person.name}还剩{person.health_val}")


class Person:
    def __init__(self, name, attack_val, health_val):
        self.name = name
        self.attack_val = attack_val
        self.health_val = health_val

    def attack(self, dog):
        dog.health_val -= self.attack_val
        print(f"{self.name}打了{dog.name},{dog.name}还剩{dog.health_val}")


d1 = Dog("金毛1", 30, 100)
p1 = Person("胡歌", 50, 100)
p1.attack(d1)
d1.bite(p1)
