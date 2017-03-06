# coding: utf-8
from datetime import datetime
from ._base import db
from .base import *


class City(Base):
	name = db.Column(db.String(50))
	country = db.Column(db.ForeignKey('country.id'))
	addresses = db.relationship('Address',
        backref=db.backref('Город в этой стране'))
	users = db.relationship('Profile',
        backref=db.backref('Город'))


	def __repr__(self):
		return '%s' % self.name
