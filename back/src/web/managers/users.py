import re

from peewee import IntegrityError, DoesNotExist
from web.exceptions import *
from web.models import User

from ..database import db


class UsersManager:

    def __init__(self):
        self.db = db

    def get_all(self):
        with self.db.transaction():
            user_list = []
            for user in User.select().dicts():
                user_list.append(user)
            logger.debug('Get all users from db. Number of users : {}'.format(len(user_list)))
            return user_list

    def get(self, id):
        with self.db.transaction():
            try:
                user = User.get(User.id == id)
                logger.debug('Get {} user. Response : {}'.format(id, user))
                return user.get_data()
            except DoesNotExist:
                raise UserNotExisting

    def create_user(self, email, admin=False):
        if re.match(r'^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$', email) is None:
            raise BadEmail
        with self.db.atomic():
            try:
                User.create(
                    first_name='test',
                    last_name='test',
                    email=email,
                    admin=admin
                )
            except IntegrityError:
                raise UserAlreadyRegistered

    def delete_users_table(self):
        with self.db.atomic():
            User.drop_table()
