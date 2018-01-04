# -*- conding:utf-8 -*-
# db.py
# 数据库引擎对象
class _Engine(object):            # 私有类，只能提供给
    def __init__(self,connect):
        self._connect = connect    # 创建类的时候传入连接对象
    def connect(self):
        return self._connect

engine = None       # 声明类变量

# 持有数据库连接的上下文对象：
class DBContext(threading.local):   # DBcontext时threadlocal对象，它持有的数据库连接对于每个线程看到的是不一样的，每一线程之间的连接都是相互隔离的
    def __init__(self):
        self.connect = None
        self.transactions = 0
    
    def is_init(self):
        return not self.connect is None

    def init(self):
        self.connect = _lasyConnection()
        self.transactions = 0
    
    def cleanup(self):
        self.connect.cleanup()
        self.connection = None

    def cursor(self):
        return self.connection.cursor()

_dbContext = DBContext()    # 使用

class _ConnectionContext(object):
    def __enter__(self):
        global _db_contex
        self.should_cleanup = False
        if not _db_contex.is_init():
            DBContext()
            self.should_cleanup = True
        return self

    def __exit__(self,exctype,excvalue,traceback):
        global _db_contex
        if self.should_cleanup:
            _db_contex.cleanup()

def connection():
    return _ConnectionContext()

# 定义了enter和exit的对象可以用于with语句，确保在任何情况下exit方法能被执行