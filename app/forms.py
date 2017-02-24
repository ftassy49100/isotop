from flask_wtf import Form
from wtforms import StringField, BooleanField, SelectField, TextAreaField, RadioField, DateTimeField
from wtforms.validators import DataRequired
from wtforms.ext.sqlalchemy.orm import model_form

from app import db
from app.models.user import User
from app.models.anomalyType import AnomalyType
from app.models.topic import Topic


class LoginForm(Form):
    nickname = StringField('nickname', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)


class CreateFolderForm(Form):
    opened_by = SelectField('Opened By: ', choices=User.form_list())
    anomaly_type = SelectField('Anomaly Type: ', choices=AnomalyType.form_list())
    topic = SelectField('Topic: ', choices=Topic.form_list())
    report = TextAreaField('Report: ')
    risk_level = RadioField('Risk Level: ', choices=[('1', '1'), ('2', '2'), ('3', '3')])
    risk_occurrence = RadioField('Risk Occurrence: ', choices=[('1', '1'), ('2', '2'), ('3', '3')])


class CreateCorrectiveActionForm(Form):

    pilote = SelectField('Pilote: ', choices=User.form_list())
    cause = TextAreaField('Cause: ')
    to_do = TextAreaField('To do: ')
    defined_by = SelectField('Defined by: ', choices=User.form_list())
    led_by = SelectField('Led by: ', choices=User.form_list())
    set_up_by = SelectField('Set up by: ', choices=User.form_list())
    predicted_date = DateTimeField('Date objective: ')


class CreatePreventiveActionForm(Form):

    pilote = SelectField('Pilote: ', choices=User.form_list())
    cause = TextAreaField('Cause: ')
    to_do = TextAreaField('To do: ')
    defined_by = SelectField('Defined by: ', choices=User.form_list())
    led_by = SelectField('Led by: ', choices=User.form_list())
    set_up_by = SelectField('Set up by: ', choices=User.form_list())
    predicted_date = DateTimeField('Date objective: ')


class CreateCurativeActionForm(Form):

    accountant = SelectField('Accountant: ', choices=User.form_list())
    analysis = TextAreaField('Analysis: ')
    immediate = BooleanField('Immediate action: ', validators=[DataRequired()])
    consequences = TextAreaField('Consequences: ')
    notes = TextAreaField('Notes: ')
    predicted_date = DateTimeField('Date objective:')
