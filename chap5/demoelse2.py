# 咕噜咕噜的丁丁
# 不浪费一分一秒
# 你可以的
# 时间：2021/9/10 21:38
a=0
while a<3:
    pwd=input('请输入密码：')
    if pwd=='8888':
        print('密码正确！')
        break
    else:
        print('密码错误!')
        a+=1
else:
    print('账号锁定')