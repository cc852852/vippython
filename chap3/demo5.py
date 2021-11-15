# 咕噜咕噜的丁丁
# 不浪费一分一秒
# 你可以的
# 时间：2021/9/7 12:45
# 比较运算符  比较运算符结果为bool类型
a,b=10,20
print('a>b吗？',a>b) #Flase
print('a<b吗？',a<b)
print('a<=b?',a<=b)
print('a>=b?',a>=b)
print('a==b?',a==b)
print('a!=b？',a!=b)

'''一个 = 称谓赋值运算符；==称为比较运算符
一个变量由三部分组成 标识 类型 值
==比较的是值还是标识呢？ 比较的是值
比较对象的标识 使用的是 is
'''
a=10
b=10
print(a==b) #说明 a与b 的value相等
print(a is b) #说明 a与b 的id标识相等
print(id(a))
print(id(b))
#一下代码还没学，后面会讲解
lst1=[11,22,33,44]
lst2=[11,22,33,44]
print(lst1==lst2) #value  true
print(lst1 is lst2) #id  false
print(id(lst1))
print(id(lst2))
print(a is not b) #Flase
print(lst1 is not lst2) #True
