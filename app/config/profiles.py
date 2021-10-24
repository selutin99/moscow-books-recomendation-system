import os


class Config:
    # Application settings
    DEBUG = True

    # ORM
    SECRET_KEY = os.urandom(32)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SESSION_TYPE = 'sqlalchemy'

    JSON_AS_ASCII = False
    JSONIFY_PRETTYPRINT_REGULAR = True


class ProdConfig(Config):
    def __str__(self):
        return 'ProdConfig'

    FLASK_ENV = 'production'
    DEBUG = False
    TESTING = False

    # Database
    MYSQL_USER = os.environ.get('MYSQL_USER')
    MYSQL_PASSWORD = os.environ.get('MYSQL_PASSWORD')
    MYSQL_URL = os.environ.get('MYSQL_URL')
    MYSQL_DB = os.environ.get('MYSQL_DB')


class DevConfig(Config):
    def __str__(self):
        return 'DevConfig'

    FLASK_ENV = 'development'
    DEBUG = True
    TESTING = False

    # Database
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = 'password'
    MYSQL_URL = 'localhost'
    MYSQL_DB = 'moscow_books'
