# 咕噜咕噜的丁丁
# 不浪费一分一秒
# 你可以的
# 时间：2021/10/31 21:40
pwd=input('请输入支付宝密码：')
if pwd.isdigit():
    print('支付数据合法！')
else:
    print('支付数字不合法！支付密码只能是数字')

print('---------------------')
print('支付数据合法！' if pwd.isdigit() else '支付数字不合法！支付密码只能是数字')