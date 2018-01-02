# python中我们把很多函数分组，分别放在不同的文件了，通过文件进行组织代码
# 在python中，一个.py文件就成为一个模块Module
# 使用模块可以方便的引用，避免变量名称冲突
# 为了使模块名称也不冲突，python使用目录来组织模块，成为包
# --mycompany
# ---- __init__.py
# ----abc.py
# ----xyz.py

# abc.py模块的名称变成了mycompany.abc.py
# 每个模块中都包含一个init文件，作为python包的标志
# __init__.py本身就是一个模块，而它的模块名就是mycompany。