# -*- coding=utf-8 -*-

import os

base_dir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    
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
    'development': DevelopmentConfig
}