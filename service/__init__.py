from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.restful import Api

from flask.ext.httpauth import HTTPBasicAuth


app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)
api = Api(app)
auth = HTTPBasicAuth()

# Importing after SqlAlchemy object is created to
# avoid circular imports
from resources.users_resource import UsersList

api.add_resource(UsersList, '/users')
