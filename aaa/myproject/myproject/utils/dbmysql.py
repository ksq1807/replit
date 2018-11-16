# coding=utf-8
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import text
import config
from sqlalchemy import create_engine

# 配置文件中读取连接串
DB_URI = config.Mysql.url
# echo:回声 默认为False，如果为true，连接被拉扯，并从池检索将被记录到标准输出，以及池大小信息
# pool_size:池的大小
# pool_recycle:设置回收池，当池使用超过特定时间后自动关闭连接
engine = create_engine(DB_URI, echo=False, pool_size=10, pool_recycle=60)


# 插入，修改，删除操作 单条数据
def query(sql):
    # 创建DBSession类型:  用于创建程序与数据库之间的会话
    DB_Session = sessionmaker(bind=engine)
    # 创建session对象:
    DB = DB_Session()
    try:
        # 执行sql语句
        DB.execute(sql)
        DB.commit()
        return True
    except Exception as ex:
        print("exec sql got error:%s" % (ex))
        DB.rollback()
        return False
    finally:
        DB.close()


# 插入，修改，删除操作   多条数据
def query_many(sql):
    # 创建DBSession类型:
    # 创建数据库与程序之间的会话
    DB_Session = sessionmaker(bind=engine)
    # 创建session对象:
    DB = DB_Session()
    try:
        # 执行sql语句
        for item in sql:
            DB.execute(item)
        DB.commit()
        return True
    except Exception as ex:
        print("exec sql got error:%s" % (ex))
        DB.rollback()
        return False
    finally:
        DB.close()


# 查询第一条数据
def first(sql):
    # 创建DBSession类型:
    DB_Session = sessionmaker(bind=engine)
    # 创建session对象:
    DB = DB_Session()
    try:
        # 执行sql语句，.first  session对象返回第一条数据
        rs = DB.execute(sql).first()
        DB.commit()
        return rs
    except Exception as  ex:
        print("exec sql got error:%s" % (ex))
        DB.rollback()
        return False
    finally:
        DB.close()


# 查询多条数据
def fetchall(sql):
    # 创建DBSession类型:
    DB_Session = sessionmaker(bind=engine)
    # 创建session对象:
    DB = DB_Session()
    try:
        # 执行sql语句,.fetchall  session对象返回全部数据
        rs = DB.execute(sql).fetchall()
        DB.commit()
        return rs
    except Exception as ex:
        print("exec sql got error:%s" % (ex))
        DB.rollback()
        return False
    finally:
        DB.close()
