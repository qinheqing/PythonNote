# python中的继承
# python中的class都是继承至object
# 继承时，把新的属性加上，一定要记得使用__init__(self,xx,xx)方法进行初始化父类的属性
# 函数super(Student,self)将返回当前类继承的父类，即Person,然后调用__init__()方法，注意self参数已在super()中传入，在__init__()中将隐式传递，不需要写出（也不能写）。

class Person(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

class Teacher(Person):

    def __init__(self, name, gender, course):
        super(Teacher,self).__init__(name,gender)    # 初始化父类属性
        self.course = course

t = Teacher('Alice', 'Female', 'English')
print t.name
print t.course

# python中判断类型，判断某一个变量的类型是否属于某一个类：

class Person(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

class Student(Person):
    def __init__(self, name, gender, score):
        super(Student, self).__init__(name, gender)
        self.score = score

class Teacher(Person):
    def __init__(self, name, gender, course):
        super(Teacher, self).__init__(name, gender)
        self.course = course

p = Person('Tim', 'Male')
s = Student('Bob', 'Male', 88)
t = Teacher('Alice', 'Female', 'English')

print isinstance(p, Person)
True    # p是Person类
print isinstance(p, Student)
False   # p不是Student类型
print isinstance(p, Teacher)
False   # p不是Teacher类型

print isinstance(s, Person)
True    # s是Person类型
print isinstance(s, Student)
True    # s是Student类型
print isinstance(s, Teacher)
False   # s不是Teacher类型

# 一个父类的实例不能是子类类型，因为子类比父类多了一些属性和方法。
# 在一条继承链上，一个实例可以看成它本身的类型，也可以看成它父类的类型。

# 类有继承的关系，并且子类类型可以向上转型看成时父类类型，如果，一个Peron派生出了Student和teacher,并且都实现了一个方法whoAmI()
class Person(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
    def whoAmI(self):
        return 'I am a Person, my name is %s' % self.name

class Student(Person):
    def __init__(self, name, gender, score):
        super(Student, self).__init__(name, gender)
        self.score = score
    def whoAmI(self):
        return 'I am a Student, my name is %s' % self.name

class Teacher(Person):
    def __init__(self, name, gender, course):
        super(Teacher, self).__init__(name, gender)
        self.course = course
    def whoAmI(self):
        return 'I am a Teacher, my name is %s' % self.name

# 那么，在一个函数中，函数对象中，定义一个方法接收变量x
def who_am_i(x):
    print x.whoAmI()

p = Person('name','male')
s = Student('Bon','Male',18)
t = Teacher('Alice','female','english')

who_am_i(p)
who_am_i(s)
who_am_i(t)

# 在函数中，方法调用将在x的实际类型上，调用者总是先查找自身的定义，如果没有定义，则将顺着继承链向上查找，直到在某个父类中找到为止
# 而且，在动态语言中，传入的x不管作为任何类型的实例，只要有whoAmI方法即可进行调用

# 示列： Python提供了一个open函数对打开一个磁盘文件，并且返回File对象，File对象有一个read()方法可以读取文件内容
# 而由于动态语言的特性，任何对象，只要实现了read()方法，都可以传入json.load()进行调用对象的read()方法
class Students(object):

    def __init__(self, lists):
        self.lists = lists

    def read(self):
        return self.lists

s = Students('["Tim", "Bob", "Alice"]')

print json.load(s)

# 这就是python的多态性，需要注意和Java语言中的堕胎区分，其中的区别在于类的不限制性

# python中的多重继承，除了从一个父类继承之外，python可以从多个父类继承，称为多重继承