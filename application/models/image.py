# coding: utf-8
from datetime import datetime
from ._base import db
from .base import *


class Image(Base):
    name = db.Column(db.String(50))
    path = db.Column(db.Unicode(128))
    tags = db.relationship('Tag', backref='images_tags')
    product = db.Column(db.Integer, db.ForeignKey('product.id'))
    category = db.Column(db.Integer, db.ForeignKey('category.id'))
    user = db.Column(db.Integer, db.ForeignKey('user.id'))


    def __repr__(self):
        return '%s' % self.name