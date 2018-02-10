import os

from peewee import PostgresqlDatabase

db = PostgresqlDatabase(
    'bpleague',
    user='bpleague',
    password=os.environ.get('POSTGRES_PASSWORD', 'bpleague'),
    host=os.environ.get('POSTGRES_HOST', 'localhost')
)
