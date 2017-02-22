from flask_wtf import Form
from wtforms import StringField, BooleanField, SelectField
from wtforms.validators import DataRequired
from wtforms.ext.sqlalchemy.orm import model_form

from app import db, models


class LoginForm(Form):
    nickname = StringField('nickname', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)


class CreateFolderForm(Form):
    nickname = StringField('nickname')
