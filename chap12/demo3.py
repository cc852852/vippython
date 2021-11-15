# 咕噜咕噜的丁丁
# 不浪费一分一秒
# 你可以的
# 时间：2021/9/17 8:49
class Student:
    native_place='广州' #直接写在类里的变量称为类属性
    def __init__(self,name,age):
        self.name=name #self.name称为实体属性，进行了一个赋值操作，将局部变量的name赋值给实体属性
        self.age=age

    #实例方法
    def eat(self):
        print('学生在吃饭。。。')

    #静态方法
    @staticmethod
    def method():
        print('我使用了staticmethod进行修饰，所以我是静态方法')

    #类方法
    @classmethod
    def cm(cls):
        print('我是类方法，因为我使用了classmethod进行修饰')
#实例方法，在类之外定义的称为函数，在类之内定义的称为方法

def drink():
    print('喝水')

stu1=Student('张三',20)
print(id(stu1))
print(type(stu1))
print(stu1)
print('-------------------')
print(id(Student))
print(type(Student))
print(Student)