# 咕噜咕噜的丁丁
# 不浪费一分一秒
# 你可以的
# 时间：2021/9/10 21:26
'''要求输出1到50之间所有5的倍数
和5的余数为0，均为5的倍数
什么样的数不是5的倍数，和5的余数不为0的数就不是5的倍数
要求使用continue实现
'''
'''for item in range(1,51):
    if item%5==0:
        print(item)'''
for item in range(1,51):
    if item%5!=0:
        continue
    else:
        print(item)

