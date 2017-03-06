# coding: utf-8
from flask_admin import Admin, AdminIndexView, form
from flask import render_template, Blueprint, flash
from flask_admin.contrib.sqla import ModelView
from ..models import Source, Profile, Image, Address, Property, Country, City, Address, Organisation, Contact, Role, Domain, Page, User, db
from flask_security import current_user, login_required
from flask import redirect, url_for, request
from flask_admin import helpers as admin_helpers
from flask import abort, session
from flask_admin import BaseView, expose
from flask_admin.menu import MenuLink
from flask_admin.contrib.sqla.ajax import QueryAjaxModelLoader
from ..utils.babel import babel
from flask_admin.contrib.fileadmin import FileAdmin
from flask_admin.actions import action
from sqlalchemy import func, distinct
from datetime import datetime, date, time
import os
import os.path as op
from flask_admin.form.rules import Field
from wtforms.fields import PasswordField, StringField, TextAreaField
from flask_security import utils
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from flask_admin.form.widgets import Select2Widget
from sqlalchemy import or_, and_
from wtforms.ext.sqlalchemy.fields import QuerySelectField, QuerySelectMultipleField

class HandlingView(ModelView):
    list_template = 'admin/realtime.html'
    column_default_sort = ('id', True)
    column_display_pk = True
    column_list = ('source', 'accepted_by', 'delegated_by', 'message')
    form_columns = ('source', 'message')
    column_labels = dict(source='Источник',accepted_by='Принял', delegated_by='Получил', message='Сообщение')
    form_overrides = {
    'message': TextAreaField,
    'сообщения': QueryAjaxModelLoader('Источник', db.session, Source, fields=['id'], page_size=10)
    }

    form_widget_args = {
    'message': {
        'rows': 5,
        'style': 'font-family: monospace;'
        }
    }
    can_delete = False
    can_edit = False
    create_modal = True

class UserView(ModelView):
    column_labels = dict(first_name='Имя',last_name='Фамилия')
    column_list = ('first_name', 'last_name', 'email')
    form_columns = ('first_name', 'last_name', 'email')
    can_delete = False
    can_edit = False
    create_modal = True
    column_editable_list = ('first_name', 'last_name', 'email')



class ModelMaster(UserView):

    def is_accessible(self):
        print(current_user.roles)
        return current_user.is_authenticated and current_user.has_role('master')

    def inaccessible_callback(self, name, **kwargs):
        # redirect to login page if user doesn't have access
        return redirect(url_for('security.login', next=request.url))

    '''
    def get_query(self):
        return super(ModelMaster, self).get_query().filter(
            User.city == current_user.city,
            User.propertys.any(Property.name.in_(['Лид', 'Контакт'])), 
            User.contacted.any(User.id == current_user.id),
            ~User.contacted.any())
    '''

    def get_query(self):
        return (
            self.session.query(
                User,
                Profile
            ).filter(Profile.user == current_user.id
            ).filter(Profile.city == Profile.city
            ).filter(Profile.propertys.any(Property.name.in_(['Лид', 'Контакт']))
            ).filter(or_(Profile.contacted.any(Profile.id == current_user.id), ~Profile.contacted.any()))
        )




class MasterUserView(ModelMaster):
    form_excluded_columns = ['password', 'роль']