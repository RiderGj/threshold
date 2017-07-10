# -*- coding:utf-8 -*-
import sqlutil
from sqlalchemy import and_

# 获取session和数据库表对应的类
session = sqlutil.getSession()
Points = sqlutil.Points
Table = sqlutil.Table
PointVal = sqlutil.PointVal


# 进行数据库操作
# 获取测点的相关信息
def getPointInfo(point):
    pointInfo = session.query(Points).filter(Points.INSTR_NO == point).one()
    return pointInfo


def getValue(point, time):
    value = None
    pointInfo = getPointInfo(point)
    table = pointInfo.table
    comp = pointInfo.component
    isCal = pointInfo.isCalculate
    # 修改要查询的表名
    PointVal.__table__.name = table
    if (isCal == 0):
        print ('该点不参与计算')
        return value
    else:
        result = session.query(PointVal).filter(
            and_(PointVal.INSTR_NO == point, PointVal.dt == time)).one()
        if (comp == 'R1'):
            value = result.R1
        elif (comp == 'R2'):
            value = result.R2
        elif (comp == 'R3'):
            value = result.R3
        else:
            print ('获取分量失败')
    return value


def main():
    print getValue('C4-A04-PL-01', '2017-05-03 16:00:00')


if __name__ == '__main__':
    main()
