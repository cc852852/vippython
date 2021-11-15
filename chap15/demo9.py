# 咕噜咕噜的丁丁
# 不浪费一分一秒
# 你可以的
# 时间：2021/9/23 20:17

file=open('c.txt','r')
file.seek(2)
print(file.read())
print(file.tell())
file.close()