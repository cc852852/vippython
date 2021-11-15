# 咕噜咕噜的丁丁
# 不浪费一分一秒
# 你可以的
# 时间：2021/11/4 21:14
import random
def guess(num,guess_num):
    if num==guess_num:
        return 0
    elif guess_num>num:
        return 1
    else:
        return -1

num=random.randint(1,100)
for i in range(10):
    guess_num=int(input('在我心里有个数，0到100，猜猜看看'))
    result=guess(num,guess_num)
    if result==0:
        print('恭喜你，猜对了！')
        break
    elif result>0:
        print('猜大了，猜小一点')
    else:
        print('猜小了，猜大一点')
else:
    print('大笨蛋，10次都没猜对哈哈哈哈')