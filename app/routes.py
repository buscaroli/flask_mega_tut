from flask import render_template, flash, redirect, url_for
from flask_login import current_user, login_user, logout_user
from app import app
from app.forms import LoginForm
from app.models import User

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

@app.route('/login', methods=['GET', 'POST'])
def login():
    # if a user navigates to the /login endpoint but is authenticated
    # refer him back to the homepage
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = LoginForm()
   
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
            #  login_user will ser the current_user var to the user for the duration 
            #  of the session
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))
