# 咕噜咕噜的丁丁
# 不浪费一分一秒
# 你可以的
# 时间：2021/9/15 11:36
s='hello,python'
print('1.',s.isidentifier()) #False
print('2','hello'.isidentifier()) #True
print('3','张三_'.isidentifier()) #True
print('4','张三_1234'.isidentifier()) #True

print('5','\t'.isspace()) #True

print('6','abc'.isalpha()) #True
print('7','张三'.isalpha()) #True
print('8','张三1'.isalpha()) #False

print('9','123'.isdecimal()) #True
print('10','123四'.isdecimal()) #False
print('11','ⅡⅡⅡ'.isdecimal()) #False

print('12','123'.isnumeric()) #True
print('13','123四'.isnumeric()) #True
print('14','ⅡⅡⅡ'.isnumeric()) #True

print('15','123四'.isalnum()) #True
print('16','张三123'.isalnum()) #True
print('17','abc!'.isalnum()) #False