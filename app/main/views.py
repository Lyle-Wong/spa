# -*- coding=utf-8 -*-

import json

from flask_restful import Resource

from . import main_api


class TestApi(Resource):

    def get(self):
        data = {'result':'return_data'}
        return data

main_api.add_resource(TestApi, 'api/')
