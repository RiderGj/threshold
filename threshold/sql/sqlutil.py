# -*- coding:utf-8 -*-
from sqlalchemy import create_engine, String
from sqlalchemy import Integer, Column, DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建数据库的基类
Base = declarative_base()


# 定义表对应的类
# 1.定义DefTableType类
class Table(Base):
    # 表名
    __tablename__ = 'DefTableType'
    # 表结构
    type = Column(Integer, primary_key=True)
    table = Column(String(50))
    describe = Column(String(50))


# 2.定义thresholdpoints类
class Points(Base):
    # 表名
    __tablename__ = 'thresholdpoints'
    # 表结构
    INSTR_NO = Column(String(30), primary_key=True)
    table = Column(String(50))
    component = Column(String(10))
    isCalculate = Column(Integer)


# 3.定义每个测点表T_ZB_*的类
class PointVal(Base):
    # 表名
    __tablename__ = 'T_ZB_EA'
    # 表结构
    INSTR_NO = Column(String(30), primary_key=True)
    dt = Column(DateTime)
    R1 = Column(String(11))
    R2 = Column(String(11))
    R3 = Column(String(11))
    Note = Column(String(20))


# 数据库连接信息
arguments = dict(
    server='127.0.0.1', user='sa',
    password='amon@1991', database='Rider',
    charset='utf8')
engine = create_engine('mssql+pymssql:///', connect_args=arguments)


# 创建session类型
def getSession():
    DB_Session = sessionmaker(bind=engine)
    session = DB_Session()
    return session


# # 1.查询
# table = getSession().query(Table).filter(Table.type == 12).one()
# print ('type:', type(table))
# print ('tableName:', table.table.strip())
# print ('tableDescribe:', table.describe.strip())
