#! /usr/bin/env python
# coding=utf-8
__author__ = "ipigzhu"

from wtforms import Form
from wtforms.fields import simple
from wtforms import validators
from wtforms import widgets


class UserRegForm(Form):
    name = simple.StringField(
            label='用户名',
            widget=widgets.TextInput(),
    )
    xxx = simple.StringField(
            label='测试字段',
            widget=widgets.TextInput(),
    )
