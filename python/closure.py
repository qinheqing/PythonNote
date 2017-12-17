# python中的闭包
# 在函数内部定义的函数和外部定义的函数是一样的，只是内部定义的函数在外部无法被访问
def g():
    print 'function name is g()...'
    def f():
        print 'inner function name is f()...'
    return g

# 通过以上的这个代码，使得只能通过g()内部使用f函数，外部无法使用
# 内层函数引用了外层函数的变量（参数也算是局部变量），然后返回内层函数的情况，称为闭包
# 其特点是返回的函数还引用了外层函数的局部变量，所以要正确使用闭包，要确保引用的局部变量在函数返回之后不能变de
def add_out(lst):
    def lazy_add():
        return sum(lst)      # 引用了外层的变量
    return lazy_add


def count():
    fs = []
    for i in range(1, 4):
        def f(m = i):
            return m*m
        fs.append(f)
    return fs

f1, f2, f3 = count()
print f1(), f2(), f3()

# 方法：问题的产生是因为函数只在执行时才去获取外层参数i，若函数定义时可以获取到i，问题便可解决。
# 而默认参数正好可以完成定义时获取i值且运行函数时无需参数输入的功能，所以在函数f()定义中改为f(m = i),函数f返回值改为m*m即可.

# 高阶函数中的匿名函数：为了方便高阶函数中的接受函数作为形参，有时候我们不必要显示的定义函数，直接使用匿名函数更方便
# 匿名函数： lambda x: x*x 关键字lambda 冒号前面的是参数，匿名函数还有个限制，就是只能有一个表达式，不写return
print map(lambda x: x*x,[1,2,4,5,6,8])

