a = "hello world"
print(type(a))
print("切片："+a[3:6]) # 切片：lo_
print("center:"+a.center(20,'-')) # center:----hello_world1----
print("count:"+str(a.count("l"))) # count:3
print("endswith:"+str(a.endswith("1"))) # endswith:False 判断结尾
print("startswith:"+str(a.startswith("h"))) # startswith:True 判断开头
print("find:"+str(a.find("l"))) # find:2 找到输出下标  -1表示没找到
print("isdigit:"+str("22".isdigit())) # isdigit:True 判断是否为整数
print("isdecimal:"+str(a.isdecimal())) # isdecimal:False 判断是否为小数
l=["wo","love","cy","!"]
print("join:"+"-".join(l)) # join:wo-love-cy-! 字符串拼接
print("replace:"+a.replace("d","d!")) # replace:hello world!
print("strip:"+str(a.strip())) # strip:hello world 去除两边的空格
print("split:"+str(a.split())) # split:['hello', 'world'] 将字符串分隔为列表