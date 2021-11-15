# 咕噜咕噜的丁丁
# 不浪费一分一秒
# 你可以的
# 时间：2021/9/16 15:53
def fac(n):
    if n==1:
        return 1
    else:
        return n*fac(n-1)

print(fac(6))