#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = '__mikasama__'


from pyexpat import model
from sqlalchemy.orm import Session

from financial import models, schemas


# 根据id查找wencai表数据
def get_stock(db: Session, stock_id: int):
    return db.query(models.Wencai).filter(models.Wencai.id == stock_id).first()

# 根据股票名称stockname来查找数据
def get_stock_by_name(db: Session, stock_name: str):
    return db.query(models.Wencai).filter(models.Wencai.stockname == stock_name).first()

# order_by(models.Wencai.id) 按字段正序排序，前面加-则是倒叙
def get_all_stocks(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Wencai).order_by(-models.Wencai.id).offset(skip).limit(limit).all()

# def get_all_stocks(db: Session):
#     return db.query(models.Wencai).order_by(-models.Wencai.id).all()

# 新增wencai表数据操作
def create_wencai(db: Session, wencai_data: schemas.CreateWencai):
    db_wencai_data = models.Wencai(**wencai_data.dict())
    db.add(db_wencai_data)
    db.commit()
    db.refresh(db_wencai_data)
    return db_wencai_data