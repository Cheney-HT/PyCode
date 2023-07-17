# r，只读模式，不能写
# w，创建模式，若文件存在则覆盖，不能读
# a，追加模式，新数据会写到文件末尾，能写不能读

# r，只读模式
f=open("火锅_食材",mode="w")

f.write("羊肉卷\n") #写入操作
f.write("麻辣牛肉\n")
f.write("精品毛肚\n")

f.close()

# w，创建模式
f=open("火锅_食材",mode="r")

print(f.readline())
print("-------------")
print(f.read())

f.close()

# a，追加模式
f=open("火锅_食材",mode="a")
f.write("绣球菌")

f.close()