from flask_restx import Namespace, Resource
from datetime import datetime


api = Namespace('health', description='Health check operations')

@api.route('/')
class healthApi(Resource):
    def get(self):
        return [{"status": "OK", "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}]

@api.route('/deepcheck')
class deepHealthApi(Resource):
    def get(self):
        return [{"status": "OK"}]