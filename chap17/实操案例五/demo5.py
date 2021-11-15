# 咕噜咕噜的丁丁
# 不浪费一分一秒
# 你可以的
# 时间：2021/11/2 20:38
import random
rand=random.randint(1,100)
for i in range(1,11):
    num=int(input('在我心中有一个1~100的数，你猜猜看看'))
    if num<rand:
        print('猜小了')
    elif num>rand:
        print('猜大了')
    else:
        print('猜对啦')
        break
print(f'你一共猜了{i}次')
if i<3:
    print('真聪明')
elif i<=7:
    print('还凑和')
else:
    print('貌似不太行哟')