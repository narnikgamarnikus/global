from ._base import db
from sqlalchemy.exc import IntegrityError, InterfaceError
from flask import flash
from sqlalchemy import event
from sqlalchemy.event import listen
from sqlalchemy.orm.interfaces import MapperExtension
from ..utils.redis import redis_store
from sqlalchemy import inspect
from sqlalchemy.ext.declarative import as_declarative, declared_attr
from pickle import dumps, loads

@as_declarative()
class BaseExtension(MapperExtension):
    """Base entension class for all entities """

    def after_insert(self, mapper, connection, instance):
        row = instance.query.filter_by(id = instance.id).first()
        payload = {'model': instance.__class__.__name__, 'data': instance.id, 'type': 'INSERT', 'row': row}
        redis_store.publish('realtime', dumps(payload))


    def after_update(self, mapper, connection, instance):
        row = instance.query.filter_by(id = instance.id).first()
        payload = {'model': instance.__class__.__name__, 'data': instance.id, 'type': 'UPDATE', 'row': row}
        redis_store.publish('realtime', dumps(payload))


    def after_delete(self, mapper, connection, instance):
        row = instance.query.filter_by(id = instance.id).first()
        payload = {'model': instance.__class__.__name__, 'data': instance.id, 'type': 'DELETE', 'row': row}
        redis_store.publish('realtime', dumps(payload))



class Base(db.Model):

    __abstract__ = True
    __mapper_args__ = { 'extension': BaseExtension() }
    
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    modified_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    
    @classmethod
    def create(cls,**kwargs):
        c = cls(**kwargs)
        db.session.add(c)
        try:
            db.session.commit()
            flash((c.__tablename__).capitalize() + u' created successfully!', 'success')
        except IntegrityError:
            db.session.rollback()
            flash((c.__tablename__).capitalize() + u' created failed!' + u' IntegrityError', 'error')
            print('IntegrityError')
        except InterfaceError:
            db.session.rollback()
            flash((c.__tablename__).capitalize() + u' created failed!' + u' InterfaceError', 'error')
            print('InterfaceError')
        return c


    def __repr__(self):
        mapper = inspect(self).mapper
        ent = []
        object_data = {col.key: getattr(self, col.key) if not col.key == 'created_at' and not col.key == 'password' and not col.key == 'modified_at' else None  for col in mapper.column_attrs}
        '''
        for col in mapper.column_attrs:
            ent.append("{0}={1}".format(col.key, getattr(self, col.key)))
        return "<{0}(".format(self.__class__.__name__) + ", ".join(ent) + ")>"
        '''
        return "{0}".format(object_data)
        #return "{0}".format(self.id)