# coding: utf-8
from flask import Blueprint, render_template
from flask_potion import Api, ModelResource
from ..models import Call

bp = Blueprint('api', __name__)

class CallResource(ModelResource):
    class Meta:
        model = Call
