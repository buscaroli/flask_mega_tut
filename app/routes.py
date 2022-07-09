from flask import render_template
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'John'}
    posts = [
        {
            'author': {'username': 'George'},
            'body': 'Hi there I am George!'
        },
        {
            'author': {'username': 'Clare'},
            'body': 'Hi there I am Clare!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)
