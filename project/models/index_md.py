#! /usr/bin/env python
#coding=utf-8
__author__ = "ipigzhu"

from .. import db

import time
from datetime import datetime

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    bir = db.Column(db.DateTime, default=db.func.now())





