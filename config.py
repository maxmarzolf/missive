from os import environ, path
from dotenv import load_dotenv

basedirectory = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedirectory, '.env'))

class Config():
    pass

class ConfigDev(Config):
    SQLALCHEMY_DATABASE_URI = environ.get("DEV_DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = environ.get("DEV_SECRET_KEY")
    DEBUG = True
    TESTING = True


class ConfigTest(Config):
    DEBUG = True
    TESTING = True


class ConfigProd(Config):
    DEBUG = False
    TESTING = False