class Config(object):
    """Base config, uses staging database server."""
    DEBUG = False
    TESTING = False
    APP_WEATHER_KEY = '1508a9a4840a5574c822d70ca2132032'


class ProductionConfig(Config):
    FLASK_ENV = 'PROD'


class DevelopmentConfig(Config):
    DEBUG = True
    FLASK_ENV = 'DEV'


class TestingConfig(Config):
    DEBUG = True
    FLASK_ENV = 'TESTING'
