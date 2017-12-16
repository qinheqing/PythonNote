# python的函数不仅可以返回list,str,list,dict等数据，还可以返回一个函数：
# 其思想是python的函数本身就是一个对象，那么，一个函数返回一个对象是没有什么问题的：
def f():
    print 'call f()...'
    # 定义一个函数：
    def g():
        print 'my name is g()...'
    return g

print f()

#返回一个函数，可以把一些计算延迟进行，例如：
def calc_sum(lst):
    return sum(lst)

print calc_sum([1,2,43,5])

# 如果返回一个函数，可以延迟计算：
def calc_sum1(llst):
    def lazy_sum():
        return sum(llst)
    return lazy_sum

f = calc_sum1([1,3,45,6,8,9])
print f()