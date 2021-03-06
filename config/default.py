# coding: utf-8
import os


class Config(object):
    """Base config class."""
    # Flask app config
    DEBUG = False
    TESTING = False
    SECRET_KEY = "\xb5\xb3}#\xb7A\xcac\x9d0\xb6\x0f\x80z\x97\x00\x1e\xc0\xb8+\xe9)\xf0}"
    PERMANENT_SESSION_LIFETIME = 3600 * 24 * 7
    SESSION_COOKIE_NAME = 'global_session'


    # Root path of project
    PROJECT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

    # Site domain
    SITE_TITLE = "global"
    SITE_DOMAIN = "http://localhost:5000"
    WTF_CSRF_ENABLED = False

    # SQLAlchemy config
    # See:
    # https://pythonhosted.org/Flask-SQLAlchemy/config.html#connection-uri-format
    # http://docs.sqlalchemy.org/en/rel_0_9/core/engines.html#database-urls
    SQLALCHEMY_DATABASE_URI = ""
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Flask-DebugToolbar
    DEBUG_TB_INTERCEPT_REDIRECTS = False

    # Sentry config
    SENTRY_DSN = ''

    # Host string, used by fabric
    HOST_STRING = "root@185.87.193.188"



    REDIS_URL = "redis://@localhost:6379"
    #REDIS_HOST = "localhost"
    #REDIS_PASSWORD = "password"
    #REDIS_PORT = 5050

    # Flask_mail configuration
    MAIL_SERVER = "smtp.gmail.com"
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = 'narnikgamarnikus@gmail.com'  ## CHANGE THIS
    MAIL_PASSWORD = 'nikogdanesdavatsa'

    # Flask_security configuration
    SECURITY_EMAIL_SENDER = 'narnikgamarnikus@gmail.com'
    SECURITY_PASSWORD_HASH = 'pbkdf2_sha512'
    SECURITY_PASSWORD_SALT = 'something_super_secret_change_in_production'

    SECURITY_CONFIRMABLE = False
    SECURITY_REGISTERABLE = True
    SECURITY_RECOVERABLE = True
    SECURITY_TRACKABLE = True
    SECURITY_PASSWORDLESS = False
    SECURITY_CHANGEABLE = True
    SECURITY_URL_PREFIX = '/account'
    SECURITY_POST_LOGIN_VIEW = '/admin'
