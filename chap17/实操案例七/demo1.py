# 咕噜咕噜的丁丁
# 不浪费一分一秒
# 你可以的
# 时间：2021/11/2 21:26
constellation=['1','2','3','4','5','6','7','8','9']
nature=['a','b','c','d','e','f','g','h','i']
d=dict(zip(constellation,nature))
'''for item in a:
    print(item,a[item])'''
print(d)
key=input('请输入星座名称：')
flag=True
for item in d:
    if key==item:
        flag=True
        print(key,'的性格特点为：',d.get(key))
        break
    else:
        #print('对八起，你的输入有误，请重新输入')

        flag=False
if not flag:
    print('对不起，你输入有误')