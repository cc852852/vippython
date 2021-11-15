# 咕噜咕噜的丁丁
# 不浪费一分一秒
# 你可以的
# 时间：2021/10/19 9:12

def fun():
    num=int(input('请输入一个十进制的整数：')) #将str类型转换成int类型
    print(num,'的二进制数为',bin(num)) #第一种写法 使用了个数可变的位置参数
    print(str(num)+'的二进制数为:'+str(bin(num))) #第二种写法 使用了“+”作为连接符  +的左右均为str类型才行
    print('%s的二进制数为:%s' %(num,bin(num))) #第三种写法，格式化字符串
    print('{0}的二进制数为:{1}'.format(num,bin(num))) #第三种写法，格式化字符串
    print(f'{num}的二进制数为:{bin(num)}') #第三种写法，格式化字符串
    print('------------------------')
    print(f'{num}的八进制数为:{oct(num)}')
    print(f'{num}的十六进制数为:{hex(num)}')

if __name__ == '__main__':
    while True:
        try:
            fun()
            break
        except:
            print('error')

