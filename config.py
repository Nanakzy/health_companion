import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'ubuntu'
    MYSQL_PASSWORD = 'healthapp'
    MYSQL_DB = 'health_companion'
