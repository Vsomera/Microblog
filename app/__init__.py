# script creates the application object as an instance of Flask (initiates flask)
from flask import Flask
from config import Config # applies config.py 

app = Flask(__name__) 
app.config.from_object(Config)

from app import routes

if __name__ == '__init__':
    app.debug = True
    app.run()