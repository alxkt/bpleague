from peewee import *

from ..database import db


class Match(Model):
    id = PrimaryKeyField()
    id_playerA = IntegerField()
    id_playerB = IntegerField()
    id_playerC = IntegerField()
    id_playerD = IntegerField()
    scoreAB = IntegerField()
    scoreCD = IntegerField()
    issuer = IntegerField()
    date = DateField()
    contested = BooleanField()

    class Meta:
        database = db


db.connect()
Match.create_table(fail_silently=True)
db.close()
