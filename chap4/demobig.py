# 咕噜咕噜的丁丁
# 不浪费一分一秒
# 你可以的
# 时间：2021/9/9 11:50
'''从键盘录入两个整数，比较两个整数的大小'''
'''a=int(input('请输入第一个整数：'))
b=int(input('请输入第二个整数：'))
if a>b:
    print(a,'比',b,'大')
elif a<b:
    print(b,'比',a,'大')
else:
    print('一样大')'''

num_a=int(input('请输入第一个整数'))
num_b=int(input('请输入第二个整数'))
'''if num_a>=num_b:
    print(num_a,'大于等于',num_b)
else:
    print(num_a,'小于',num_b)'''

print('使用条件表达式进行比较')
print(  str(num_a)+'大于等于'+str(num_b)    if num_a>=num_b   else  str(num_a)+'小于'+str(num_b))