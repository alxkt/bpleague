from flask import redirect, url_for, session, request, jsonify
from flask_jwt_extended import create_access_token, create_refresh_token
from flask_oauthlib.client import OAuth
from werkzeug import security

from ..managers import UsersManager
from ..config import config
from ..database import db
from ..models import User
from ..exceptions.users import NotConnected


def create_oauth(app, auth_bp):
    oauth = OAuth(app)

    viarezo = oauth.remote_app(
        'viarezo',
        consumer_key=config['oauth']['CLIENT_ID'],
        consumer_secret=config['oauth']['CLIENT_SECRET'],
        request_token_params={'scope': 'default', 'state': lambda: security.gen_salt(10)},
        base_url=config['oauth']['base_url'],
        request_token_url=None,
        access_token_method='POST',
        access_token_url=config['oauth']['token_url'],
        authorize_url=config['oauth']['auth_url']
    )

    @auth_bp.route('/login')
    def login():
        auth = viarezo.authorize(config['oauth']['callback_url'])
        return jsonify({'url': auth.location})

    @auth_bp.route('/logout')
    def logout():
        session.pop('viarezo_token', None)
        return jsonify({'msg': 'success'})

    @auth_bp.route('/callback')
    def callback():
        code = request.args.get('code')
        state = request.args.get('state')
        return redirect('http://localhost:8080/#/auth/callback?code={}&state={}'.format(code, state))

    @auth_bp.route('/authorize')
    def authorize():
        resp = viarezo.authorized_response()
        if resp is None or resp.get('access_token') is None:
            return 'Access denied: reason=%s error=%s resp=%s' % (
                request.args['error'],
                request.args['error_description'],
                resp
            )
        session['viarezo_token'] = (resp['access_token'], '')
        me = viarezo.get(config['oauth']['me_path'])
        email = me.data['email']
        with db.transaction():
            users = User.select().where(User.email == email)
            if len(users) > 0:
                user = users[0]
            else:
                manager = UsersManager()
                first_name = me.data['firstName']
                last_name = me.data['lastName']
                user = manager.create_user(email, first_name, last_name)

        identity = {"id": user.id, "admin": user.admin}
        response = {'access_token': create_access_token(identity=identity),
                    'refresh_token': create_refresh_token(identity=identity)}
        return jsonify(response), 200

    @viarezo.tokengetter
    def get_viarezo_oauth_token():
        return session.get('viarezo_token')
