# 咕噜咕噜的丁丁
# 不浪费一分一秒
# 你可以的
# 时间：2021/11/2 20:55
year=[82,89,88,86,85,00,99]
print('原列表：',year)
for index,value in enumerate(year):
    #print(index,value)
    if str(value)!='0':
        year[index]=int('19'+str(value))
    else:
        year[index]=int('200'+str(value))

print('修改后列表：',year)
year.sort(reverse=True)
print('排序后列表：',year)