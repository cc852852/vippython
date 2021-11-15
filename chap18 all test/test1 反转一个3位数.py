# 咕噜咕噜的丁丁
# 不浪费一分一秒
# 你可以的
# 时间：2021/11/14 20:49
class Solution:
    #参数number：输入一个3位数
    #返回值：反转后的数字
    def reverseInteger(self,number):
        bai=int(number/100)
        shi=int(number%100/10)
        ge=int(number%10)
        return (ge*100+shi*10+bai)

if __name__ == '__main__':
    solution=Solution()
    num=int(input('请输入一个3位数：'))
    ans=solution.reverseInteger(num)
    print('输入:',num)
    print('输出:',ans)