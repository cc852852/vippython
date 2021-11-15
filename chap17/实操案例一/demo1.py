# 咕噜咕噜的丁丁
# 不浪费一分一秒
# 你可以的
# 时间：2021/10/13 20:25
'''使用print方式进行输出，（输出的目的地是文件）'''
fp=open('E:/实操保存的目录/text.txt','w')
print('奋斗成就更好的你',file=fp)
fp.close()

'''第二种方式，使用文件的读写操作'''
with open('E:/实操保存的目录/test.txt','w') as file:
    file.write('奋斗成就更好的你')