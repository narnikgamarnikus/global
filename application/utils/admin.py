# coding: utf-8
from flask_admin import Admin, AdminIndexView, form
from flask import render_template, Blueprint, flash
from flask_admin.contrib.sqla import ModelView
from ..models import Page, Resource ,Source, Handling, Image, Address, Property, Country, City, Address, Organisation, Contact, Role, Domain, Page, User, db
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
from wtforms.ext.sqlalchemy.fields import QuerySelectField, QuerySelectMultipleField
from flask_admin.form.widgets import Select2Widget
from wtforms import widgets
from ..modules.user import MasterUserView, HandlingView
from wtforms.ext.sqlalchemy.orm import model_form
from flask_wtf import Form
from wtforms import validators
from flask_admin.form import SecureForm


static_path = op.join(op.dirname(__file__), '../static')
page_path = op.join(op.dirname(__file__), '../pages')
avatar_path = op.join(op.dirname(__file__), '../static/img/avatars/')


'''



@babel.localeselector
def get_locale():
    override = request.args.get('lang')

    if override:
        session['lang'] = override

    return session.get('lang', 'ru')



class BaseView(ModelView):


    def is_accessible(self):
        print(current_user.roles)
        return current_user.is_authenticated and current_user.has_role('superadmin')

    def inaccessible_callback(self, name, **kwargs):
        # redirect to login page if user doesn't have access
        return redirect(url_for('security.login', next=request.url))
	



class Adresses(BaseView):
    column_display_all_relations = True
    

class DomainView(BaseView):
	column_display_all_relations = True



class MyAdmin(FileAdmin):
    
    def is_accessible(self):
        print(current_user.roles)
        return current_user.is_authenticated and current_user.has_role('superadmin')

    
    def inaccessible_callback(self, name, **kwargs):
        # redirect to login page if user doesn't have access
        return redirect(url_for('security.login', next=request.url))

	   

    editable_extensions = ('md', 'html', 'txt', 'js', 'css')


class MyLastAdmin(FileAdmin):

    def is_accessible(self):
        print(current_user.roles)
        return current_user.is_authenticated and current_user.has_role('superadmin')

    def inaccessible_callback(self, name, **kwargs):
        # redirect to login page if user doesn't have access
        return redirect(url_for('security.login', next=request.url))

	
    editable_extensions = ('md', 'html', 'txt', 'js', 'css')

'''

class MyHomeView(AdminIndexView):
    @expose('/')
    def index(self):
        if not current_user.is_authenticated:
            return redirect(url_for('security.login'))

        if current_user.has_role('master'):
            print('i am a master')
            current_week = len(
                Profile.query.filter(
                    Profile.propertys.any(
                    Property.name == 'Лид')
                    ).filter(Profile.user == current_user.id
                    ).filter(func.strftime('%W', User.created_at) == ('0' + str(datetime.now().isocalendar()[1]))
                    ).filter(Profile.city == Profile.city
                    ).filter(Profile.contacted.any(Profile.user == current_user.id)).all())
            print(current_week)
            previous_week = len(
                Profile.query.filter(
                    Profile.propertys.any(
                    Property.name == 'Лид')
                    ).filter(Profile.user == current_user.id
                    ).filter(func.strftime('%W', User.created_at) == ('0' + str(datetime.now().isocalendar()[1]-1))
                    ).filter(Profile.city == Profile.city
                    ).filter(Profile.contacted.any(Profile.user == current_user.id)).all())
            print(previous_week)

            if previous_week == 0 and current_week == 0:
                delta = 0
            elif previous_week == 0:
                delta = round((((float(previous_week)/float(current_week))+1)*100), 2)
            else:
                delta = round((((float(current_week)/float(previous_week))-1)*100), 2)


        elif current_user.has_role('superadmin'):
            arg1 = 'Hello'
            asd = User.query.get(1)
            year = '2018'
            month = '1'
            day = '1'
            time = '23:59:59'
            data = '{}-{}-{} {}'.format(year, month, day, time)
            newdata = '{}-{}-{} {}'.format((str(int(year)-25)), month, day, time)
            #print(newdata)
            print(asd.created_at.isocalendar()[1])
            print(str(int(datetime.now().isocalendar()[1])))
            if asd.created_at.strftime('%V') == ('0' + str(int(datetime.now().isocalendar()[1]))):
                print('yeah!')

            print(asd.created_at.strftime('%V'))
            print('0' + str(int(datetime.now().isocalendar()[1])))
            weekly_contacts = User.query.filter(db.func.date(User.created_at)<=data, 
                db.func.date(User.created_at)>=newdata).count()
            current_week = len(User.query.filter(func.strftime('%W', User.created_at) == ('0' + str(datetime.now().isocalendar()[1]))).all())
            previous_week = len(User.query.filter(func.strftime('%W', User.created_at) == ('0' + str(datetime.now().isocalendar()[1]-1))).all())
            
            #print(newquery)
            print(current_week)
            print(previous_week)
            if previous_week == 0 and current_week == 0:
                delta = 0
            elif previous_week == 0:
                delta = round((((float(previous_week)/float(current_week))+1)*100), 2)
            else:
                delta = round((((float(current_week)/float(previous_week))-1)*100), 2)


            #fromto_contacts = len(User.query.filter(User.created_at.between(newdata, data)).all())
            #print(fromto_contacts)
            #print(weekly_contacts)            

        
        
        return self.render('admin/roles/superadmin.html',
                current_week='123',#current_week,
                previous_week='123',#previous_week,
                delta='123')#delta)
        
'''
class MyModelAdmin(ModelView):

    def is_accessible(self):
        print(current_user.roles)
        return current_user.is_authenticated and current_user.has_role('superadmin')

    def inaccessible_callback(self, name, **kwargs):
        # redirect to login page if user doesn't have access
        return redirect(url_for('security.login', next=request.url))

class ProfileView(MyModelAdmin):
    column_display_all_relations = True



class UserView(MyModelAdmin):
    column_display_all_relations = True
    list_template = 'admin/realtime.html'
    column_default_sort = ('id', True)
    column_display_pk = True

    #form_excluded_columns = ['password', 'роль', 'propertys', 'projects', 'organisations', 'contacts']
    #column_exclude_list = ('password')
    #searchable_columns = ('last_name','first_name', 'email')
    

    def _list_thumbnail(view, context, model, name):
        if not model.path:
            return ''

        return Markup('<img src="%s" style="width: 250px; height: 250px">' % url_for('static',
            filename=form.thumbgen_filename(model.path)))



    column_formatters = {
    'path': _list_thumbnail
    }
    
    


    def scaffold_form(self):

        # Start with the standard form as provided by Flask-Admin. We've already told Flask-Admin to exclude the
        # password field from this form.
        form_class = super(UserView, self).scaffold_form()

        # Add a password field, naming it "password2" and labeling it "New Password".
        form_class.password1 = PasswordField('Старый пароль')
        form_class.password2 = PasswordField('Подтвердите')
        form_class.password3 = PasswordField('Новый пароль')
        form_class.problem = TextAreaField('Проблема')
        #form_class.c = QuerySelectMultipleField(label='Картинки', query_factory=lambda: Profile.query.filter(Profile.propertys.any(Property.name == 'Лид'), ~Profile.contacted.any()).all())
        return form_class

        
    def on_model_change(self, form, model):
        if not Profile.query.filter(Profile.user == model.id).first():
            #self.is_created=True
            Profile.create(user=model.id)

            #roles = Role.query.filter(Role.users.any(roles_users.c.user_id == model.id)).all()
            #print('roles is :' + str(roles))
            #propertys = Property.query.all()

            #Property.propertys_users.contains(model.id)
            #print('123')
        
        if model.password1 != model.password2:
            print(model.password1)
            print(model.password1)
            flash('Новые пароли не совпадают!')
            print('Новые пароли не совпадают!')
            # If the password field isn't blank...
        elif model.password1 and model.password2 == model.password:
            flash('Новый и старый пароль совпадают!')
            print('Новый и старый пароль совпадают!')
        else:
            if len(model.password3):

                # ... then encrypt the new password prior to storing it in the database. If the password field is blank,
                # the existing password in the database will be retained.
                model.password = utils.encrypt_password(model.password3)



    #form_excluded_columns = ['password', 'created_at', 'modified_at', 'confirmed_at', 'current_login_at', 'last_login_at', 'last_login_ip', 'current_login_ip', 'last_login_ip']
    #column_exclude_list = ('password', 'created_at', 'modified_at', 'password', 'confirmed_at', 'current_login_at', 'last_login_at', 'current_login_ip', 'last_login_ip', 'organisations', 'contacts', 'projects', 'activities')
    #form_ajax_refs = {
    #'user': QueryAjaxModelLoader('user', db.session, User, fields=['email'], page_size=10)
    #}
    column_labels = dict(roles='Роль',first_name='Имя', last_name='Фамилия', email='Email', login_count='Количество посещений')
    edit_modal = True
    create_modal = True
    details_modal = True
    #column_editable_list = ('first_name', 'last_name', 'email')
    list_template = 'admin/model/list.html'
	#form_edit_rules = [
	#CustomizableField('email', field_args={
	#	'readonly': True
	#	})]
	#
    '''


'''
class HandlingView(HandlingView):
    column_display_all_relations = True
'''

admin = Admin(index_view=MyHomeView(menu_icon_type='ti', menu_icon_value='ti-home'),
category_icon_classes={
	'CRM': 'ti ti-money'
	}
	)

'''
admin = Admin(name='CMS', 
    template_mode='bootstrap3')

admin.add_view(ModelView(User, db.session))
''' 
#admin.add_view(MasterUserView(User, db.session, endpoint='userss', category='CRM', name='Лиды', menu_icon_type='ti', menu_icon_value='ti-link'))

#admin.add_view(DomainView(Role, db.session, category='CRM', name='Роли', menu_icon_type='ti', menu_icon_value='ti-link'))
#admin.add_view(UserView(User, db.session, category='CRM', name='Юзеры', menu_icon_type='ti', menu_icon_value='ti-user'))
#admin.add_view(UserView(Profile, db.session, category='CRM', name='Профили', menu_icon_type='ti', menu_icon_value='ti-user'))
#admin.add_view(UserView(Source, db.session, category='CRM', name='Источники', menu_icon_type='ti', menu_icon_value='ti-user'))
#admin.add_view(HandlingView(Handling, db.session, category='CRM', name='Касания', menu_icon_type='ti', menu_icon_value='ti-user'))
#admin.add_view(UserView(Role, db.session, category='CRM', name='Роли', menu_icon_type='ti', menu_icon_value='ti-user'))
#admin.add_view(UserView(Resource, db.session, category='CMS', name='Ресурсы', menu_icon_type='ti', menu_icon_value='ti-user'))
#admin.add_view(UserView(Page, db.session, category='CMS', name='Страницы', menu_icon_type='ti', menu_icon_value='ti-user'))

#admin.add_view(DomainView(Domain, db.session, category='CRM', name='Домены', menu_icon_type='ti', menu_icon_value='ti-server'))
#admin.add_view(BaseView(Contact, db.session, category='CRM', name='Контакты', menu_icon_type='ti', menu_icon_value='ti-target'))
#admin.add_view(BaseView(Property, db.session, category='CRM', name='Свойства', menu_icon_type='ti', menu_icon_value='ti-property'))

#admin.add_view(BaseView(Organisation, db.session, category='CRM', name='Организации', menu_icon_type='ti', menu_icon_value='ti-stamp'))
#admin.add_view(Adresses(Address, db.session, category='CRM', name='Адреса', menu_icon_type='ti', menu_icon_value='ti-map-alt '))
#admin.add_view(Adresses(City, db.session, category='CRM', name='Города', menu_icon_type='ti', menu_icon_value='ti-map-alt '))
#admin.add_view(Adresses(Country, db.session, category='CRM', name='Страны', menu_icon_type='ti', menu_icon_value='ti-map-alt '))

#admin.add_view(BaseView(Page, db.session, category='CMS', name='Страницы', menu_icon_type='ti', menu_icon_value='ti-files'))
#admin.add_view(ModelView(Resource, db.session, category='CMS', name='Ресурсы', menu_icon_type='ti', menu_icon_value='ti-link'))
#admin.add_view(MyAdmin(static_path, '/static/', category='CMS', name='Файлы', menu_icon_type='ti', menu_icon_value='ti-folder'))
#admin.add_view(MyLastAdmin(page_path, '/pages/', category='CMS', name='Шаблоны', menu_icon_type='ti', menu_icon_value='ti-layout'))
#admin.add_link(MenuLink(name='Login', category='', endpoint="security.login"))