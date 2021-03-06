# python中的面向对象编程的实现，类的定义：
class Person(object):
    pass

# 类的创建：
xiaoming = Person()

# 类中进行创建实例属性，由于python语言的动态性，对于每一个实例，都可以直接给他们的属性赋值
a1 = Person()
a1.name = 'XiaoMing'
a1.gender = 3

a2 = Person()
a2.name = 'xiaoHong'
a2.school = 'jiangsu'

a1.gender = a1.gender +1 

print a1
print a2

# python中对象的初始化,可以为对象增加一个特殊的初始化方法
class Student(object):
    def __init__(self,name,gender,birth):
        self.name = name
        self.gender = gender
        self.birth = birth

# 创建用户的时候，需要传入参数：
s1 = Student('zhangsan',2,'2017-2-9')

# python中的访问限制。在实例中我们绑定了多个变量，但是有些属性不希望被外部访问，可以对属性进行控制：
# 规则：如果一个属性以双下划线开头（_）,表示属性是私有的，不能被外界访问到
class Person(object):
    def __init__(self, name, score):
        self.name = name
        self.__score = score

p = Person('Bob', 59)

print p.name
try:
    print p.__score

except AttributeError:

    print ('attributeError')
# 但是，如果一个属性以"__xxx__"的形式定义，那它又可以被外部访问了，以"__xxx__"定义的属性在Python的类中被称为特殊属性，有很多预定义的特殊属性可以使用，通常我们不要把普通属性用"__xxx__"定义。

# 由于python动态语言的特性，可以在实例上绑定新的属性，当一个实例既有实例属性，又有类属性的时候，实例属性的优先级比较高
# 实例属性将屏蔽掉类属性的访问，当把实例属性删除之后，访问又可以使用类属性
    # del p1.address  ## 可以删除p1绑定的实例属性

# 一般，建议不要在实例上修改类属性，因为它仅仅绑定了一个新的实例属性

# python中定义实例的方法
# 一个实例的是有属性是以_开头的，无法被外部访问，但可以被内部的方法使用
# 实例方法就是类中定义的函数，它的第一个参数永远是它本身self
class Teacher(object):
    def __init__(self,name):
        self.__name = name

    def get_name(self):
        return self.__name

t1 = Teacher('zhangsan')
print t1.get_name()

class Person(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score
        self.get_grade = lambda: 'A'

p1 = Person('Bob', 90)
print p1.get_grade
print p1.get_grade()

# python在class中定义的实例方法其实也是属性，它实际上是一个函数对象：
# 也就是说，p1.get_grade 返回的是一个函数对象，但这个函数是一个绑定到实例的函数，p1.get_grade() 才是方法调用。
# 而由于方法也是一个属性，那么动态语言可以动态的添加对象的属性，那当然也能动态的添加方法：
# 只是需要用 types.MethodType() 把一个函数变为一个方法：
import types
def fn_get_grade(self):
    if self.score >= 80:
        return 'A'
    if self.score >= 60:
        return 'B'
    return 'C'

class Person(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

p1 = Person('Bob', 90)
p1.get_grade = types.MethodType(fn_get_grade, p1, Person)
print p1.get_grade()
# => A
p2 = Person('Alice', 65)
print p2.get_grade()
# ERROR: AttributeError: 'Person' object has no attribute 'get_grade'
# 因为p2实例并没有绑定get_grade

# python中定义类方法和实例方法：
# 在class定义的都是实例方法，实例方法第一个参数都是实例本身self
class Humen(object):
    count = 0
    @classmethod                # 通过标记@classmethod,将方法绑定到Human上，而区别与实例方法
    def how_many(cls):
        return cls.count
    def __init__(self,name):
        self.name = name
        Humen.count = Humen.count + 1

print Humen.how_many()
h1 = Humen('haha...')
print Humen.how_many()

# 因为是在类上调用，而非实例上调用，因此类方法无法获得任何实例变量，只能获得类的引用。
















