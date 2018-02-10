import logging


class FlaskConfig(object):
    DEBUG = True
    TESTING = False
    SECRET_KEY = 'testtesttesttest'


flask_config = FlaskConfig
logger = logging.getLogger()
handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)

logger = logging.getLogger('bpleague')

version = '0.1.0'
