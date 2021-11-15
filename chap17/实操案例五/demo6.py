# 咕噜咕噜的丁丁
# 不浪费一分一秒
# 你可以的
# 时间：2021/11/2 20:46
import math
for i in range(100,1000):
    if math.pow((i%10),3)+math.pow((i//10%10),3)+math.pow((i//100),3)==i:
        print(i)