# 计算之所能自动化任务，因为它可以自己做条件判断，高级语言当然也会封装计算机的判断流程
# python中的判断语句

age = 18
if age >= 18:
    print 'you age is', age
    print 'adult'

print 'END'

## 注意，python依赖缩进作为代码块的区分，同过缩进表示代码所属于的范围
# if 表达式后面接冒号，表示代码开始，如果在python交互环境下，还需要特别留意缩进，并且在退出缩进的时候需要多敲一行回车
# 可以使用not表示反转
if not age > 20:
    print 'teenager'

# if ...else..的语句
if age >= 18:
    print 'adult'
else:
    print 'teenager'

# 有时候业务比较复杂的时候，一个else不满足的时候，可以使用if...elif...else

if age >= 18:
    print 'adult'
else:
    if age >= 6:
        print 'teenager'
    else:
        print 'kid'

# 以上代码嵌套不好看，不友好，可以使用以下的方式进行多个判断：
if age >= 18:
    print 'adult'
elif age >=6:
    print 'teenager'
elif age >=3:
    print 'kid'
else:
    print 'baby'

## python 中的for循环，list或者tuple表示一个集合，如果想要遍历集合中所有元素，可以使用循环

mylist = ['a','b','c','d']
for name in mylist:             # name是变量for循环中定义的
    print name

# 循环还有一种形式，为while循环，while循环不会迭代元素，它是通过判断表达式控制循环的结束
sum = 0
x = 1
while x < 100:
    sum = sum + x
    x = x + 2
print sum

# 当使用for或者while循环时，如果在循环内直接退出循环，可以使用break语句
while True:
    sum = sum + x
    x = x + 1
    if x > 60:
        break
print sum

# python中的continue继续循环，在循环中，使用break退出当前的循环，使用continue跳过后续代码，执行下次循环
L = [78,67,81,51,43,69,85]
sum = 0.0
for x in L:
    if x < 60:
        continue
    sum = sum + x
print sum

# for 循环的多重循环
for x in [1,2,3,4,5,6,7,8,9]:
    for y in [1,2,3,4,5,6,7,8,9]:
        if x < y:
            print 10*x+y

for x in range(1,9):                #取枚举1-9
    for y in range(x+1,10):         #取y比x至少大于1，一直到10的枚举
        print str(x)+str(y)         #然后使用str返回字符串即可