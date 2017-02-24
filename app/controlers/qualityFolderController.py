from flask import render_template, flash, redirect, session, url_for, request, g
from app import app, db, lm, models
from app.forms import CreateCurativeActionForm, CreateCorrectiveActionForm, CreatePreventiveActionForm
from app.models.user import User
from app.models.qualityFolder import QualityFolder
from flask_login import login_user, logout_user, current_user, login_required
import createController
import mainController


@app.before_request
def before_request():
    g.user = current_user


@app.route('/')
@app.route('/folders/<int:folder_id>')
def see_folder(folder_id):
    folders = []
    folder = QualityFolder.query.filter_by(id=folder_id).first()
    folders.append(folder)
    if folder == None:
        flash('Folder %s not found.' % folder_id)
        return redirect(url_for('index'))
    return render_template('folder.html', title="Folder " + str(folder.id), user=g.user, folders=folders)


@app.route('/folders/<nickname>')
def folders_of_user(nickname):
    user = User.query.filter_by(nickname=nickname).first()
    folders = QualityFolder.query.filter_by(opened_by_id=user.id)
    for folder in folders:
        folder.preventive_a_form = CreatePreventiveActionForm()
        print folder.preventive_a_form
    return render_template('folder.html', title="Folders of " + user.firstname + ' ' + user.lastname, folders=folders)
