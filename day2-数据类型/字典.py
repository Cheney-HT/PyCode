dic={
    '胡歌':[22,'演员'],
    '周杰伦':[21,'歌手'],
    '马云':[33,'CEO']
}
dic['乔松涛']=[55,'创始人']# 添加
print(dic)
dic.pop("马云")# 删除
print(dic)
# dic.clear()# 清空
print(dic["胡歌"]) # 根据key查找value
print(dic.keys()) # 打印所有的key
print(dic.items()) # 以列表的形式
for i in dic.items():
    print(i)
print("--------------")
for k,v in dic.items(): #打印key,value 效率低
    print(k,v)
print("--------------")
for i in dic: #打印key,value  效率高
    print(i,dic[i])
print("--------------")
print(len(dic))
