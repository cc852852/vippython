# 咕噜咕噜的丁丁
# 不浪费一分一秒
# 你可以的
# 时间：2021/9/10 21:34
for item in range(3):
    pwd=input('请输入密码：')
    if pwd=='8888':
        print('密码正确')
        break
    else:
        print('密码错误')
else:
    print('你的账号已被锁定')