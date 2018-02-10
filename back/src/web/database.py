from peewee import PostgresqlDatabase

from .config import config

db = PostgresqlDatabase(
    'bpleague',
    user=config['database'].get('user', 'bpleague'),
    password=config['database'].get('password', 'bpleague'),
    host=config['database'].get('host', 'localhost')
)
