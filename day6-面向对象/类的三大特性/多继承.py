# -*- coding: utf-8 -*- 
# Created By CHT  
"""
编码     : encoding="utf-8"
Time    : 2023/8/26 12:01
Project : PycharmCode
"""


# 继承深度优先 ，fight先找到Monkey就用Monkey的fight,没找到就向上找MonkeyBase
class MonkeyBase(object):
    def fight(self):
        print("猿猴在打架")


class Monkey(MonkeyBase):
    def eat_peach(self):
        print("猴子喜欢吃桃子。。。")

    # def fight(self):
    #     print("猴子在打架。。。")


class Immortal(object):  # Immortal神仙
    def fly(self):
        print("神仙都会飞。。。")

    def fight(self):
        print("神仙在打架。。。")


# 多继承  继承顺序从左到右
class MonkeyKing(Monkey, Immortal):
    def play_golden_cudgel(self):  # golden cudgel金箍棒
        print("孙悟空会玩金箍棒。。。")


m = MonkeyKing()
m.fly()
m.eat_peach()
m.play_golden_cudgel()
# m.fight()  # 猴子在打架。。。
m.fight()  # 猿猴在打架
