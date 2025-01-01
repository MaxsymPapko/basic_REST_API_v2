import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://postgres:mysecretpassword@db:5432/mydatabase')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
