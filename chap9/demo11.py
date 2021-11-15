# 咕噜咕噜的丁丁
# 不浪费一分一秒
# 你可以的
# 时间：2021/9/15 17:20
# 格式化字符串
#（1）%占位符
name='张三'
age=20
print('我叫%s，今年%d岁' %(name,age))

#（2）{}
print('我叫{0}，今年{1}岁，我真的叫{0}'.format(name,age))

#（3）f-string
print(f'我叫{name}，今年{age}岁')