#!/usr/bin/env python
# -*- coding:utf-8 -*-

from project import create_app
app = create_app()

if __name__ == '__main__':
    app.run(port=88, host='127.0.0.1')
