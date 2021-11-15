# 咕噜咕噜的丁丁
# 不浪费一分一秒
# 你可以的
# 时间：2021/9/5 21:09
name='张三'
age=20
print(type(name),type(age))
print('我叫',name,'。今年',age,'岁')
print('我叫'+name+'。今年'+str(age)+'岁')

print('-----------str()将其他类型转成str类型------------------')
a=10
b=198.8
c=False
print(type(a),type(b),type(c))
print(str(a),str(b),str(c),type(a),type(b),type(c))
print('-----------int()将其他类型转成int类型------------------')
s1='128'
f1=98.7
s2='76.77'
ff=True
s3='hello'
print(type(s1),type(f1),type(s2),type(ff),type(s3))
print(int(s1),type(int(s1)))
print(int(f1),type(int(f1)))
print(int(ff),type(int(ff)))
print('-----------float()将其他类型转成float类型------------------')
s1='128.98'
s2='76'
ff=True
s3='hello'
i=98
print((type(s1),type(s2),type(ff),type(s3)))
print(float(s1),type(float(s1)))
print(float(s2),type(float(s2)))
print(float(ff),type(float(ff)))
print(float(i),type(i))