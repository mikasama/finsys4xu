#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = '__mikasama__'


from fastapi import APIRouter, Depends, HTTPException, BackgroundTasks, Request
from requests import Session
from sqlalchemy.orm import Session

financial_app = APIRouter()


# 子应用路由测试数据
@financial_app.get('/test_api/{ids}')
def test_api(ids: int):
    return {"meg": f"ApiRouter run success. {ids}"}