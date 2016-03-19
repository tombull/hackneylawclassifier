"""Create and configure the Flask server."""

from flask import Flask
from settings import DEBUG
from flask_restful import Api

app = Flask(__name__)

app.debug = DEBUG

api = Api(app)

from app import api_methods
