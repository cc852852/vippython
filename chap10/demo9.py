# 咕噜咕噜的丁丁
# 不浪费一分一秒
# 你可以的
# 时间：2021/9/16 15:40
def fun(a,b):
    c=a+b  #c称为局部变量，因为c就是在函数体内进行定义的变量；a，b为函数的形参，作用范围也是函数内部，相当于局部变量
    print(c)

name='丁丁' #name的作用范围为函数的内部和函数的外部都可以使用————》称为全局变量
print(name)

def fun2():
    print(name)

fun2()

def fun3():
    global age #函数内部定义的变量为局部变量，局部变量使用global声明，这个变量实际上就变成了全局变量
    age=20
    print(age)
fun3()
print(age)