# 咕噜咕噜的丁丁
# 不浪费一分一秒
# 你可以的
# 时间：2021/9/11 12:34
'''流程控制语句break与continue在二重循环中的作用'''
for i in range(5): #代表外层循环要执行5次
    for j in range(1,10):
        if j%2==0:
            #break
            continue
        print(j,end='\t')
    print()