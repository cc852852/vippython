# 咕噜咕噜的丁丁
# 不浪费一分一秒
# 你可以的
# 时间：2021/9/12 17:57
lst=[20,40,10,98,54]
print('排序前的列表：',lst,id(lst))
#开始排序，调用列表对象的sort方法，默认升序
lst.sort()
print('排序后的列表：',lst,id(lst))

#通过指定关键字参数，将列表中的元素尽行降序排序
lst.sort(reverse=True) #reverse=True 表示降序排序，reverse=False 就是升序排序
print(lst)
lst.sort(reverse=False)
print(lst)

print('---使用内置函数sorted()对列表进行排序，将产生一个新的列表对象----')
lst=[20,40,10,98,54]
print('原列表',lst)
#开始排序
new_lst=sorted(lst)
print(lst)
print(new_lst)
desc_list=sorted(lst,reverse=True)
print(desc_list)