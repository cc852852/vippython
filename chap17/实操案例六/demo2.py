# 咕噜咕噜的丁丁
# 不浪费一分一秒
# 你可以的
# 时间：2021/11/2 21:07
lst=[]
for i in range(0,5):
    goods=input('请输入商品编号和商品名称进行商品入库，每次只能输入一件商品：')
    lst.append(goods)
for item in lst:
    print(item)

cart=[]
while True:
    num=input('请输入要购买的商品编号：')
    for item in lst:
        if item.find(num)!=-1:
            cart.append(item)
            break
    if num=='q':
        break
print('购物车的商品有：')
#for m in cart:
    #print(m)
for m in range(len(cart)-1,-1,-1):
    print(cart[m])
