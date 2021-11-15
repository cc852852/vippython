# 咕噜咕噜的丁丁
# 不浪费一分一秒
# 你可以的
# 时间：2021/11/4 12:50
def get_count(s,ch):
    count=0
    for item in s:
        if ch.upper()==item or ch.lower()==item:
            count+=1
    return count

if __name__ == '__main__':
    s='hellopython,hellojava,hellogo'
    ch=input('请输入要统计的字符：')
    count=get_count(s,ch)
    print(f'{ch}在{s}中出现的次数为{count}次')