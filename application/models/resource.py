# coding: utf-8
from datetime import datetime
from ._base import *
from .base import *

class Resource(Base):
    name = db.Column(db.String(50), unique=True)
    url = db.Column(db.String(50), unique=True)
    pages = db.relationship('Page', backref='resources_pages')


    def __repr__(self):
        return '<Resource %s>' % self.name
