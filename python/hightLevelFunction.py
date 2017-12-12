import math
# python中，支持函数式编程，所谓函数式编程，就是能支持在函数的参数中允许传入函数对象：
# 其要求意味着，1-函数必须是作为一个对象；2-函数作为对象，必须可以使用一个变量进行指向，通过变量可以获取到函数这个对象

# 高阶函数，就是在函数的入参中传入了函数对象：
def high_level(x,y,f):
    return f(x) + f(y)

print high_level(8,9,abs)

# 测试：利用add(x,y,f)函数，计算 根号x + 根号y

def add(x,y,f):
    return f(x) + f(y)


def sqrt1(a):
    return pow(a,0.5)

print add(4,16,sqrt1)

# 改进版本：
print add(4,16,math.sqrt)

# python 中的map()函数：map()是python内置的高阶函数，它接收一个函数f和一个list,并把函数f依次作用在list的每个元素上，得到一个新的listb并返回
# 例如：对于list[1,2,3,4,5,6,7,8,9] 可以传入一个函数，使每个元素都做平方后生成新的list
L1 = [1,2,3,4,5,6,7,8,9]
def rooting(x):
    return x*x

print map(rooting,L1)

# 注意，此函数并不会改变原有的list,而是新生成了一个新的list

# 测试：假设用户输入的英文名字不规范，没有按照首字母大写，后续字母小写的规则，请利用map()函数，把一个list（包含若干不规范的英文名字）变成一个包含规范英文名字的list：
    #输入：['adam', 'LISA', 'barT']
    #输出：['Adam', 'Lisa', 'Bart']
# capitalize() 首字母大写，其余全部小写../upper() 全转换成大写../lower() 全转换成小写 /title()  标题首字大写，如"i love python".title()  "I love python"

names = ['adam', 'LISA', 'barT']
def upper_frist(s):
    return s.capitalize()

print map(upper_frist,names)

############################################################################
# 2.0 python中的reduce()函数，也是python内置的高阶函数，reduce()函数接受的参数和map()类似，也是函数f,和一个list,其操作不一样：
# reduce()函数传入的参数中f函数的入参必须接受两个参数

# reduce()函数其实是对与map()函数的补充，传入两个参数，进行迭代式的对list元素进行操作
# reduce()还可以接收第3个可选参数，作为计算的初始值。如果把初始值设为100，计算：
reduce(f, [1, 3, 5, 7, 9], 100)

# 测试：求积公式 输入 [2, 4, 5, 7, 12] 求结果
def f1()
print reduce(f1,[2, 4, 5, 7, 12])


