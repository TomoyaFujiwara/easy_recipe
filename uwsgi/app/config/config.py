import os

from dotenv import load_dotenv

load_dotenv(dotenv_path='.env')


class Config(object):
    """Common configurations
    """
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI')
    SQLALCHEMY_ECHO = False
    JSON_AS_ASCII = False
    JSON_SORT_KEYS = False


class DevelopmentConfig(Config):
    """Development configurations
    """

    DEBUG = True
    SECRET_KEY = "test"
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{user}:{password}@{host}/{database}?charset=utf8'.format(
        **{
            'user': 'root',
            'password': 'mysql_pass',
            'host': 'mysql',
            'database': 'recipe',
        })
    SQLALCHEMY_ECHO = True


class ProductionConfig(Config):
    """Production configurations
    """

    DEBUG = False
    TESTING = False


class TestingConfig(Config):
    """Testing configurations
    """

    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.getenv('TEST_DATABASE_URI')
    PRESERVE_CONTEXT_ON_EXCEPTION = False


app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig
}