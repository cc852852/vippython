# 咕噜咕噜的丁丁
# 不浪费一分一秒
# 你可以的
# 时间：2021/11/7 21:47
class Car(object):
    def __init__(self,type,no):
        self.type=type
        self.no=no

    def start(self):
        pass
    def stop(self):
        pass

class Taxi(Car):
    def __init__(self,type,no,company):
        super().__init__(type,no)
        self.company=company
    def start(self):
        print('乘客您好')
        print(f'我是{self.company}出租车公司，我的车牌是{self.no},请问你要去哪里')
    def stop(self):
        print('目的地到了，请付款下次，欢迎下次乘坐')

class FamilyCar(Car):
    def __init__(self,type,no,name):
        super().__init__(type,no)
        self.name=name
    def stop(self):
        print('目的地到了，我么们去完咯')
    def start(self):
        print(f'我是{self.name},我的汽车我做主')

if __name__ == '__main__':
    taxi=Taxi('上海大众','粤A88888','五羊')
    taxi.start()
    taxi.stop()
    print('-'*30)
    familycar=FamilyCar('广汽本田','粤A66666','哈哈儿')
    familycar.start()
    familycar.stop()
