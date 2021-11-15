# 咕噜咕噜的丁丁
# 不浪费一分一秒
# 你可以的
# 时间：2021/9/8 14:01
money=1000 #余额
s=int(input('请输入取款金额：')) #取款金额
#判断余额是否充足
if money>=s:
    money=money-s
    print('取款成功，余额为：',money)
