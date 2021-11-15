# 咕噜咕噜的丁丁
# 不浪费一分一秒
# 你可以的
# 时间：2021/9/15 16:12
print('apple'>'app') #True
print('apple'>'banana') #False 相当于 97>98吗？结果为False
print(ord('a'),ord('b'))
print(ord('冯'))

print(chr(97),chr(98))
print(chr(20911))

'''==与is的区别
==比较的是value
is比较的是id是否相等'''
a=b='Python'
c='Python'
print(a==b) #True
print(b==c) #True

print(a is b) #True
print(a is c) #True
print(id(a)) #1465957111984
print(id(b)) #1465957111984
print(id(c)) #1465957111984