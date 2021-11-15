# 咕噜咕噜的丁丁
# 不浪费一分一秒
# 你可以的
# 时间：2021/9/10 17:32
'''
举例：153=3*3*3+5*5*5+1*1*1
此为水仙花数
'''
print('----输出100~999之间的水仙花数----')
for item in range(100,1000):
    ge=item%10 #个位
    shi=item//10%10 #十位
    bai=item//100 #百位
    # print(ge,shi,bai)
    # 判断
    if item==ge**3+shi**3+bai**3:
        print(item)
