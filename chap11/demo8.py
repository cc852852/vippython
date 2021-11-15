# 咕噜咕噜的丁丁
# 不浪费一分一秒
# 你可以的
# 时间：2021/9/16 20:34
try:
    a=int(input('请输入第一个整数：'))
    b=int(input('请输入第二个整数：'))
    result=a / b
except BaseException as e:
    print('出错了，',e)
else:
    print('计算结果为：',result)
finally:
    print('谢谢了啊')