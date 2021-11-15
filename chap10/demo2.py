# 咕噜咕噜的丁丁
# 不浪费一分一秒
# 你可以的
# 时间：2021/9/15 20:44
def fun(arg1,arg2):
    print('arg1',arg1)
    print('arg2',arg2)
    arg1=100
    arg2.append(10)
    print('arg1',arg1)
    print('arg2',arg2)
n1=11
n2=[22,33,44]
print(n1)
print(n2)
print('-------------')
fun(n1,n2)
print(n1)
print(n2)
'''在函数调用过程中，进行参数的传递，
如果是不可改变对象，在函数体的修改不会影响实参的值 arg1的修改不会影响n1的值
如果是可变对象，在函数体内的修改回影响实参的值 arg2的修改回影响n2的值
'''