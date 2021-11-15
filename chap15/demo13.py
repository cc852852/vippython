# 咕噜咕噜的丁丁
# 不浪费一分一秒
# 你可以的
# 时间：2021/9/23 21:11


'''
MyContentMrg实现了特殊方法__enter__(),__exit__()称为该类对象遵守了上下文管理器协议
该类对象的实例对象，称为上下文管理器

'''
class MyContentMrg(object):
    def __enter__(self):
        print('enter方法被调用执行了')
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print('exit方法被调用执行了')

    def show(self):
        print('show方法被调用执行了')

with MyContentMrg() as file:  #相当于file=MyContentMrg()
    file.show()

