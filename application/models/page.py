# coding: utf-8
from datetime import datetime
from ._base import db
from .base import * 

class Page(Base):
    name = db.Column(db.String(50), unique=True)
    url = db.Column(db.String(50), unique=True)
    resource = db.Column(db.Integer, db.ForeignKey('resource.id'))

    def __repr__(self):
        return '<Page %s>' % self.name
