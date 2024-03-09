from flask_restx import Namespace, Resource

api = Namespace('campus', description='Campus related operations')

@api.route('/')
class campusListApi(Resource):
    def get(self):
        return [{"id": 1,
                 "name": "Monash"},
                {"id": 2,
                 "name": "campus b"},
                {"id": 3,
                 "name": "campus c"}]
