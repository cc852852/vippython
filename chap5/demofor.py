# 咕噜咕噜的丁丁
# 不浪费一分一秒
# 你可以的
# 时间：2021/9/10 17:16
'''for item in 'python': #第一次取出来的是p，讲p赋值给item，将item的值输出
    print(item)

# range()产生一个整数序列，---》也是一个可迭代对象
for i in range(10):
    print(i)

#如果在循环体中，不需要使用到自定义变量，可将自定义变量写为“_”
for _ in range(5):
    print('人生苦短，我选python')'''
print('-----使用for循环计算1~100之间的偶数和-----')
'''sum=0 #用于存储偶数和
for a in  range(0,101,2):
    sum+=a
print(sum)'''
sum=0  #存储偶数和
for item in range(1,101,1):
    if item %2==0:
        sum+=item
print(sum)