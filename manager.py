#! /usr/bin/env python
# coding=utf-8
__author__ = "ipigzhu"

from project import create_app, db
from flask_script import Manager

app = create_app()
manager = Manager(app)

from flask_migrate import Migrate, MigrateCommand

migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()

'''
    需要在命令行执行

    帮助
    python manager.py -?

    第一种功能：
    启动服务器群
    python manager.py runserver -p 80


    第二种功能：
    想Django一样同步数据库
    python manager.py db init
    python manager.py db migrate
    python manager.py db upgrade

    细节看《001 笔记.wps》
'''
