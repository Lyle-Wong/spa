# -*- coding=utf-8 -*-

import os

base_dir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    """config file"""
    MONGO_URI = 'mongodb://admin:password@localhost'
    MONGO_HOST = 'localhost'
    MONGO_DBNAME = 'spa'
    MONGO_USERNAME = 'admin'
    MONGO_PASSWORD = 'password'

    SECRET_KEY = 'you will never know'
    MAIL_SERVER = 'mail server'
    MAIL_USE_TLS = True

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