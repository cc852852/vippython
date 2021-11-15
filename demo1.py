# 咕噜咕噜的丁丁
# 不浪费一分一秒
# 你可以的
# 时间：2021/9/5 13:00
#可以输出数字
print(520)
print(98.5)

#可以输出字符串
print('helloworld')
print("helloworld")

#含有运算符的表达式
print(3+1)

#将数据输出到文件当中 ps 1、注意盘符存在 2、使用file=
fp=open('E:/text.txt','a+')#a+意思 文件不存在就创建并且写入，文件存在就再文件后面追加
print('helloworld',file=fp)
fp.close()

#不进行换行输出，（输出内容再一行当中）
print('hello','world','python')