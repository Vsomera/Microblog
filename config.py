import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    # Genearates a secret signature (Flask will use it to protect against attacks)