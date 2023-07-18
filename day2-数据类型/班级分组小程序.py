stu_list = [["杨振宁", 100], ["韦东奕", 95],
            ["伊力", 88], ["陈吉宁", 85], ["楼阳生", 89],
            ["周杰伦", 78], ["毛不易", 77], ["胡歌", 79],
            ["张杰", 65], ["倪岳峰", 66], ["袁家军", 69],
            ["周深", 59], ["gai", 40]
            ]
for i in stu_list:
    print(i)
new_stu_list = [[],  # 90-100
                [],  # 80-89
                [],  # 70-79
                [],  # 60-69
                []]  # 0-59
for i in stu_list:
    if i[1] >= 90:
        new_stu_list[0].append(i)
    elif i[1] >= 80:
        new_stu_list[1].append(i)
    elif i[1] >= 70:
        new_stu_list[2].append(i)
    elif i[1] >= 60:
        new_stu_list[3].append(i)
    else:
        new_stu_list[4].append(i)
for group in new_stu_list:
    print(group)
