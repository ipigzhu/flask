#!/usr/bin/env python
# -*- coding:utf-8 -*-

from project import create_app
from project import db

app = create_app()
with app.app_context():
    db.create_all()
    # db.drop_all()
    pass


'''
作用:
    不想执行 python manager.py db migrate 这样的方式同步数据的
    就和普通的sqlalchemy同步数据库一模一样


因为配置信息在 Flask 对象中，SQLAlchemy想要读取配置信息，需要在 Flask 上下文读取
这个文件是 “离线脚本” 所以需要手工推送app到 LocalStack 中
'''
