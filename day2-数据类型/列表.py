names1=[]
names2=["a","b","c","d","e"]
names3=["哈","嘿","喔"]
names1.append("1") # 末尾追加元素
names1.insert(0,"0") # 插入元素
names1.extend(names2) # 合并
names1.insert(1,names3) # 列表嵌套
delete=names1.pop() # e 删除最后一个元素并返回元素的值
print(delete)
print(names1)
print(names2)
print(names3)
