from flask import render_template # module for returning html files to the browser
from app import app

# the browser will request either 2 of these URL's, flask will invoke the function and pass the return value as a response
@app.route("/")
@app.route("/index") # browser will make this request

def index():         # returns the string as a response
    user = {'username' : "Vsomera"}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body' : 'The avengers movie was so cool'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts) # passes title and user arguments to html file

