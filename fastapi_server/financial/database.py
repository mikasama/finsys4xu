#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = '__mikasama__'


from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from financial import config


# MySql连接方法 engine = create_engine('mysql+pymysql://user:passwd@192.168.1.1:3306/mydbname')
# PostgreSQL连接方法 engine = create_engine('postgresql://scott:tiger@localhost/mydatabase')
db_url: str = f'mysql+pymysql://{config.db_user}:{config.db_passwd}@{config.db_url}:{config.db_port}/{config.db_name}'  
# db_url: str = 'mysql+pymysql://root:Xu123456@42.193.138.254:3306/test'


engine = create_engine(
    db_url, encoding='utf-8', echo=True  # echo=True表示引擎将用repr()函数记录所有语句及其参数列表到日志
)

# sqlalchemy中，CRUD都是通过会话(session)进行的，所以我们必须要先创建会话，每一个SessionLocal实例就是一个数据库session
# flush()是指发送数据库语句到数据库，但数据库不一定执行写入磁盘；commit()是指提交事务，将变更保存到数据库文件
# 当 expire_on_commit=True 时，commit 之后所有实例都会过期，之后再访问这些过期实例的属性时，SQLAlchemy 会重新去数据库加载实例对应的数据记录。高并发出现性能下降，可尝试设置为false
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False, expire_on_commit=True)

# 创建基本映射类，应该叫实例。用于创建数据库表等，后面均要继承它
Base = declarative_base(bind=engine, name='Base')