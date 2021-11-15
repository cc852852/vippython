# 咕噜咕噜的丁丁
# 不浪费一分一秒
# 你可以的
# 时间：2021/9/8 18:47
'''a=int(input('请输入你的成绩：'))
if a>100:
    print('输入有误')
elif 90<=a<=100:
    print('你的等级是A级')
elif 80<=a<90:
    print('你的等级是B级')
elif 70<=a<80:
    print('你的等级是C级')
elif 60<=a<70:
    print('你的等级是D级')
elif 0<=a<60:
    print('你的等级是E级')
elif a<0:
    print('你的输入有误')'''

score=int(input('请输入你的成绩：'))
if score>=90 and score <=100:
    print('A')
elif score>=80 and score<=89:
    print('B')
elif score>=70 and score<=79:
    print('C')
elif score>=60 and score<=69:
    print('D')
elif score>=0 and score<=59:
    print('E')
else:
    print('你耍我呢？')