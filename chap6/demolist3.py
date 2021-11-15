# 咕噜咕噜的丁丁
# 不浪费一分一秒
# 你可以的
# 时间：2021/9/12 16:16
lst=[10,20,30,40,50,60,70,80]
# start=1,stop=6,step=1
#print(lst[1:6:1])
print('原列表',id(lst))
lst2=lst[1:6:1]
print('新列表',id(lst2))
print(lst[1:6]) #默认步长为1
print(lst[1:6:])
#print(id(lst3))
print(lst[1:6:2]) #start=1;stop=6;step=2
print(lst[:6:2]) #start留空，stop为6，step为2
print(lst[1::2]) #start=1;stop留空，step=2
print('----step为负数的情况----')
print('源列表：',lst)
print(lst[::-1])
#start=7;stop省略,step=-1
print(lst[7::-1])
#start=6;stop=0;step=-2
print(lst[6:0:-2])