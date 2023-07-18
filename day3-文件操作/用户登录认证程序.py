# -*- coding: utf-8 -*- 
# Created By CHT  
"""
编码     : encoding="utf-8"
Time    : 2023/7/18 10:45
File    : 全局文本检索替换脚本.py
Project : PycharmCode
"""
"""
解题思路：1、确定数据结构 2、账号存入字典，方便调用 3、书写具体判断逻辑

"""
accounts = {
    # "hg":["hg","111","0"]
}
f = open("account.db", "r")
# 将数据存储在字典里
for line in f:
    line = line.strip().split(",")  # 先去除两边的空格在切片
    accounts[line[0]] = line
print(accounts)
while True:
    user = input("请输入用户名:").strip()
    if user not in accounts:  # 用户未注册
        print("用户未注册...")
        continue
    elif accounts[user][2] == "1":  # 表示此账户已锁定
        print(f"{user}账户已被锁定，请联系管理员开通")
        continue
    count = 0
    while count < 3:
        password = input("请输入密码:").strip()
        if password == accounts[user][1]:
            print(f"Welcome {user}")
            exit("登陆成功")
        else:
            print(f"密码错误，你还剩{2 - count}次机会")
        count += 1
    if count == 3:
        print(f"输错了3次密码，{user}账户将锁定")
        # 修改用户状态为1
        accounts[user][2] = "1"
        # 将数据改回account.db文件
        f2 = open("account.db", "w")
        for user, val in accounts.items():
            line = ",".join(val) + "\n"  # 把列表转为字符串
            f2.write(line)
        f2.close()
        exit("bye...")
