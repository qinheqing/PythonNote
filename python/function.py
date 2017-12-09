# python的内置函数，要调用一个函数，需要知道函数的名称和参数，查询python的内置函数，可以使用help(函数名)进行查看函数的信息
# 调用python的内置函数
temp = abs(-34)
print temp

# 调用函数的时候，如果传入的参数不对，会报错typeError；如果传入的参数和函数的参数类型不匹配，也一样会报同样错误

# 比较函数cmp(x,y)
result = cmp('abc',8)
print result

# python还内置有常用的函数包含数据类型的转换函数，比如int()函数可以把其他数据类型转为整数
num = int('2345')
print num

# str()函数可以把其他类型转为str