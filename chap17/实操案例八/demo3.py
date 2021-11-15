# 咕噜咕噜的丁丁
# 不浪费一分一秒
# 你可以的
# 时间：2021/11/3 14:26
phones=set()
for i in range(5):
    info=input(f'请输入第{i+1}个朋友的姓名和电话号码：')
    phones.add(info)

for item in phones:
    print(item)