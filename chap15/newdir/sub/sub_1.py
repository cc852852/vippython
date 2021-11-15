# 咕噜咕噜的丁丁
# 不浪费一分一秒
# 你可以的
# 时间：2021/9/24 21:23
import os
path=os.getcwd()
lst_files=os.walk(path)
print(lst_files)
for dirpath,dirnames,filenames in lst_files:
    print(dirpath)
    print(dirnames)
    print(filenames)