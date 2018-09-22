#! /usr/bin/env python
# coding=utf-8
__author__ = "ipigzhu"

import datetime, os

class Config(object):
    DEBUG = True
    HOSTNAME = '127.0.0.1'
    PORT = '3306'
    DATABASE = 'flask'
    USERNAME = 'root'
    PASSWORD = '111'
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://%s:%s@%s:%s/%s' % (USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)
    SQLALCHEMY_POOL_SIZE = 5
    SQLALCHEMY_POOL_TIMEOUT = 30
    SQLALCHEMY_POOL_RECYCLE = -1
    # 追踪对象的修改并且发送信号
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SECRET_KEY = 'zj-lili'
    PERMANENT_SESSION_LIFETIME = datetime.timedelta(seconds=3600)

    # SESSION_TYPE = 'redis'  # session类型为redis
    # SESSION_KEY_PREFIX = 'session:'  # 保存到session中的值的前缀
    # SESSION_PERMANENT = True  # 如果设置为False，则关闭浏览器session就失效。
    # SESSION_USE_SIGNER = False  # 是否对发送到浏览器上 session:cookie值进行加密

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # 项目的绝对路径
    UPLOAD_FOLDER = os.path.join(BASE_DIR, 'project/static/upload')
    MAX_CONTENT_LENGTH = 3 * 1024 * 1024  # 只能上传 3M



class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False


'''
默认配置
 {
        'DEBUG':                                get_debug_flag(default=False),  是否开启Debug模式
        'TESTING':                              False,                          是否开启测试模式
        'PROPAGATE_EXCEPTIONS':                 None,
        'PRESERVE_CONTEXT_ON_EXCEPTION':        None,
        'SECRET_KEY':                           None,
        'PERMANENT_SESSION_LIFETIME':           timedelta(days=31),
        'USE_X_SENDFILE':                       False,
        'LOGGER_NAME':                          None,
        'LOGGER_HANDLER_POLICY':               'always',
        'SERVER_NAME':                          None,
        'APPLICATION_ROOT':                     None,
        'SESSION_COOKIE_NAME':                  'session',
        'SESSION_COOKIE_DOMAIN':                None,
        'SESSION_COOKIE_PATH':                  None,
        'SESSION_COOKIE_HTTPONLY':              True,
        'SESSION_COOKIE_SECURE':                False,
        'SESSION_REFRESH_EACH_REQUEST':         True,
        'MAX_CONTENT_LENGTH':                   None,
        'SEND_FILE_MAX_AGE_DEFAULT':            timedelta(hours=12),
        'TRAP_BAD_REQUEST_ERRORS':              False,
        'TRAP_HTTP_EXCEPTIONS':                 False,
        'EXPLAIN_TEMPLATE_LOADING':             False,
        'PREFERRED_URL_SCHEME':                 'http',
        'JSON_AS_ASCII':                        True,
        'JSON_SORT_KEYS':                       True,
        'JSONIFY_PRETTYPRINT_REGULAR':          True,
        'JSONIFY_MIMETYPE':                     'application/json',
        'TEMPLATES_AUTO_RELOAD':                None,
    }
'''
