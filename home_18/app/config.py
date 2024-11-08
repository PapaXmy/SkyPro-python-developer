class Config(object):
    """Класс конфигурации приложения"""

    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///./movies.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

