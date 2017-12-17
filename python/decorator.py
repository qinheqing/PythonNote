# 需要在调用函数的时候增加函数的功能，而又不用改变原来函数
# 例如：需要对某个函数增加功能，方法1，直接改变原来函数，方法二，通过高阶函数封装，返回一个新的函数
def f1(x):
    return x*2

def new_f1(x):
    def fn(f):                                          # 通过包装一层函数fn，在fn函数中调用目标函数之前进行处理
        print 'call'+f._name_+'()'
        return f(x)
    return fn

# 通过装饰器函数，进行增强
# python中的装饰器就是为了简化 装饰器的调用：
@new_f1
def f1(x):
    return x*2

# 以上操作等价于：
def f1(x):
    return x*2
f1 = new_f1(f1)

# 通过函数的装饰器，可以方便的使用函数：
# @log
# @test   
# 等等

# 编写无参数的decorator:在python中decorator本质上就是一个高阶函数，它接受一个函数作为参数，返回一个新的函数：
# 使用@可以避免使用f = decorator(f)
def log(f):
    def fn(x):
        print 'call'+f._name_+'()...'
        return f(x)
    return fn

# 这样的装饰器，由于在函数中定义的是一个入参，在一个参数的方法上使用这个装饰器是没有问题的，但是在多个参数的函数山使用这个
# 装饰器会报错，要自适应的参数，可以使用python中提供的*args 和**kw保证任意个参数总能调用正常;
# 编写一个@performance,可以打印出函数的调用时间：
def performance(f):
    def fn(*args,**kw):
        print "call factorial() in",time.localtime(time.time())
        return f(*args,**kw)
    return fn

# 编写带参数的装饰器：
# 其实是在原来的decorator上再嵌套一层，在原来的高阶函数上再嵌套一层高阶函数，使用最上层的高阶函数处理传入的参数;
def log_in(prefix):
    def log_decorator(f):
        def wrapper(*args,**kw):
            print '[%s]%s()...' %(prefix,f._name_)
            return f(*args,**kw)
        return wrapper
    return log_decorator

@log_in('haha')
def test():
    pass
print test()
