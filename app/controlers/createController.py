from flask import render_template, flash, redirect, session, url_for, request, g
from datetime import datetime
from app import app, db, lm
from app.forms import LoginForm, CreateFolderForm
from app.models.user import User
from app.models.qualityFolder import QualityFolder
from app.models.anomalyType import AnomalyType
from app.models.topic import Topic
from flask_login import login_user, logout_user, current_user, login_required


@app.route('/create/folder', methods=['GET', 'POST'])
def createFolder():
    if g.user is not None and g.user.is_authenticated:
        return redirect(url_for('login'))
    form = CreateFolderForm()
    if form.validate_on_submit():
        qf = QualityFolder(risk_level=int(form.risk_level.data), risk_occurrence=int(form.risk_occurrence.data),
                           opening_date=datetime.now(), report=form.report.data)
        at = AnomalyType.query.get(int(form.anomaly_type.data))
        at.quality_folders.append(qf)
        opened_by = User.query.get(int(form.opened_by.data))
        opened_by.quality_folders.append(qf)
        topic = Topic.query.get(int(form.topic.data))
        topic.quality_folders.append(qf)

        db.session.add(qf)
        db.session.add(at)
        db.session.add(opened_by)
        db.session.add(topic)
        db.session.commit()
        flash('Folder %s created.' % qf.id)
        redirect(url_for('see_folder', title='Folder ' + str(qf.id), folder=qf))
    return render_template('create/folder_creation.html', title='New Folder', form=form)
