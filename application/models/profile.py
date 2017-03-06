# coding: utf-8
from datetime import datetime
from ._base import *
from .base import *


profile_images = db.Table('profile_images', 
    db.Column('users_ids', db.Integer(), db.ForeignKey('profile.id')),
    db.Column('images_ids', db.Integer(), db.ForeignKey('image.id'))
)

profile_contacts = db.Table('profile_contacts',
    db.Column('users_ids', db.Integer, db.ForeignKey('profile.id')),
    db.Column('contacts_ids', db.Integer, db.ForeignKey('user.id'))
)

profile_addresses = db.Table('profile_addresses', 
    db.Column('users_ids', db.Integer(), db.ForeignKey('profile.id')),
    db.Column('addresses_ids', db.Integer(), db.ForeignKey('address.id'))
)

profile_domains = db.Table('profile_domains', 
    db.Column('users_ids', db.Integer(), db.ForeignKey('profile.id')),
    db.Column('domains_ids', db.Integer(), db.ForeignKey('domain.id'))
)

profile_propertys = db.Table('profile_propertys', 
    db.Column('users_ids', db.Integer(), db.ForeignKey('profile.id')),
    db.Column('propertys_ids', db.Integer(), db.ForeignKey('property.id'))
)

profile_users = db.Table('profile_users', 
    db.Column('users_ids', db.Integer(), db.ForeignKey('profile.id')),
    db.Column('profiles_ids', db.Integer(), db.ForeignKey('user.id'))
)

profile_handlings = db.Table('profile_handlings', 
    db.Column('users_ids', db.Integer(), db.ForeignKey('profile.id')),
    db.Column('handlings_ids', db.Integer(), db.ForeignKey('handling.id'))
)

class Profile(Base):
    user = db.Column(db.Integer, db.ForeignKey('user.id'), unique=True)
    avatar = db.Column(db.Integer, db.ForeignKey('image.id'))
    city = db.Column(db.Integer, db.ForeignKey('city.id'))
    images = db.relationship('Image', secondary=profile_images,
        backref=db.backref('images'))
    handlings = db.relationship('Handling', 
		secondary=profile_handlings,
         backref=db.backref('users'))
    contacts = db.relationship(
        'Profile', lambda: profile_contacts,
        primaryjoin=lambda: Profile.id == profile_contacts.c.users_ids,
        secondaryjoin=lambda: Profile.id == profile_contacts.c.contacts_ids,
        backref='contacted')
    adresses = db.relationship('Address', secondary=profile_addresses,
        backref=db.backref('usersz'))
    propertys = db.relationship('Property', secondary=profile_propertys,
        backref=db.backref('propertys_users'))
    domains = db.relationship('Domain', secondary=profile_domains,
        backref=db.backref('users_users'))
    organisations = db.relationship('Organisation', backref='users_organisations')
    activities = db.relationship('Activity', backref='users_activities')
    is_master = db.Column(db.Boolean())

    def __repr__(self):
        return '%s' % self.user
