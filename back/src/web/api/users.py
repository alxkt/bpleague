from flask_jwt_extended import jwt_required
from flask_restful import Resource, request
from web.managers.users import UsersManager

from ..config import logger

userManager = UsersManager()


class Users(Resource):
    """
    Manage the users in the database
    """

    @jwt_required
    def get(self):
        """
        Get the list of users in BPLeague
        :return: list of users
        """
        search = request.args.get('search', None)
        logger.debug('Get on /users called. Search : {}'.format(search))
        return userManager.get_all(search=search)


class User(Resource):
    """
    Manage an user in the database
    """

    @jwt_required
    def get(self, user_id):
        """
        Get an user by its id
        :return: the user demanded
        """
        logger.debug('Get on /users/:id called.')
        return userManager.get(user_id)
