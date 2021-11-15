# 咕噜咕噜的丁丁
# 不浪费一分一秒
# 你可以的
# 时间：2021/9/23 20:17

src_file=open('yasuo.jpg','rb')

target_file = open('copyyasuo.jpg','wb')

target_file.write(src_file.read())

target_file.close()
src_file.close()