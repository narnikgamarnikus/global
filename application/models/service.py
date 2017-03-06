# coding: utf-8
from datetime import datetime
from ._base import db
from .base import *


class Service(Base):
    name = db.Column(db.String(50), unique=True)
    domains = db.Column(db.String(50))

    def __repr__(self):
        return '<Service %s>' % self.name
