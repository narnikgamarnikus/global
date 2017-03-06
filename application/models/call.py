# coding: utf-8
from datetime import datetime
from ._base import db
from .base import *


class Call(Base):
    manager = db.Column(db.String(50))
    direction = db.Column(db.String(50))
    phone = db.Column(db.String(50))
    name = db.Column(db.String(50))
    duration = db.Column(db.String(50))
    noreply = db.Column(db.String(50))
    tags = db.Column(db.String(50))
    note = db.Column(db.String(50))



