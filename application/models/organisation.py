# coding: utf-8
from datetime import datetime
from ._base import db
from .base import Base
from sqlalchemy import ForeignKey
from sqlalchemy.exc import IntegrityError
import sqlalchemy_utils
from sqlalchemy_utils import EmailType, ChoiceType



class Organisation(Base):

    name = db.Column(db.String(50), unique=True, nullable=False)
    address = db.Column(db.String(50))
    city = db.Column(db.Integer, db.ForeignKey('city.id'), nullable=False) 
    country = db.Column(db.Integer, db.ForeignKey('country.id'), nullable=False) 
    type = db.Column(db.Integer, db.ForeignKey('type.id'), nullable=False) 
    created_by = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False) 
    contacts = db.relationship('Contact', backref='Организации')
    activities = db.relationship('Activity', backref='Виды деятельности')

    '''
    @staticmethod
    def create(**kwargs):
        o = Organisation(**kwargs)
        db.session.add(o)
        try:
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
        return o
    '''
    
    def __repr__(self):
        return str(self.id)
