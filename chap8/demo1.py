# 咕噜咕噜的丁丁
# 不浪费一分一秒
# 你可以的
# 时间：2021/9/13 20:18
'''不可变序列 以及 可变序列'''
'''可变序列：列表，字典'''
lst=[10,20,45]
print(id(lst))
lst.append(300)
print(id(lst))
'''不可变序列：字符串、元组'''
s='hello'
print(id(s))
s=s+'world'
print(id(s))
print(s)