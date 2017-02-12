# coding: utf-8
from flask import current_app
from application.models import User, Role, db
from itsdangerous import URLSafeSerializer, BadSignature
from flask_security import Security, SQLAlchemyUserDatastore


security = Security()
user_datastore = SQLAlchemyUserDatastore(db, User, Role) 


def encode(something):
    """Encode something with SECRET_KEY."""
    secret_key = current_app.config.get('SECRET_KEY')
    s = URLSafeSerializer(secret_key)
    return s.dumps(something)


def decode(something):
    """Decode something with SECRET_KEY."""
    secret_key = current_app.config.get('SECRET_KEY')
    s = URLSafeSerializer(secret_key)
    try:
        return s.loads(something)
    except BadSignature:
        return None
