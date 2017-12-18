# python中的模板使用：
# 要先使用一个模板，首先应该使用import关键字进行导入，例如，导入系统自带的模板math
import math

print math.pow(2,0.5)

print math.pi

# 如果我们只希望导入用到的math模板中的某几个函数，而不是所有的函数，可以使用如下语句：
from math import pow,sin,log
# 可以直接使用
print pow(2,10)

# 这样就可以使用pow,sin,log几个方法了
# 导入的模块使用时需要以模块名引用，使用from xxx import ...导入的方法可能会引起名字冲突，可以使用别名
from math import log
from logging import log as Logger  # 这时可以直接使用logger

# 动态的导入模块：
try:
    from cStringIO import StringIO
Except ImportError:
    from StringIO import StringIO

# 安装第三方模块，通常使用python自带的官方管理工具，pip(2.7.9内置的包管理工具)
