from flask import Blueprint, jsonify, request
from flask_jwt_extended import JWTManager, create_access_token, get_jwt_identity, jwt_refresh_token_required, \
    create_refresh_token
from web.exceptions.users import *
from web.models import User

from .register import create_register
from ..database import db

auth_bp = Blueprint('login', __name__)


@auth_bp.errorhandler(UserError)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


@auth_bp.route('', methods=['POST'])
def login():
    email = request.json.get('email', None)
    password = request.json.get('password', None)
    if not (email and password):
        raise BadUser
    with db.transaction():
        users = User.select().where(User.email == email)
        if len(users) > 0:
            user = users[0]
            if user is not None and user.check_password(password):
                identity = {"id": user.id, "admin": user.admin}
                response = {'access_token': create_access_token(identity=identity),
                            'refresh_token': create_refresh_token(identity=identity)}
                return jsonify(response), 200
            else:
                raise BadEmailPassword
        else:
            raise BadEmailPassword


@auth_bp.route('/refresh', methods=['POST'])
@jwt_refresh_token_required
def refresh():
    current_user = get_jwt_identity()
    access_token = create_access_token(identity=current_user)
    return jsonify(access_token=access_token), 200


def admin_only(func):
    def success(user):
        me = get_jwt_identity()
        if me and me['admin']:
            return func(user)
        else:
            raise UserNotAdmin

    return success


def create_auth(app):
    jwt = JWTManager(app)
    app.register_blueprint(auth_bp, url_prefix="/auth")
    create_register(app)
