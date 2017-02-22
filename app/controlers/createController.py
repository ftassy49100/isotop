from flask import render_template, flash, redirect, session, url_for, request, g
from app import app, db, lm
from app.forms import LoginForm, CreateFolderForm
from app.models import user
from flask_login import login_user, logout_user, current_user, login_required


@app.route('/create/folder', methods=['GET', 'POST'])
def createFolder():
    if g.user is not None and g.user.is_authenticated:
        return redirect(url_for('login'))
    form = CreateFolderForm()
    if form.validate_on_submit():
        session['remember_me'] = form.remember_me.data
        g.user = load_user(1)
        return redirect('/index')
    return render_template('create/folder.html', title='New Folder', form=form)
