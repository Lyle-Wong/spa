# -*- coding=utf-8 -*-

from flask import Flask
from flask_pymongo import PyMongo

from config import config


pymongo = PyMongo()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Headers',
                             'Content-Type,Authorization')
        response.headers.add('Access-Control-Allow-Methods',
                             'GET,PUT,POST,DELETE')
        return response

    pymongo.init_app(app)

    from .main import main as main_blueprint

    app.register_blueprint(main_blueprint, url_prefix='/')
    return app
