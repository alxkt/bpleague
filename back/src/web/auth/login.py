from flask import Blueprint, jsonify
from flask_jwt_extended import JWTManager, create_access_token, get_jwt_identity, jwt_refresh_token_required

from ..exceptions.users import *
from .oauth import create_oauth

auth_bp = Blueprint('login', __name__)


@auth_bp.errorhandler(UserError)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


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
    create_oauth(app, auth_bp)
    app.register_blueprint(auth_bp, url_prefix="/auth")
