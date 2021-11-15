# 咕噜咕噜的丁丁
# 不浪费一分一秒
# 你可以的
# 时间：2021/9/7 13:28
# 布尔运算符
a,b=1,2
print('-----------and 并且-------------')
print(a==1 and b==2) #True  True and True  ---> True
print(a==1 and b<2) #False  True and Flase ---> False
print(a!=1 and b==2) #False Flase and True ---> False
print(a!=1 and b!=2) #False False and False ---> False
print('------------oe 或者--------------')
print(a==1 or b==2) #有一个是True就是True
print(a==1 or b<2)
print(a!=1 or b==2)
print(a!=1 or b!=2)

print('---------not bool类型，对bool类型操作数取反---------')
f=True
f2=False
print(not f)
print(not f2)

print('============in 与 not in------------')
s='helloworld'
print('w' in s )
print('k' in s)
print('w' not in s)
print('k' not in s)