from flask import Flask
from flask_cors import CORS

from web.api import register_api
from web.auth import create_auth


def create_app():
    app = Flask(__name__)
    CORS(app, resources={r"*": {"origins": "*"}})

    create_auth(app)

    register_api(app)

    return app
