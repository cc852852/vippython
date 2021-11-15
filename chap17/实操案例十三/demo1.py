# 咕噜咕噜的丁丁
# 不浪费一分一秒
# 你可以的
# 时间：2021/11/7 21:21
class Instrument():
    def make_sound(self):
        pass

class Erhu(Instrument):
    def make_sound(self):
        print('二胡在演奏')
class Piano(Instrument):
    def make_sound(self):
        print('钢琴在演奏')
class Violin(Instrument):
    def make_sound(self):
        print('小提琴在演奏')

class Bird():
    def make_sound(self):
        print('小鸟在唱歌')

#演奏的函数
def play(instrument):
    instrument.make_sound()

if __name__ == '__main__':
    play(Erhu())
    play(Piano())
    play(Violin())
    play(Bird())