# -*- coding=utf-8 -*-

from flask_script import Manager, Server, Shell

from app import create_app

app = create_app('development')
manager = Manager(app)

def make_shell_context():
    return dict(app=app)

manager.add_command('shell', Shell(make_context=make_shell_context))
manager.add_command('runserver', Server(host='127.0.0.1', port=5000))

if __name__ == "__main__":
    manager.run()
