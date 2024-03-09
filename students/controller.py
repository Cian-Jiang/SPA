from flask_restx import Namespace, Resource
from flask import request
from students.model import Student
from students.schema import StudentSchema, StudentListSchema


# /students/...
api = Namespace('students', description='Students related operations')


@api.route('/')
class studentListApi(Resource):
    def get(self):
        students = list(Student.objects())
        return StudentListSchema.from_orm(students).dict(), 200



    def post(self):
        request_student = request.json
        student = Student(**request_student)
        student.save()
        return 'student created! id: ' + student.id, 201

    def delete(self):
        return 'delete student', 204

    def put(self):
        return 'update student', 200
