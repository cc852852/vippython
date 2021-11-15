# 咕噜咕噜的丁丁
# 不浪费一分一秒
# 你可以的
# 时间：2021/11/14 21:20
print("s1 = 'Hello, world'")
print("s2 = 'Hello, \\'Adam\\''")
print("s3 = r'Hello, \"Bart\"'")
print("s4 = r'''Hello,\nLiaa!'''")

print(ord('中'))
ord('文')
print(b'ABC'.decode(('ascii')))
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))
print(len('ABC'))
print(len('中文'))
print('hello,%s,you have $%d' %('andy',10000))
print('%2d-%02d' %(3,1))
print('%.2f' % 3.1415926)
print('hello,{0},成绩提升了{1:.1f}%'.format('小明',17.125))
r = 2.5
s = 3.14 * r ** 2
print(f'the area of a circle with radius {r} is {s:.2f}')

s1=72
s2=85
r=(s2-s1)/s1*100
n='小明'
print('相比去年，小明的成绩提高了%.1f%%' %r)
print(f'相比去年，{n}的成绩提高了{r:.1f}%')
print('相比去年，{0}的成绩提高了{1:.1f}%'.format(n,r))