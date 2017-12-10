import math
# python的内置函数，要调用一个函数，需要知道函数的名称和参数，查询python的内置函数，可以使用help(函数名)进行查看函数的信息
# 调用python的内置函数
temp = abs(-34)
print temp

# 调用函数的时候，如果传入的参数不对，会报错typeError；如果传入的参数和函数的参数类型不匹配，也一样会报同样错误

# 比较函数cmp(x,y)
result = cmp('abc',8)
print result

# python还内置有常用的函数包含数据类型的转换函数，比如int()函数可以把其他数据类型转为整数
num = int('2345')
print num

# str()函数可以把其他类型转为str
# sum()函数接受一个list作为参数，并返回list所有元素之和。请计算 1*1 + 2*2 + 3*3 + ... + 100*100。
i = 1;
tlist = []
while i < 101:
    tlist.append(i*i)
    i = i + 1

countStr = str(sum(tlist))
print countStr

# python的函数编写
# 在python中，定义一个函数需要使用def关键字进行定义，依次写入 【函数名】【括号】【参数和冒号：】，在缩进块中编写函数体，函数的返回语句return
# 示例定义一个求绝对值的函数
def my_abs(x):
    if x >= 0:
        return X
    else:
        return -x

# 如果函数没有写return ，默认会返回None, return None可以简写为return
test = my_abs(-6)
print test

# 测试：请定义一个 square_of_sum 函数，它接受一个list，返回list中每个元素平方的和。
def square_of_sum(a_list):
    acount = 0
    for item in a_list:
        acount = item*item + acount
    return acount

# 优化写法：
def square_of_sum1(L):
    return sum([i*i for i in L])

test_list = [2,3,4]
sum_my = square_of_sum(test_list)
print sum_my

# Python函数的返回值：特点是可以返回多个值
# Python在返回多个值本质上还是一个值，其返回值是一个tuple，语法上返回一个tuple可以省略括号，而多个变量同时接收一个tuple
# 按位置赋值给对应的值，Python的函数返回值就是一个tuple，写起来看上去是多个值

# 测试：一元二次方程的定义是：ax² + bx + c = 0，请编写一个函数，返回一元二次方程的两个解。
#   注意：Python的math包提供了sqrt()函数用于计算平方根。
def getResult(a,b,c):
    t = b*b -4*a*c
    if t < 0:
        return
    elif t == 0:
        return -b/(2*a)
    else:
        return (math.sqrt(t)-b)/(2*a),-(math.sqrt(t)-b)/(2*a)

# Python的递归函数
# 在函数内部，可以直接调用其他的函数，如果在一个函数内调用自己，则函数为递归函数，举个栗子：
# 计算阶乘：n! = 1*2*3*4...*n  = fact(n-1)*n
def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)

# 这种递归的函数，需要不断在内存中创建匿名变量，接受上层函数返回的值，递归需要一个结束条件
print fact(100)

# 在计算机中，函数的调用是通过栈（stack）这种数据结构实现的，每进行一次函数调用，栈就会push一层栈帧，每当函数返回值时，
# 栈就会减少一个栈层，内存中的值就会被推出返回，变量中的值清空，所以在使用递归的时候，一定需要注意栈溢出的问题
# 测试： 汉诺塔的移动-有A,B,C三根针，将A针上N个从小到大叠放的盘子移动到C针，一次只能移动一个，不重复移动，小盘子必须在大盘子上面。

# 递归的核心思想，把大象放到冰箱--> 永远只有三步骤：打开冰箱，放到冰箱中，关上冰箱
# 递归的思想时要放弃细节，只需要关注递归两层之间的交换+递归的总结条件即可
def removie(n,a,b,c):
    if n == 1:
        print a,'-->',c
        return
    removie(n-1,a,c,b)   #把n-1的塔，
    print a,'-->',c
    removie(n-1,b,a,c)

# python定义默认参数：
# python定义函数的时候，可以使用默认参数，如python自带的int()函数，其函数有两个，使用的时候可以使用传一个或者两个参数
print int('123',8)  #第二个参数时转换进制，如果不传，默认十进制

# 使用默认参数可以简化调用，方便一些场景的使用
def power(x,n=2):    #可以把不传值得调用默认赋值为2
    s = 1
    while n > 0:
        n = n-1
        s = s*x
    return s

# 函数的参数按左到右的顺序匹配，所以默认的参数只能定义在必传参数的后面

# 定义函数可变参数：如果让一个函数接受任一多个参数，我们可以定义一个可变参数：
def MyFun(*args):
    print args

print MyFun('a','b','c','d')
# 事实上，python的解释器把传入的可变参数组装成一个tuple保存，在函数内部，可变参数可看作为tuple
# 例如我们可以定义一个计算任何个数的平均值，可以定义一个可变参数
def averages(*args):
    length = len(args)
    acounts = 0
    for x in args:
        acounts = acounts + x
    return acounts/length

# 优化版本：
def averages1(*args):
    if args:
        return sum(args)*1.0/len(args)
    else:
        return 0.0

print averages(1,2,3,4,5,6,7,8,9)

