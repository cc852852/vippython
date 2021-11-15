# 咕噜咕噜的丁丁
# 不浪费一分一秒
# 你可以的
# 时间：2021/9/16 20:23
try:
    a=int(input('请输入第一个整数：'))
    b=int(input('请输入第二个整数：'))
    result=a/b
    print('结果为：',result)
except ZeroDivisionError:
    print('除数不允许为0')
print('程序结束')