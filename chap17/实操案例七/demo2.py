# 咕噜咕噜的丁丁
# 不浪费一分一秒
# 你可以的
# 时间：2021/11/3 12:22
dict_ticket={'G1569':['北京南-天津南','18:05','18:39','00:37'],
             'G1567':['北京南-天津南','18:15','18:49','00:34'],
             'G8917':['北京南-天津南','18:20','19:19','00:59'],
             'G203 ':['北京南-天津南','18:35','19:09','00:34']}
print(' 车次\t出发站-到达站\t 出发时间\t 到达时间\t 历史时长')
for item in dict_ticket:
    print(item,end='   ')
    for i in dict_ticket[item]:
        print(i,end='   ')
    print() #换行
#输入要购买的车次
train_no=input('请输入要购买的车次：')
person=input('请输入乘车人，如果是多人请用都逗号分隔：')
s=f'你已购买了{train_no}次列车 '
s_info=dict_ticket[train_no] #获取车次详细信息
s+=s_info[0]+' '+s_info[1]+' 开'
print(f'{s}请{person}尽快取走纸质车票【铁路客服】')
