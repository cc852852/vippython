# 咕噜咕噜的丁丁
# 不浪费一分一秒
# 你可以的
# 时间：2021/9/21 14:56
class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return '我的名字是{0}，今年{1}岁了'.format(self.name,self.age)

stu=Student('张三',20)
print(dir(stu))
print(stu) #默认调用 __str__()这样的方法
print(type(stu))