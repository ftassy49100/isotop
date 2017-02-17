from flask_wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired
from wtforms.ext.sqlalchemy.orm import model_form
from app.models import qualityFolder

class LoginForm(Form):
	nickname = StringField('nickname', validators=[DataRequired()])
	remember_me = BooleanField('remember_me', default=False)

CreateFolderForm = model_form(qualityFolder.QualityFolder, Form)
