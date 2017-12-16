# 在python中，如果给定一个list或者tuple，可以通过for循环进行遍历集合中的元素
# python中通过for ...in 来完成，python中的for循环不仅可用用在list或者tuple上，还可以作用在任何可迭代的对象上

# 集合指包含一组元素的数据结构：
    # 有序集合list,tuple,str,unicode
    # 无序集合：set
    # 无序集合且有键值对，dict

# 迭代是比较抽象的操作，使用者不需要知道具体如何迭代，只关心这个动作
# python对于集合的索引迭代：
# 当特别业务需要以按照索引的形式进行处理集合的元素的时候，python有专门的函数可以实现：
L = ['A','B','C','D','E','F','G']
for index,name in enumerate(L):
    print index,'-',name

# 通过使用enumerate()函数，实际上把传入的集合列表中的每个元素生成一个tuple，并且把集合元素和索引绑定在一起生成tup
# 通过for循环实际上迭代出来的是一个个tuple
for t in enumerate(L):
    print t

# zip()函数可以把两个list合并成为一个list:
print zip([1,2,3],['a','b','c'])

# 测试：在迭代 ['Adam', 'Lisa', 'Bart', 'Paul'] 时，如果我们想打印出名次 - 名字（名次从1开始)，请考虑如何在迭代中打印出来。
L1 = ['Adam', 'Lisa', 'Bart', 'Paul']
L2 = zip(range(1,5),L1)
for index,name in L2:
    print index,'-',name

# 迭代dict的value,dict本身也是可以迭代的集合，使用for循环迭代dict可以每次获取到dict的key
# dict对象有一个values()的方法，可以把dict转换成包含所有value的list,这样可以迭代获取到value
dict1 = {'admin':22,'lisa':23,'bart':24}
print dict1.values()

# 在dict中还有一个获取values的方法，是itervalues(),这个方法不会直接把dict转换为只包含values的list,每次迭代去取值
# values()方法实际上是把dict转换成了只包含values的list
# 测试：给定一个dict：d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59, 'Paul': 74 }，请计算所有同学的平均分。
d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59, 'Paul': 74 }
print sum(d.values())*1.0/len(d.values())   #事实上，使用len()函数也可以获取dict的长度

# 实际上python3.x已经取消了itervalues

# dict中获取key，values的方法，实际上，可以使用items()方法，此方法把每一个dict的键值对生成一个tuple,变成一个tuple的list,可以方便迭代元素
print d.items()

# 通过这个方法，我们可以对生成的list进行迭代，获取对应的key-values键值对
for key,value in d.items():
    print key,':',value

# 注：Python中串联字符串的操作符有两个，一个是"+"， 一个是",", "+"不能用来串联非字符串，而","可以！而且","还会输出一个空格

# 2.0 python生成列表，当要生成一个list[1,2,3,4,5,6]我们可以使用range(1,6)生成，当需要生成特殊的list时，如果继续使用这个函数生成，则需要迭代处理，较为繁琐
# python中有一个列表生成式：
print [x*x for x in range(1,10)]

# 复杂表达式: 使用for循环可以迭代list，也可以迭代dict,通过和列表生成式，可以进行复杂的操作：
dict2 = {'A':11,'B':22,'C':33,'D':44}
tds = ['<tr><td>%s</td><td>%s</td></tr>'%(name,score) for name,score in dict2.items()]

# 测试：生成表格html显示特殊的标记

d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59 }
def generate_tr(name, score):
    if score > 60:
       return '<tr><td>%s</td><td>%s</td></tr>' % (name, score)
    else:
       return '<tr><td>%s</td><td style="color:red">%s</td></tr>' % (name, score)

tds = [generate_tr(name,score) for name, score in d.iteritems()]
print '<table border="1">'
print '<tr><th>Name</th><th>Score</th><tr>'
print '\n'.join(tds)
print '</table>'

# 生成式后面还可以加上if尽心条件判断：
print [x*x for x in range(1,10) if x%2 == 0]

# 测试，请编写一个函数，它接受一个 list，然后把list中的所有字符串变成大写后返回，非字符串元素将被忽略。
def filter1(strL):
    L = []
    for s in strL:
        if isinstance(s,str):
            L.append(s.upper())

    return L

def filter2(L):
    return [s.upper() for s in L if isinstance(s,str)]

print filter1(['abxk',123,'Ad'])
print filter2(['abxk',123,'Ad'])

# 多层嵌套表达式，for循环可以嵌套，在列表生成器中，也可以使用多层嵌套
print [m+n for m in 'ABC' for n in '123']

# 其写法实际上和下面代码效果是一样的：
L3 = []
for m in 'ABC':
    for n in '123':
        L3.append(m+n)

# 测试：利用 3 层for循环的列表生成式，找出对称的 3 位数。例如，121 就是对称数，因为从右到左倒过来还是 121。
print [str(a)+str(b)+str(c) for a in range(1,10) for b in range(0,10) for c in range(1,10) if a == c]

# 数字版本
print [x for x in range(100,1000) if x/100 ==x%10]

# python中的内置函数sorted()函数可以对list进行排序：
print sorted([1,3,5,4,6,2,8])

# sorted() 也是一个高阶函数，它可以接受一个比较函数来实现自定义排序，比较函数的定义是：传入两个待比较的元素x,y;如果x排在y前面，返回-1
# 如果x应该排在y的后面，返回的是1，如果x和y相等，返回0

# 是实现一个倒叙排列的函数：
def reverse_cmp(x,y):
    if x > y:
        return -1
    elif x < y:
        return 1
    else:
        return 0

print sorted([1,3,5,7,4,3],reverse_cmp)

# sorted()如果不传入函数，默认对传入的两个值，根据ASCII大小进行编码比较大小
# sorted()对字符串进行排序：
print sorted(['bob','ara','paii','sex'])

# 对字符串排序时，有时候忽略大小写排序更符合习惯。请利用sorted()高阶函数，实现忽略大小写排序的算法。
def cmp_ignore_case(s1, s2):
    if s1.lower() > s2.lower():
        return 1
    elif s1.lower() < s2.lower():
       return -1
    return 0

print sorted(['bob', 'about', 'Zoo', 'Credit'], cmp_ignore_case)

