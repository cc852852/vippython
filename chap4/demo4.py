# 咕噜咕噜的丁丁
# 不浪费一分一秒
# 你可以的
# 时间：2021/9/8 19:02
'''a=float(input('欢迎来到丁丁超市，请输入你的消费金额：')) #询问金额
b=str(input('请问你是会员吗？请回答是 或者 不是'))
if b==str('是'):
    if a>=200:
        print('本次消费打9折，请支付',a*0.9,'元')
    elif 100<=a<200:
        print('本次消费打9.5折，请支付',a*0.95,'元')
    else:
        print('本次消费不打折，请支付',a,'元')
else:
    if a>=200:
        print('本次消费打9.5折，请支付',a*0.95,'元')
    else:
        print('本次消费不打折，请支付',a,'元')'''
answer=input('您是会员吗？y/n')
money=float(input('请输入你的购物金额：'))
#外层判断是否是会员
if answer=='y': #会员
    if money>=200:
        print('打8折，付款金额为：',money*0.8)
    elif money>=100:
        print('打9折，付款金额为：',money*0.9)
    else:
        print('不打折，付款金额为',money)
else: #非会员
    if money>=200:
        print('打9.5折，付款金额为：',money*0.95)
    else:
        print('不打折，付款金额为：',money)

