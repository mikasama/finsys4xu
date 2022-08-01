#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = '__mikasama__'


import uvicorn
from fastapi import FastAPI

from financial import financial_app


# 初始化主应用
myapp = FastAPI(
    title='finsys4xu',
    version='0.1.0',
    description='徐氏大金融系统',
    openapi_url='/openapi.json',
    docs_url='/docs',
    redoc_url='/redoc'
)

# 添加子应用路由，在swagger中将以分类展示
myapp.include_router(financial_app, prefix='/financial', tags=['金融数据服务'])

# 测试数据
@myapp.get('/{ids}')
def test_api_docs(ids: int):
    return {"msg": f"It works {ids}."}


if __name__ == '__main__':
    uvicorn.run('run_server:myapp', host='0.0.0.0', port=9999, reload=True, debug=True,workers=1)