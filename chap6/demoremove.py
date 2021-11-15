# 咕噜咕噜的丁丁
# 不浪费一分一秒
# 你可以的
# 时间：2021/9/12 17:23
lst=[10,20,30,40,50,60,30]
print(id(lst))
lst.remove(30) #从列表中移除一个元素，如果有重复元素只移除第一个元素
print(lst,id(lst))
#lst.remove(100)

#pop 根据索引移除元素
lst.pop(1)
print(lst)
#lst.pop(5)#pop index out of range 如果指定的所以不存在，将抛出异常
lst.pop() #如果不指定参数，将删除列表中最后一个元素
print(lst)
print('---切片操作，删除至少一个元素，将产生一个新的列表对象----')
new_lst=lst[1:3]
print('原列表：',lst,id(lst))
print('新列表',new_lst,id(new_lst))
'''不产生新的列表对象，而是删除原列表中的内容'''
lst[1:3]=[]
print(lst)

'''清除列表中的左右元素'''
lst.clear()
print(lst)
'''del 语句将列表对象删除'''
del lst

print(lst)