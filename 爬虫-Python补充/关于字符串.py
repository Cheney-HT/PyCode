# -*- coding: utf-8 -*- 
# Created By CHT  
"""
编码     : encoding="utf-8"
Time    : 2023/8/15 10:21
File    : 关于字符串.py
Project : PycharmCode
"""
# 字符串表示
print("胡歌说:\"我要当爸爸了!\"")  # 其他的语言
print('胡歌说:"我要当爸爸了!"')
print('胡歌说:"我要当爸爸了!"')
print("""胡歌说:"我要当'爸爸'了!" """)

# 索引和切片
s0 = "Cht真的可以改变世界吗？"
print(s0[0])
print(s0[0:3])  # 从0切片到3，顾头不顾尾-Cht
print(s0[0:])  # 从0到最后

# strip 去除所有两端的'空白符'，不能去除中间的空白符
"""
# 若想去除中间的空白符，使用replace替换
\t 制表符,一个缩进
\r 回车
\n 换行符
# 字符串操作：所有的字符串是不可变的数据类型；字符串操作都会返回一个新的字符串
"""
s1 = "   \t\t我是谁\r\n"
s1.strip()
print(s1)
print(s1.strip())
s2 = "hello world,我\t帅\r吗?"
print(s2)
s = s2.replace("\t", "").replace("\r", "").replace(" ", "").strip()
print(s)

# join拼接
list1 = ["陈浩天", "陈阳", "金毛"]
s = "_".join(list1)
print(s)
list1 = ["\n\r", "\n\r", "周\n\r", "不认识我\n\r"]
s = "".join(list1).strip().replace("\n\r", "")
print(s)
