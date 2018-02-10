from flask import Blueprint, request, jsonify

from web.exceptions.users import *
from web.managers import UsersManager

register_bp = Blueprint('register', __name__)


@register_bp.errorhandler(UserError)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


@register_bp.route('', methods=['POST'])
def register():
    body = request.json
    if 'email' not in body.keys():
        raise BadUser
    elif 'password' not in body.keys():
        raise BadUser
    else:
        email = body['email']
        password = body['password']
        manager = UsersManager()
        manager.create_user(email, password)
        return jsonify({'msg': 'success'})


def create_register(app):
    app.register_blueprint(register_bp, url_prefix="/auth/register")
    logger.debug('Register blueprint successfully registered.')
