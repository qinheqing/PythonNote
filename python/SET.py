# Python中的Set
# Python的作用是建立一组key和一组value的映射关系，dict的key是不能重复的，有时候我们需要的是dict的key不重复的特性

# set就是这样的集合：set中的元素没有重复，而且是无序的（这点和Java不一样，Java中的set是有序元素）

# 创建set的方式：s = set(['A','B','c'])
myset = set(['a','b','c','d'])
# 查看set的元素,打印出来的set元素是无序的
print myset

# 由于set是无序的，当我们传入重复的元素时候:
myset1 = set([1,2,2,3,4,5,6,6,7,7])
print myset1   #直接去重

# set的无序性，那么访问获取set就不能使用索引的形式获取值，一般set也是用于某个元素是否在当前的set中
print 5 in myset1

# set的特点1，set内部结构和dict相似，唯一区别是不存在value,因此判断一个元素是否存在set中的速度极快
# set的特点2，set存储的元素和dict类似，必须是不变的对象任何可变的对象不能放在set中
# set的使用场景，比如我们期望用户输入字符串'mon','tue','sun'...可以放入set中，方便判断输入是否是期望的

s = set([('Adam', 95), ('Lisa', 85), ('Bart', 59)])
# set中的key是不可变的量，这key是tuple
# 和遍历dict中的key一样，set可以使用for循环进行遍历：
for tup in s:
    print tup[0],':',tup[1]

# python中的set集合更新，由于set是不重复的元素，如果需要更新set，需要把新的元素添加到set中，并把已有的元素从set中删除
# 可以使用set的add()方法，如果添加的元素在set中已经存在了，不会再重复添加
myset2 = set([1,2,3,4,5,6])
myset2.add(3)
myset2.add(7)
print myset2

# 删除元素的时候，使用的set的remove()方法，如果删除不存在的元素，set会报错，所以，add可以直接添加，remove前需要判断
a = 4
if a in myset2:
    myset2.remove(a)

print myset2

# 针对下面的set，给定一个list，对list中的每一个元素，如果在set中，就将其删除，如果不在set中，就添加进去。
s = set(['Adam', 'Lisa', 'Paul'])
L = ['Adam', 'Lisa', 'Bart', 'Paul']

for listItem in L:
    if listItem in s:
        s.remove(listItem)
    else:
        s.add(listItem)

print s

# 另一种解法：
t = set(L)      # 把这个list转化为set集合，然后遍历set集合，如果set遍历的元素是另一个set中，就删除这个值
for tItem in t:
    if tItem in s:
       t.remove(tItem)

print t


