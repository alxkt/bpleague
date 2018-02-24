import datetime
from peewee import IntegrityError, DoesNotExist

from ..exceptions import *
from ..models import Match
from ..database import db


class MatchsManager:
    MANDATORY_FIELDS = ['playerA', 'playerB', 'playerC', 'playerD', 'scoreAB', 'scoreCD']

    def __init__(self, user_id=None):
        self.db = db
        self.db.connect(reuse_if_open=True)
        self.user_id = user_id

    def __del__(self):
        self.db.close()

    def get_all(self):
        matchs_list = []
        for match in Match.select().dicts():
            matchs_list.append(match)
        logger.debug('Get all matchs from db. Number of matchs : {}'.format(len(matchs_list)))
        return matchs_list

    def get(self, id):
        try:
            match = Match.get(Match.id == id)
            logger.debug('Get {} match. Response : {}'.format(id, match))
            return match.get_data()
        except DoesNotExist:
            raise MatchError('Get not possible.')

    def add_match(self, body):
        for field in self.MANDATORY_FIELDS:
            if field not in body.keys():
                raise MatchError('{} is missing from body.'.format(field))

        if 'date' not in body.keys():
            body['date'] = datetime.datetime.now()
        with self.db.atomic():
            try:
                match = Match.create(
                    playerA=body['playerA'],
                    playerB=body['playerB'],
                    playerC=body['playerC'],
                    playerD=body['playerD'],
                    issuer=self.user_id,
                    scoreAB=body['scoreAB'],
                    scoreCD=body['scoreCD'],
                    contested=False,
                    date=body['date']
                )
                return match
            except IntegrityError:
                raise MatchError('Match already created.')

    def delete_matchs_table(self):
        with self.db.atomic():
            Match.drop_table()

    def delete_matchs(self, id):
        try:
            match = Match.get(Match.id == id)
            logger.debug('Get {} match. Response : {}'.format(id, match))
            return match.get_data()
        except DoesNotExist:
            raise MatchError('Can\'t delete match.')
