#!/usr/bin/env python
# -*- coding:utf-8 -*-
from flask import Blueprint
from flask import render_template, redirect, request, url_for, current_app, jsonify
from flask import session, flash, get_flashed_messages
import os, uuid, json

# 首页蓝图
bp_index = Blueprint('index', __name__, url_prefix='/')

from ..forms import UserRegForm
from ..models import User
from .. import db

@bp_index.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        name = request.form.get('uname')
        print(name)

        ck = request.form.getlist('ck')
        print(ck)

        return jsonify({'status': True, 'err_msg': None, 'data': {'num': 88}})
    print(request.method,'---------')
    return render_template('index.html')
