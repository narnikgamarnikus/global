# coding: utf-8
from datetime import datetime
from ._base import db
from .base import *


class Call(Base):
    master = db.Column(db.String(50))
    client = db.Column(db.String(50))
    note = db.Column(db.String(50))


