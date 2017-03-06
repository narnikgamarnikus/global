from flask_potion import Api, ModelResource
from ..controllers.api import CallResource
api = Api()

api.add_resource(CallResource)