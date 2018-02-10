from flask_jwt_extended import jwt_required
from flask_restful import Resource

from web import logger
from web.managers.users import UsersManager

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
        logger.debug('Get on /users called.')
        return userManager.get_all()


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
