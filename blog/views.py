from flask_blog import app



@app.route('/')
@app.route('/index')
def index():
    return 'Hello World!'
    

"""
from flask import render_template, redirect
from author.form import RegisterForm


@app.route('/login')
def login():
    return "Hello, User!"
    
    
@app.route('/register', methods=('GET', 'POST'))
def register():
    form = RegisterForm()
    return render_template('author/register.html', form=form)
"""