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
