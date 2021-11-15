# 咕噜咕噜的丁丁
# 不浪费一分一秒
# 你可以的
# 时间：2021/11/14 19:51
def find_answer(question):
    with open('replay.txt','r',encoding='gbk') as file:
        while True:
            line=file.readline()
            if not line:
                break
            #字符串的分割
            keyword=line.split('|')[0]
            reply=line.split('|')[1]
            if keyword in question:
                return reply
    return False

if __name__ == '__main__':

    question=input('Hi，你好，等你很久了，快说')
    while True:
        if question=='bye':
            break
        #开始再文件当中查找
        replay=find_answer(question)
        if not replay: #如果回复的是False
            question=input('不知你说啥，你可以问关于订单、物流、账户、支付的问题（退出请输入bye）')
        else:
            print(replay)
            question=input('你还可以问关于订单、物流、账户、支付的问题（退出请输入bye）')
    print('再见')