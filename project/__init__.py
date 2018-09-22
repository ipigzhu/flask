#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
这个 init.py 文件，将来需要被外面的 run.py 导入，里面的model.py 视图函数导入
所以所以里面的所有导入动作都要使用相对路径！！
'''

from flask import Flask

# 创建数据库连接对象 db (必须在导入模型之前创建)
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# 导入配置
import settings

# 导入蓝图
blueprints = [
    'project.views.index.bp_index',
]

# 导入模型
from .models import *

def create_app():
    app = Flask(__name__, template_folder='templates',
                static_folder='static', static_url_path='/static')

    app.config.from_object(settings.Config)
    db.init_app(app)

    from werkzeug.utils import import_string
    for bp_name in blueprints:
        bp = import_string(bp_name)
        app.register_blueprint(bp)

    return app
