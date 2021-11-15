# 咕噜咕噜的丁丁
# 不浪费一分一秒
# 你可以的
# 时间：2021/9/14 19:56
# 字符串中大小写转换的方法
s='hello,python'
a=s.upper() #转成大写后会产生一个新的字符串对象
print(a,id(a))
print(s,id(s))
b=s.lower() #转换后会产生一个新的字符串
print(b,id(b))
print(s,id(s))
print(b==s) #True 内容相等
print(b is s) #False 地址不相等

s2='hello,Python'
print(s2.swapcase())
print(s2.capitalize())
print(s.title())