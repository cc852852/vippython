# 咕噜咕噜的丁丁
# 不浪费一分一秒
# 你可以的
# 时间：2021/9/15 16:52
s='hello,Python'
s1=s[:5] #由于没有指定起始位置，所以从零开始切
s2=s[6:] #由于没有指定结束位置，所以切到字符串的最后一个元素
s3='!'
newstr=s1+s3+s2

print(s1)
print(s2)
print(newstr)
print('==========================')
print(id(s))
print(id(s1))
print(id(s2))
print(id(s3))
print(id(newstr))

print('========切片[start:end:step]===============')
print(s[1:5:1]) #从1开始截到5（不包含5），步长为1
print(s[::2]) #没有写开始，默认0开始；没有写结束，默认到字符串的最后一个元素，步长为2；两个元素之间的索引间隔为2
print(s[::-1]) #默认从字符串最后一个元素开始，到字符串第一个元素结束，因为步长为负数
print(s[6::])
print(s[-6::1]) #从索引从为-6开始到字符串的最后一个元素结束，步长为1