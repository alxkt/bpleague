import datetime
from peewee import IntegrityError, DoesNotExist

from ..exceptions import *
from ..models import Match
from ..database import db


class MatchsManager:
    MANDATORY_FIELDS = ['playerA', 'playerB', 'playerC', 'playerD', 'scoreAB', 'scoreCD']

    def __init__(self, user_id=None):
        self.db = db
        self.user_id = user_id

    def get_all(self):
        with self.db.transaction():
            matchs_list = []
            for user in Match.select().dicts():
                matchs_list.append(user)
            logger.debug('Get all matchs from db. Number of matchs : {}'.format(len(matchs_list)))
            return matchs_list

    def get(self, id):
        with self.db.transaction():
            try:
                match = Match.get(Match.id == id)
                logger.debug('Get {} match. Response : {}'.format(id, match))
                return match.get_data()
            except DoesNotExist:
                raise MatchError

    def add_match(self, body):
        for field in self.MANDATORY_FIELDS:
            if field not in body.keys():
                raise MatchError

        date = datetime.datetime.now()
        with self.db.atomic():
            try:
                match = Match.create(
                    id_playerA=body['playerA'],
                    id_playerB=body['playerB'],
                    id_playerC=body['playerC'],
                    id_playerD=body['playerD'],
                    issuer=self.user_id,
                    scoreAB=body['scoreAB'],
                    scoreCD=body['scoreCD'],
                    contested=False,
                    date=date
                )
                return match
            except IntegrityError:
                raise MatchError

    def delete_matchs_table(self):
        with self.db.atomic():
            Match.drop_table()
