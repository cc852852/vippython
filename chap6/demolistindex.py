# 咕噜咕噜的丁丁
# 不浪费一分一秒
# 你可以的
# 时间：2021/9/11 14:03
lst=['hello','world',98,'hello']
print(lst.index('hello')) #如果列表中又相同元素，只返回列表中的相同元素的以一个索引
#print(lst.index('Python')) #ValueError: 'Python' is not in list
#print(lst.index('hello',1,3)) #ValueError: 'hello' is not in list
print(lst.index('hello',1,4))