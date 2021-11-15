# 咕噜咕噜的丁丁
# 不浪费一分一秒
# 你可以的
# 时间：2021/9/13 13:37
scores={'张三':100,'李四':98,'王五':45}
#获取所有的key
keys=scores.keys()
print(keys)
print(type(keys))
print(list(keys))#将所有的key组成的视图转换成列表

values=scores.values()
print(values)
print(type(values))
print(list(values))

#获取所有的key-value 对
items=scores.items()
print(items)
print(list(items)) #转换之后的列表元素是由元组组成，元组将在下一节讲解