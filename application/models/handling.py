# coding: utf-8
from datetime import datetime
from ._base import *
from .base import *
from .profile import *


class Handling(Base):

	type = db.Column(db.Integer, db.ForeignKey('type.id'), nullable=False) 
	message = db.Column(db.String(500))
	end_data = db.Column(db.DateTime)
	source = db.Column(db.Integer, db.ForeignKey('source.id'))
	#accepted_by = db.Column(db.Integer, db.ForeignKey('profile.id'), unique=True)
	#delegated_by = db.Column(db.Integer, db.ForeignKey('profile.id'), unique=True)


	def __repr__(self):
		return '%s' % (self.message)
