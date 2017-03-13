# coding: utf-8
from ..models import Call
from flask_potion import Api, ModelResource, fields
from flask_potion.routes import ItemRoute
api = Api()


class CallResource(ModelResource):
    class Meta:
        model = Call

    '''
    @ItemRoute.GET('/calling')
    def greeting(self, call) -> fields.String():
        return "Hello, {}!".format(call.id)
	'''


api.add_resource(CallResource)