# 咕噜咕噜的丁丁
# 不浪费一分一秒
# 你可以的
# 时间：2021/9/21 13:37
class Car:
    def __init__(self,brand):
        self.brand=brand
    def start(self):
        print('汽车已经启动')

car=Car('宝马X5')
car.start()
print(car.brand)