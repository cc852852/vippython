# 咕噜咕噜的丁丁
# 不浪费一分一秒
# 你可以的
# 时间：2021/10/15 9:33
book_name='python yyds'
print('《'+book_name+'》')

lst_name=['张三','李四','王五','赵六','田七']
lst_sig=['1','2','3','4','5']
for i in range(5):
    print(lst_sig[i]+lst_name[i])
for i in range(5):
    print(lst_sig[i],lst_name[i])


d={'1':'张三','2':'李四','3':'王五','4':'赵六','5':'天琦'}
for key in d:
    print(key,d[key])

print('zip------------')
for s,name in zip(lst_sig,lst_name):
    print(s,name)