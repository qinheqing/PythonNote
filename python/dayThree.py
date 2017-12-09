# -*- coding: utf-8 -*-
# python中定义的字符串，python中的字符串使用单引号和双引号进行包含起来
# 如果字符串本身包含引号，简单的可以使用单引号，双引号进行包含

print "I'm OK!"
print 'Learn "python" in imooc'

# 如果既有单引号也有双引号的时候，使用python中的转义“\”进行转义

print 'Bob say \"I\'m OK \".'

# 常见的转义字符还有： 
    # \n  表示换行
    # \t  表示一个制表符
    # \\  表示 \ 字符本身

# 练习：打印两行字符串：
print 'Python was started in 1989 by "Guido".'
print 'Python is free and easy to learn.'

print 'Python was started in 1989 by "Guido". \nPython is free and easy to learn.'

# python 中的raw字符串和多行字符串
# 如果字符串中有太多需要转义的字符，都是用转义比较麻烦，可以使用r前缀表示这一行都以字符串输出

print r'\(~_~)/ \(~_~)/'
# r'...'不能表示多行，也不能表示包含单引号或者双引号的字符串
# 表示多行的字符串可以表示为：'''....'''三引号括起来

print ''' line1
line2
line3 '''

# 也可以使用r括起来表示多行
print '''To be, or not to be: that is the question.
Whatever it's noble in the mind to suffer.'''

# 字符串中的编码问题
# 计算机只能处理数值数据，如果需要处理文本，就需要把文本转为数字才可以，最早的计算机中采用8bit进行一个字节
# 一个字节能表示的最大整数为255，0-255被用来表示大小英语字母和数字，符号，这些编码称为ASSCII编码，例如A的编码为65
# 如果要表示中文，显然一个字节不够，至少需要两个字符，而且还要不能与ASCII编码冲突，中国制定了GB2314编码
# 由于多个国家都有自己的一套编码，为了统一多有文字的编码，Unicode应运而生，Unicode通常使用两个字节表示一个字符
# 从前的英文编码从单个字节编程双字节，把最高位全部填为零即可。

# python在Unicode编码中使用u转义：
print u'中文编码'



