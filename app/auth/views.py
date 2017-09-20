# -*- coding=utf-8 -*-
from flask import g, request, abort, jsonify

from . import auth
from models import User

from app import http_auth

@auth.route('/users', methods=['POST'])
def new_user():
    username = request.json.get('username')
    password = request.json.get('password')
    if username is None or password is None:
        abort(400)
    try:
        User.obejcts.get(username=username)
        abort(400)
    except User.DoesNotExist:
        user = User(username=username)
        user.hash_password(password)
        user.save()
    return jsonify({'username':user.username})

@app.route('/users/<id>')
def get_user(id):
    user = User.objects.get(id)
    if not user:
        abort(400)
    return jsonify({'username':user.username})


@app.route('/token')
@http_auth.login_required
def get_auth_token():
    token = g.user.get_auth_token()
    return jsonify({'token':token.decode('ascii')})
