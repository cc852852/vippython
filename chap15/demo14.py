# 咕噜咕噜的丁丁
# 不浪费一分一秒
# 你可以的
# 时间：2021/9/23 21:22

with open('yasuo.jpg','rb') as src_file:
    with open('copy2yasuo.jpg','wb') as target_file:
        target_file.write(src_file.read())