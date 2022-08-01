#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = '__mikasama__'


from datetime import date, datetime
from pydantic import BaseModel



# 定义wencai表的数据类型
class CreateWencai(BaseModel):
    stockname: str
    stockcode: str
    wencaiscore: str
    shortcommnet: str
    langcommnet: str
    morecontent: str

class ReadWencai(CreateWencai):
    id: int
    createtime: datetime
    updatetime: datetime

    class Config:
        orm_mode = True