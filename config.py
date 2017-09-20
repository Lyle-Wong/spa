# -*- coding=utf-8 -*-

import os

base_dir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    """config file"""
    # MONGODB_URI = 'mongodb://admin:password@127.0.0.1:27017/spa'
    MONGODB_HOST = '127.0.0.1'
    MONGODB_DB = 'spa'
    MONGODB_PORT = 27017
    # MONGODB_USERNAME = 'lwang'
    # MONGODB_PASSWORD = 'password'

    SECRET_KEY = 'you will never know'
    MAIL_SERVER = 'mail server'
    MAIL_USE_TLS = True

    TOKEN_EXPIRATION = 600

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False

config = {
    'development': DevelopmentConfig,
    'default':ProductionConfig
}