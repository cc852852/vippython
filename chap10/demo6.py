# 咕噜咕噜的丁丁
# 不浪费一分一秒
# 你可以的
# 时间：2021/9/16 12:57
def fun(*args): #函数定义时的 可变的位置参数
    print(args)
   #print(args[0])

fun(10)
fun(10,30)
fun(10,20,30)

def fun1(**args):
    print(args)

fun1(a=10)
fun1(a=10,b=20)

print('hello','world','python')

'''def fun2(*args,*a)
    pass
    以上代码程序会报错，个数可变的位置参数只能是一个
    *args 个数可变的位置参数
    **args 个数可变的关键字参数
'''
def fun2(*args1,**args2):
    pass
# 在一个函数的定义过程中，既有个数关键字参数，又有个数可变的位置参数，要是个数可变的位置参数放在个数可变的关键字参数前