# coding: utf-8
from datetime import datetime
from ._base import db
from .base import *


class Country(Base):
	name = db.Column(db.String(50), unique=True)
	cities = db.relationship('City',
        backref=db.backref('country_cities'))

	def __repr__(self):
		return '<Country %s>' % self.name
