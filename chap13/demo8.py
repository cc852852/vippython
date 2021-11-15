# 咕噜咕噜的丁丁
# 不浪费一分一秒
# 你可以的
# 时间：2021/9/21 15:53


#print(dir(object))
class A:
    pass
class B:
    pass
class C(A,B):
    def __init__(self,name,age):
        self.name=name
        self.age=age
class D(A):
    pass
#创建C类的对象
x=C('Jack',20) #x是C类型的要给实例对象
print(x.__dict__) #实例对象的属性字典
print(C.__dict__) #类对象开到的是属性和方法
print('------------')
print(x.__class__) #<class '__main__.C'> 输出了对象所属的类
print(C.__bases__) #输出的是：C类的父类类型的元素
print(C.__base__) #输出的是：C类的第一个父类元素
print(C.__mro__) #输出的是：类的层次结构
print(A.__subclasses__()) #输出的是：有哪些子类
