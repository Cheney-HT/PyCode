f=open("联系方式")
for line in f:
    line=line.split() #将字符串分隔为列表  默认空格
    height=int(line[3])
    weight=int(line[4])
    if height>=172 and weight<=50:
        print(line)