# 咕噜咕噜的丁丁
# 不浪费一分一秒
# 你可以的
# 时间：2021/9/10 21:42
''''输出一个三行四列的矩形'''
'''for i in range(1,4): #行表，执行三次，每次一行
    for j in range(1,5):
        print('*',end='\t')  #不换行输出
    print() #打行'''
'''for i in range(1,4):
    for j in range(1,5):
        print('*',end='\t')
    print()'''
for i in range(1,10):
    for j in range(1,i+1):
        print(i,'*',j,'=',i*j,end='\t')
    print()