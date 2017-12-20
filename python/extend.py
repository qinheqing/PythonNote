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
