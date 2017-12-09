# python中的list和tuple可以表示顺序集合，但是当需要表示关联关系的数据时，虽然可以使用两个list表示，但是不方便取值
# python中使用dict表示 键=值 对这样的数据，python中通过key（键）获取到对应的值

# python中使用dict: 使用{}花括号表示创建dict
mydict = {
    'admin':888,
    'guess':777,
    'haha':666
}

# dict可以使用len(mydict) 获取dict的长度
print mydict['admin']

# 如果key中没有对应的值，会报错，可以取值之前先判断下：
if 'admin' in mydict:
    print mydict['admin']

# 使用dict的get方法，当key不存在的时候，返回None:
print mydict.get(2)
print mydict.get('guess')
print len(mydict)

d = {
    'Adam': 95,
    'Lisa': 85,
    'Bart': 59
}
print 'Adam:',d['Adam']     # print这个打印动作，连接字符串，使用逗号进行隔开
print 'Lisa:',d['Lisa']
print 'Bart:',d['Bart']

# dict的特点时查询速度极快，无论dict有10个元素或者10万个元素，查询速度都一样，相对list查询随着元素的增长，查询时间不断增长
# dict相对的付出也是内存占用大的问题，dict第二个特点是存储key-value序是没有顺序的
mydic1 = {
    'Adam': 95,
    'Lisa': 85,
    'Bart': 59
}
print mydic1        # 打印出来的顺序不是我们创建数据是保存的顺序

# dict的第三个特点是作为key的元素必须是不可变的，python的基本数据类型如字符串，整数，浮点数都是不可变的，都可以作为key
# 常用的还是str作为key

## python更新dict,dict是可变的，意味着我们是可以随时往dict中添加key-value的
# 赋值语句dict[key] = 值：如果key已经存在，这会把key对应的值覆盖掉
mydict['add'] = 99
mydict['Adam'] = 66
print mydict

# Python遍历dict
# 由于python中的dict也是一个集合，遍历dict和list类似，都可以通过for循环
for key in mydict:
    print key

for key in mydic1:
    print key,':',mydic1.get(key)   # 使用for循环可以获取key列表，再通过key获取对用的value







