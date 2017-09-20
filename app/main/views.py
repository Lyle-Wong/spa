# -*- coding=utf-8 -*-

import json

from bson import json_util
from flask import abort, g, jsonify
from flask_restful import Resource


from . import main_api, main
from .models import Navigator


class Navigation(Resource):

    @login_required
    def get(self):
        data = Navigator.objects.all()
        if not data:
            abort(404)
        return jsonify(data)

    def put(self):
        data = Navigator(title='Home', link='/home')
        save_result = data.save()
        print(save_result)

main_api.add_resource(Navigation, 'navigate/')
