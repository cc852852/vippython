# 咕噜咕噜的丁丁
# 不浪费一分一秒
# 你可以的
# 时间：2021/9/24 21:22
import os
path=os.getcwd()
lst_files=os.walk(path)
#print(lst_files)
for dirpath,dirname,filename in lst_files:
    '''print(dirpath)
    print(dirnames)
    print(filenames)
    print('--------------')'''
    for dir in dirname:
        print(os.path.join(dirpath,dir))

    for file in filename:
        print(os.path.join(dirpath,file))
    print('-------------------')