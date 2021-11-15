# 咕噜咕噜的丁丁
# 不浪费一分一秒
# 你可以的
# 时间：2021/10/31 21:48
import random
price=random.randint(1000,1500)
print('今日竞猜的商品为哈哈儿：价格在1000~1500之间')
while True:
    guess=int(input('请输入你要猜的价格'))
    if guess>price:
        print('大了')
        continue
    elif guess<price:
        print('小了')
        continue
    else:
        print('猜对了')
        break
print('真实价格为：',price)