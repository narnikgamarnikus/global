# coding: utf-8
from .default import Config


class ProductionConfig(Config):
    # App config
    SECRET_KEY = "\xb5\xb3}#\xb7A\xcac\x9d0\xb6\x0f\x80z\x97\x00\x1e\xc0\xb8+\xe9)\xf0}"
    PERMANENT_SESSION_LIFETIME = 3600 * 24 * 7
    SESSION_COOKIE_NAME = 'flask-global_session'

    # Site domain
    SITE_DOMAIN = "ремонт-пк-и-ноутбуков.бел"

    # Db config
    SQLALCHEMY_DATABASE_URI = "postgresql://global@localhost/global"

    # Sentry
    SENTRY_DSN = 'https://ca1ac05e95e24998950500556f26f08a:644a790621d3435785eab71f33039983@sentry.io/138247'
