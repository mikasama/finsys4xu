#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = '__mikasama__'


from fastapi import APIRouter, Depends, HTTPException, BackgroundTasks, Request
from requests import Session
from sqlalchemy.orm import Session
from urllib3 import Retry
from typing import List

from financial import crud, schemas
from financial.database import engine, Base, SessionLocal
from financial.models import Wencai


financial_app = APIRouter()

# 创建models中所有映射数据表，database.py中的配置了echo=True，故控制台也会打印相应数据。但不推荐次方案。还是喜欢先建表，再根据表写models。
# Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 根据id获取wencai表数据
@financial_app.get('/get_stock/{stock_id}', response_model=schemas.ReadWencai)
def get_stock(stock_id: int, db: Session = Depends(get_db)):
    db_stock = crud.get_stock(db=db, stock_id=stock_id)
    if not db_stock:
        raise HTTPException(status_code=404, detail='stock not found!')
    return db_stock

# 该接口根据股票名称stockname来查找数据
@financial_app.get('/get_stock_by_name/{stock_name}', response_model=schemas.ReadWencai)
def get_stock_by_name(stock_name: str, db: Session = Depends(get_db)):
    '''
        三个点包含的注释，可以在swagger上展示\n
        __author__ = '__mikasama__'\n
        地址后直接接股票名称stock_name名字即可查询
    '''
    db_stock = crud.get_stock_by_name(db=db, stock_name=stock_name)
    if not db_stock:
        raise HTTPException(status_code=404, detail='stock not found!')
    return db_stock

# 获取问财表所有数据
@financial_app.get('/get_all_stock')  # 加这个，报错，为什么？ response_model=List[schemas.ReadWencai]
def get_all_stocks(db: Session = Depends(get_db)):
    db_all_stocks = crud.get_all_stocks(db=db)
    if not db_all_stocks:
        raise HTTPException(status_code=404, detail='stock not found!')
    return db_all_stocks

# 向wencai表增加数据
@financial_app.post('/create_wencai', response_model=schemas.ReadWencai)
def create_wencai(wencai_data: schemas.CreateWencai, db: Session = Depends(get_db)):
    # 检查数据是否已经存在
    db_wencai_data = crud.get_stock_by_name(db=db, stock_name=wencai_data.stockname)
    if db_wencai_data:
        raise HTTPException(status_code=404, detail='This stock already exist!')
    return crud.create_wencai(db=db, wencai_data=wencai_data)



# # 子应用路由测试数据
# @financial_app.get('/test_api/{ids}')
# def test_api(ids: int):
#     return {"meg": f"ApiRouter run success. {ids}"}