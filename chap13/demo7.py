# 咕噜咕噜的丁丁
# 不浪费一分一秒
# 你可以的
# 时间：2021/9/21 15:18
class Animal(object):
    def eat(self):
        print('动物会吃')
class Dog(Animal):
    def eat(self):
        print('狗吃骨头')
class Cat(Animal):
    def eat(self):
        print('猫吃鱼')

class Person:
    def eat(self):
        print('人吃五谷杂粮')


#定义一个函数
def fun(obj):
    obj.eat()

#开始调用函数fun
fun(Dog())
fun(Cat())
fun(Animal())
print('-----------')
fun(Person())