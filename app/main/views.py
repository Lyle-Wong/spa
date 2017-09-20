# -*- coding=utf-8 -*-

import json

from bson import json_util
from flask import abort, g, jsonify
from flask_restful import Resource
from flask_security import login_required

from . import main_api, main
from .auth import User
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

class Person(Resource):
    
    def put(self):
        data = User(username='lwang', email='test@test.com', active=False)
        data.hash_password("pwd")
        data.save()

@main.route('api/token')
@login_required
def get_auth_token():
    token = g.user.get_auth_token()
    return jsonify({'token':token.decode('ascii')})


main_api.add_resource(Navigation, 'navigate/')
main_api.add_resource(Person, 'auth/')
