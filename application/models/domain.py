# coding: utf-8
from datetime import datetime
from ._base import db
from .base import Base




class Domain(Base):
    name = db.Column(db.String(50), unique=True)
    url = db.Column(db.Unicode(128), unique=True)
    #products = db.relationship('Product', backref='domains')
    #services = db.relationship('Service', backref='domains')


    def __repr__(self):
        return '%s' % self.url