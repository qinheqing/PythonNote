# python中的内置数据类型List
# list是python的内置数据类型，是一种有序的集合，可以随时添加或者删除元素
# list 是数学意义上的有序集合，list中的元素是按照顺序排列的[] 括起来的就是一个list对象
mylist = ['zhangsan','lisi','wangwu']
print mylist

# 由于python动态语言的特性，list中的元素不要求同一种类型，一个列表中可以包含多种数据类型
mylist1 = [1,8.8,'haha','test']
print mylist1

# 获取list中的数据,通过索引获取元素：
print mylist[0]
print mylist1[2]

# 倒叙遍历list集合
print mylist[-1]   # 表示最后一个元素

# list集合添加元素，第一种方法是使用list对象的方法append()把新元素追加到list末尾
mylist.append('addSomeItem')

# list 方法insert()方法，接受两个参数，第一个参数是索引，第二个参数是待添加的元素
mylist.insert(0,'insertFrist')
print mylist

# list 中的删除元素的方法，list对象的方法pop()删除列表中的最后一个元素，并且返回删除的元素
print mylist.pop()

# list对象中的pop()方法也可以指定位置删除元素
print mylist.pop(2)

# list中可以直接指定索引替换元素，也可以使用倒序得索引进行替换元素
mylist[-1] = 'change1'
mylist[2] = 'change'
print mylist


print '#########################################################################'
# python中得tuple,python中得另一种有序列表中文翻译为“元组”，其特性和list类似，但是tuple一旦创建，就不能修改
# python使用的创建使用的是()
mytuple = ('admin','manager','boss')

# tuple没有添加元素和插入元素的方法，而获取元素的方式和list是一样的
# tuple中的单个元素,由于（）作为计算中的优先级表示，为了防止出现歧义，单个元素，声明为：
mytuple1 = (1,)

# 可变的tuple，其中表示的是包含的元素指向性不变，指向的元素可以变
mytuple2 = ('a','b',['A','B'])  # 此时tuple中含有三个指向元素，这三个指向元素不会变，但是如果指向的是一个可以变的元素，那么指向的元素是可以变得
mytuple3 = ('a','b',('A','B'))  # 此时所有的指向元素指向的元素都为不可变的元素，则内容不可变


