# -*- coding: utf-8 -*- 
# Created By CHT  
"""
编码     : encoding="utf-8"
Time    : 2023/8/26 11:30
Project : PycharmCode
"""


# 父类
class Animal:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def eat(self):
        print(f"{self.name} is eating...")


# 继承父类Animal
class Dog(Animal):
    def bite(self):
        print(f"{self.name} is biting")

    # 重写方法
    def eat(self):
        print(f"{self.name}在胡乱地eating")


d = Dog("二哈", 5, "FM")
d.bite()
d.eat()


# 重写父类方法
class Person(Animal):

    def __init__(self, name, age, sex, hobby):
        # Animal.__init__(self, name, age, sex) py2
        # super(Person, self).__init__(name, age, sex)   py3  效果同上
        super().__init__(name, age, sex)  # py3  效果同上
        self.hobby = hobby

    def think(self):
        print(f"{self.name} is thinking")

    # 重写方法，执行子类的eat方法
    def eat(self):
        # 先执行父类eat
        # Animal.eat(self)
        super().eat()  # py3  效果同上
        print(f"{self.name}在优雅地eating")


p1 = Person("zzy", 15, "男", "女人")
p1.eat()
p1.think()
print(p1.name, p1.hobby)
