# 递归算法的python实现
# 在递归思想：递归就是子程序直接调用自己或者通过一系列调用自己完成功能，是一种描述问题和解决问题的基本方法
# 递归的两个要素：
# 	1. 边界条件：确定递归何时终止，也成为递归的出口
# 	2. 递归的模式：大问题是如何分解为小问题进行调用的

# 最基本的递归算法，计算一个整数n的阶乘
def fun_resursion(n):
	if n == 1:
		return 1
	return n * fun_resursion(n - 1)

# 理论优化一、
# 我们在程序中递归的调用每次都需要调用自己，这种行为在计算机中是需要依赖内存结构中的栈数据结构的，
# 每次调用都会压入栈中，如果计算量大，函数调用需要的内存可能会炒出物理内存，发生溢出错误，解决这样问题的方法：
# 通过尾递归优化，事实上，尾递归和循环的效果是一样的，所以可以把循环看做是一种特殊的尾递归函数
def fact(n):
    return fact_iter(n, 1)

def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)

# 计算fact(5)
===> fact_iter(5, 1)
===> fact_iter(4, 5)
===> fact_iter(3, 20)
===> fact_iter(2, 60)
===> fact_iter(1, 120)
===> 120

# 尾递归调用时，如果做了优化，栈不会增长，因此，无论多少次调用也不会导致栈溢出。但是大部分程序并没有对
# 尾递归进行优化，python也没有，使用尾递归也一样会发生溢出

# 优化二：
# 通过查看递归，可以看到许多是被重复计算的数据，可以把每次计算的结果进行保存到hash表中，下次直接获取
# 避免多次重复计算，减少时间复杂度的同时也能减少空间复杂度，这种算法可以成为备忘录算法
def fun_resursion(n):
	noteDict = {}
	if n == 1:
		return 1
	else:
		if noteDict.has_key(n):
			return noteDict[n]
		else:
			value = n * fun_resursion(n - 1)
			noteDict[n] = value
			return value

# 通过记住值，所有值只计算一次，时间复杂度变为了n

# 优化二、通过自底向上的迭代方式进行逆向计算，观察计算过程：
# f(1) = 1
# f(2) = 2 * f(1)   # 此次计算需要依赖的是上一次f(1)的结果
# f(3) = 3 * f(2)	# 此次计算需要依赖的是上一次f(2)的结果      
# f(4) = 4 * f(3)	# ...
# f(5) = 5 * f(4)	# ...
# f(6) = 6 * f(5)	# 依次类推，我们可以简化内存的使用
# f(7) = 7 * f(6)
def fun_resursion(n):
	temp = 0
	if n == 1:
		return 1
	else:
		if noteDict.has_key(n):
			return noteDict[n]
		else:
			value = n * fun_resursion(n - 1)
			noteDict[n] = value
			return value



# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# 经典的递归解决问题方案
# 汉诺塔问题是递归函数的经典应用，它来自一个古老传说：
# 
# 	在世界刚被创建的时候有一座钻石宝塔A，其上有64个金蝶。
# 	所有碟子按从大到小的次序从塔底堆放至塔顶。紧挨着这座塔有另外两个钻石宝塔B和C。
# 	从世界创始之日起，波罗门的牧师就一直在试图把塔A上的碟子移动到C上去，其间借助于塔B的帮助。
# 	每次只能移动一个碟子，任何时候都不能把一个碟子放在比它小的碟子上面。
# 	当牧师们完成这个任务时，世界末日也就到了。 
# 
# 对于汉诺塔问题的求解，可以通过以下3步实现： 
#  （1）将塔A上的(n - 1)个碟子借助C塔先移动到B塔上； 
#  （2）把塔A上剩下的一个碟子移动到塔C上； 
#  （3）将(n - 1)个碟子从B塔借助塔A移动到塔C上。 

# 参数，塔高度，A，B，C三个塔
def Hanio(n,A,B,C):
	if(n == 1):
		move(1,A,C)    # 移动a到c柱子
	else:
		Hanio(n-1,A,C,B)  # 将n-1碟子借助C移动到B
		move(n,A,C)  # 移动A到C
		Hanio(n-1,B,A,C)  # B塔借助A移动到C

def move(n,from,to):
	global i
	print str(from),"--->",str(to)
	i = i + 1


# 这里的递归方法，可以使用动态规划的算法进行优化算法的时间和空间复杂度：
# 例如有题目：
# 	有一座高度是10级台阶的楼梯，从下往上走，每跨一步只能向上1级或者2级台阶。
# 	要求用程序来求出一共有多少种走法。
#	比如，每次走1级台阶，一共走10步，这是其中一种走法。我们可以简写成 1,1,1,1,1,1,1,1,1,1。

# 解析：
# 	1. 每次只走一级台阶
# 	2. 每次只走两级台阶
# 	3. 有走两级和一级的

# 解法1，暴力枚举所有可能，如果枚举出来的可以走法刚好符合，则进行加1
# 解法2，动态规划思想
# 	-.最后一步，只有两种情况，
# 		一个是从第九级台阶到第十级，另一个是从第八级台阶传到第十级台阶
# 		f(10) = f(9) + f(8)

def up_step(n):
	if n == 1:
		return 1
	elif n == 2:
		return 2
	else:
		return up_step(n-1) + up_step(n-2)

# 动态规划中包含三种重要的概念
# 	最优子结构
# 	边界
# 	状态转移公式，解决了问题的每一个阶段和下一个阶段的关系
# 	
# 我们可以得知f(10) = f(9) + f(8) ---f(9)和f(8)是f(10)的最优子结构
# 我们可以得知f(1) = 1，f(2) = 2  ---f(1)和f(2)是问题的边界
# 我们也可得知f(n) = f(n-1) + f(n-2) ---此为阶段和阶段之间的（状态转移方程）

# 而此时使用递归的方式进行数据的计算，那么其实