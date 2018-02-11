import re

from peewee import IntegrityError, DoesNotExist

from ..exceptions import *
from ..models import User
from ..database import db


class UsersManager:

    def __init__(self):
        self.db = db

    def get_all(self, search=None):
        with self.db.transaction():
            user_list = []
            if search is None or search == '':
                query = User.select().dicts()
            else:
                query = User.select().where(
                    (User.first_name.contains(search)) |
                    (User.last_name.contains(search))
                ).dicts()
            for user in query:
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

    def create_user(self, email, first_name, last_name, admin=False):
        if re.match(r'^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$', email) is None:
            raise BadEmail
        with self.db.atomic():
            try:
                user = User.create(
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                    admin=admin
                )
                return user
            except IntegrityError:
                raise UserAlreadyRegistered

    def delete_users_table(self):
        with self.db.atomic():
            User.drop_table()
