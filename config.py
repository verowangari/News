from distutils.log import debug


# NEWS_API_KEY='26e92efd5ae74abf9827342828a892d9'
class Config(object):
    SECRET_KEY = 'guess-me'
    debug = False
    testing = False
    CSRF_ENABLED = True

class ProductionConfig(Config):
    debug = False
    mail_debug = False


class DevelopmentConfig(Config):
    development = True
    debug = True


class TestingConfig(Config):
    testing = True



