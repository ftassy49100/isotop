from flask import render_template, flash, redirect, session, url_for, request, g
from app import app, db, lm, models
from app.forms import LoginForm
from app.models.user import User
from flask_login import login_user, logout_user, current_user, login_required


@lm.user_loader
def load_user(nickname):
    return User.query.filter_by(nickname=nickname)


@app.before_request
def before_request():
    g.user = current_user


@app.route('/')
@app.route('/index')
def index():
    if session.get('nickname'):
        return render_template('index.html', title="Home", user=session['user'])
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    print session
    if session.get('nickname'):
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        session['remember_me'] = form.remember_me.data
        current_user = load_user(form.nickname.data)
        return redirect(request.args.get('next') or url_for('index'))
    return render_template('login.html', title='Sign In', form=form, user=g.user)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))
