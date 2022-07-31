#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = '__mikasama__'


from turtle import update
from sqlalchemy import Column, String, Integer, BigInteger, Date, DateTime, ForeignKey, func
from sqlalchemy.orm import relationship

from financial.database import Base


# 创建wencai表model
class Wencai(Base):
    __tablename__ = 'wencai'  # 表名，指的是本类映射到wencai表

    # 指定id映射到id字段，id字段为整型，主键，自动增长，不能为空
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    stockname = Column(String(128), nullable=False, comment='股票名称')
    stockcode = Column(String(128), nullable=False, unique=True, comment='股票代码')
    wencaiscore = Column(String(128), nullable=False, comment='问财打分')
    shortcommnet = Column(String(128), nullable=False, comment='问财短评')
    langcommnet = Column(String(128), nullable=False, comment='问财长评')  # 字段名称要一致，不然连接会出问题 langcommnet表里面字段写错了，就出现该问题，现在这里只好改成错的拼写
    morecontent = Column(String(128), nullable=False, comment='更多信息')

    createtime = Column(DateTime, server_default=func.now(), comment='创建时间')
    updatetime = Column(DateTime, server_default=func.now(), onupdate=func.now(), comment='更新时间')

    # 新版本sqlalchemy已放弃该字段，而是在crud时使用order_by()来灵活操作
    # __mapper_args__ = {"order_by": createtime}  # 按stockname字段正序排序，如果要倒叙，则：stockname.desc()

    # object 基类也存在该方法，这里重写该方法  （这句话抄来的）
    # __repr__方法默认返回该对象实现类的“类名+object at +内存地址”值
    def __repr__(self):
        return f'股票名称：{self.stockname}，股票代码：{self.stockcode}'