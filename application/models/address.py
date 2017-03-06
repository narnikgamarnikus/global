# coding: utf-8
from datetime import datetime
from ._base import db
from .base import *

class Address(Base):
    name = db.Column(db.String(50), unique=True)
    index = db.Column(db.String(50))
    city = db.Column(db.ForeignKey('city.id'))


    def __repr__(self):
        return '%s, %s' % (self.city, self.name)
