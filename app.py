#!/usr/bin/env/ python

from flask import Flask
from flask.ext.login import LoginManager, AnonymousUserMixin, UserMixin

app = Flask(__name__)
app.config['SECRET_KEY'] = '\xc2\xec\xbd\xcf\xa5\xd4\x87\x8e&\xe1\xa2 \xed\xa73\xfe\xf1\xf5\x15* \x93\xcc\x03E'
app.config['DATABASE'] = "web.db"
app.config.from_object(__name__)

wsgi_app = app.wsgi_app

from routeTest import *
from loginmain import *

if __name__ == "__main__":
	import os
	HOST = os.environ.get("SERVER_HOST", "localhost")
	try:
		PORT = int(os.environ.get("SERVER_POST", "5555"))
	except ValueError:
		PORT = 5555
	app.run(HOST, PORT,debug=True)
