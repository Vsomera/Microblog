# script creates the application object as an instance of Flask (initiates flask)

from flask import Flask

app = Flask(__name__) # __name__ is the name of the name of the script (__init__)

from app import routes

