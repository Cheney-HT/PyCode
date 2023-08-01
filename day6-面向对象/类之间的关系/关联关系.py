# -*- coding: utf-8 -*- 
# Created By CHT  
"""
编码     : encoding="utf-8"
Time    : 2023/7/31 17:46
File    : 关联关系.py
Project : PycharmCode
"""


class Relationship:
    """保存couple之间的关系"""

    def __init__(self):
        self.couple = []

    def do_couple(self, obj1, obj2):
        self.couple = [obj1, obj2]
        print(f"{obj1.name}和{obj2.name}确定了男女关系")

    def get_my_partner(self, obj):
        print(f"找{obj.name}的对象")
        for i in self.couple:
            if i != obj:
                return i
        else:
            print("Single Dog...")

    def break_rel(self):
        print(f"{self.couple[0].name}和{self.couple[1].name}正式分手了")
        self.couple.clear()  # 分手


class Person:
    def __init__(self, name, age, sex, relation):
        self.name = name
        self.age = age
        self.sex = sex
        self.relation = relation  # 在实例中存储关系对象
        # self.partner = None  # 对象
        print(f"I am {name},{age}岁,性别：{sex}")

    def do_private_thing(self):
        pass


relation = Relationship()
p1 = Person("cht", 18, "M", relation)
p2 = Person("cy", 18, "F", relation)

relation.do_couple(p1, p2)
print(p1.relation.couple)
print(p1.relation.get_my_partner(p1).name)

p1.relation.break_rel()
p2.relation.get_my_partner(p2)
# p1.partner = p2  # 绑定
# print(p1.partner.name, p2.partner)
# p2.partner = p1  # 双向关联
# print(p1.partner.name, p2.partner.name)
# # 解除关系 但是不能同时解绑 必须双方都解除
# p1.partner = None
# p2.partner = None
# print(p1.partner, p2.partner)
