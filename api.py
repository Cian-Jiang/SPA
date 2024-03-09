from flask import Flask
from config import Config
from flask_mongoengine import MongoEngine
from flask_restx import Api, Namespace
from students.controller import api as students_api
from campus.controller import api as campus_api
from health.controller import api as health_api


app = Flask(Config.APP_NAME)
app.config.from_object(Config)

# 使用flask_mongoengine连接数据库
db = MongoEngine(app)

# 使用flask_restx创建api
api = Api(app,
         # version='1.0', title='MyApp API', description='A simple API',
)
# 添加命名空间 /students/...
api.add_namespace(students_api)
# 添加命名空间 /campus/...
api.add_namespace(campus_api)
# 添加命名空间 /health/...
api.add_namespace(health_api)


@app.route('/')
def hello_world():  # put application's code here
    return '<p>Hello World!</p>'

# @app.route('/health')
# def hello():
#     return 'OK!'

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000, debug=True)
