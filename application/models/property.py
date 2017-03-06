# coding: utf-8
from datetime import datetime
from ._base import *
from .base import *


class Property(Base):
    name = db.Column(db.String(50), unique=True)
    description = db.Column(db.String(150))

    def __repr__(self):
        return '%s' % self.name
