from flask import render_template, flash, redirect, session, url_for, request, g
from app import app, db, lm, models
from app.forms import LoginForm
from app.models.user import User
from app.models.qualityFolder import QualityFolder
from flask_login import login_user, logout_user, current_user, login_required
import createController
import mainController


@lm.user_loader
def load_user(id_user):
    return User.query.get(int(id_user))


@app.before_request
def before_request():
    g.user = current_user


@app.route('/')
@app.route('/folder/<folder_id>')
def see_folder(folder_id):
    folder = QualityFolder.query.filter_by(id=folder_id).first()
    if folder == None:
        flash('Folder %s not found.' % folder_id)
        return redirect(url_for('index'))
    return render_template('folder.html', title="Folder "+str(folder.id), user=g.user, folder=folder)
