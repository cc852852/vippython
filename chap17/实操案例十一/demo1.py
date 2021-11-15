# 咕噜咕噜的丁丁
# 不浪费一分一秒
# 你可以的
# 时间：2021/11/7 15:55
try:
    score=int(input('请输入你的分数：'))
    if 0<=score<=100:
        print('分数为：',score)
    else:
        raise Exception('分数不正确！')
except Exception as e:
    print(e)
