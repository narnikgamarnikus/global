# coding: utf-8
from datetime import datetime
from ._base import *
from .base import *
from sqlalchemy_utils import ChoiceType
from sqlalchemy import Enum


class Source(Base):
	#type = db.Column(db.Integer, db.ForeignKey('type.id'), nullable=False)
	#subtype = db.Column(db.Integer, db.ForeignKey('type.id'), nullable=False)

	def __repr__(self):
		return '%s, %s' % (self.type, self.subtype)
