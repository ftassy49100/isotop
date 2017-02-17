from flask import render_template, flash, redirect, session, url_for, request, g
from app import app, db, lm, models
from app.forms import LoginForm
from app.models import user
from flask_login import login_user, logout_user, current_user, login_required
import createController

@lm.user_loader
def load_user(id):
	return models.user.User.query.get(int(id))

@app.before_request
def before_request():
	g.user = current_user

@app.route('/')
@app.route('/index')
def index():
	user = g.user
	posts = [{'author':{'nickname':'John'}, 'body':'Beautiful day in Portland !'},
		{'author': {'nickname':'Emilie'}, 'body':'The Avengers movie was cool'}]
	return render_template('index.html', title="Home", user=user, posts = posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
	if g.user is not None and g.user.is_authenticated:
		return redirect(url_for('index'))
	form = LoginForm()
	if form.validate_on_submit():
		session['remember_me'] = form.remember_me.data
		session['nickname'] = form.nickname.data
		g.user = load_user(session['nickname'])
		return redirect(request.args.get('next') or url_for('index'))
	return render_template('login.html', title='Sign In', form=form, user=g.user)

@app.route('/logout')
def logout():
	logout_user()
	return redirect(url_for('index'))

