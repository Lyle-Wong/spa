# -*- coding=utf-8 -*-

from flask import Flask
from flask_mongoengine import MongoEngine
from flask_debugtoolbar import DebugToolbarExtension
from flask_httpauth import HTTPBasicAuth
from config import config


debugtool = DebugToolbarExtension()
mongo = MongoEngine()
basic_auth = HTTPBasicAuth()

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

    debugtool.init_app(app)
    mongo.init_app(app)

    from .main import main as main_blueprint

    app.register_blueprint(main_blueprint, url_prefix='/')
    return app
