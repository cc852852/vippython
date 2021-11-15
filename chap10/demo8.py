# 咕噜咕噜的丁丁
# 不浪费一分一秒
# 你可以的
# 时间：2021/9/16 14:54
def fun(a,b=10): #b在函数的定义处，所以b是形参，而且进行了赋值，所以b称为默认值形参
    print('a',a)
    print('b',b)

def fun2(*args): #个数可变的位置形参
    print(args)

def fun3(**args2): #个数可变的关键字形参
    print(args2)

fun2(20,30,40) #结果是元组
fun3(a=11,b=22,c=66) #结果是字典

def fun4(a,b,*,c,d): #从*之后的参数，在函数调用时，只能采用关键字参数传递
    print('a', a)
    print('b', b)
    print('c', c)
    print('d', d)

#调用fun4
#fun4(10,20,30,40) #位置实参传递
fun4(a=10,b=20,c=30,d=40) #关键字实参传递
fun4(10,20,c=30,d=40) #前两个参数是位置实参传递，后两个参数采用的是关键字实参传递

'''需求：c，d只能采用关键字实参传递'''

'''函数定义时形参的顺序问题'''
def fun5(a,b,*,c,d,**args):
    pass
def fun6(*args,**args2):
    pass
def fun7(a,b=10,*args,**args2):
    pass