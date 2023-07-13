# for循环
girl_age=22
for i in range(3):
    guess=int(input("请输入你猜测的年龄："))
    if guess>girl_age:
        print("讨厌，人家没有那么老!") #猜大了
    elif guess<girl_age:
        print("虽然我看着年轻，但你没猜对哦！") #猜小了
    else:
        exit("恭喜你，带我走吧！")
