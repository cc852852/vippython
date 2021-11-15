# 咕噜咕噜的丁丁
# 不浪费一分一秒
# 你可以的
# 时间：2021/9/6 7:11
# 赋值运算符：从右往左
i=3+4
print(i)
a=b=c=20
print(a,id(a))
print(b,id(b))
print(c,id(c))
print('-_________支持参数赋值_____________')
a=20
a+=30 #相当于a=a+30
print(a)
a-=10
print(a) #相当于a=a-10
a*=2 #相当于a=a*2
print(a)
print(type(a)) #int
a/=3
print(a)
print(type(a))
a//=2
print(a)
print(type(a))
a%=3
print(a)
print(type(a))
print('---------解包赋值--------------------------')
a,b,c=20,30,40
print(a,b,c)
print('-----------交换两个变量的值--------------')
a,b=10,20
print('交换之前：',a,b)
#交换
a,b=b,a
print('交换之后：',a,b)