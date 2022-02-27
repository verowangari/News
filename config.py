NEWS_API_KEY='26e92efd5ae74abf9827342828a892d9'
class Config(object):
    SECRET_KEY = 'guess-me'
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True

class ProductionConfig(Config):
    DEBUG = False
    MAIL_DEBUG = False
class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True



