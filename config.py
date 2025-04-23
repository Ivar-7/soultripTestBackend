import os

class Config:
    SECRET_KEY = os.urandom(24)  # In production, use a fixed secret key
    SQLALCHEMY_DATABASE_URI = 'sqlite:///users.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False