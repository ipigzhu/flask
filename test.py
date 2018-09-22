#!/usr/bin/env python
# -*- coding:utf-8 -*-

from project import create_app
from project import db

app = create_app()

from flask import url_for
with app.test_request_context():
    print(url_for('login.login', _external=True))
    print(url_for('user.aa'))
    pass



