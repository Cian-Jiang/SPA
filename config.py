from flask import Config
class Config(Config):
    APP_NAME = 'MyApp'
    enable_utc = True
    MONGODB_DB = 'api'
    MONGODB_HOST = '127.0.0.1'
    MONGODB_PORT = 27017
    MONGODB_USERNAME = 'root'
    MONGODB_PASSWORD = 'rootmongo'