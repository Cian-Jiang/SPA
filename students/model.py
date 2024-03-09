from flask_mongoengine import Document
from mongoengine.fields import StringField, IntField

class Student(Document):
    name = StringField(required=True, max_length=50)
    # age = IntField
    username = StringField(required=True, max_length=50,unique=True)
    password = StringField(required=True, max_length=50)

    # def __init__(self, name, password,username):
    #     self.name = name
    #     self.password = password
    #     self.username = username

    def to_dick(self):
        return {
            "id": str(self.id),
            "username": self.username,
            "name": self.name
        }
