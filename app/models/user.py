from app import db
from sqlalchemy.orm import relationship
from sqlalchemy import Table, Column, Integer, ForeignKey
import qualityFolder
import preventiveAction
import curativeAction
import correctiveAction


class User(db.Model):
    __tablename__ = 'it_user'
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(64))
    lastname = db.Column(db.String(64))
    nickname = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    # quality folders relationship#
    quality_folders = db.relationship('QualityFolder', backref='opened_by',
                                      lazy="dynamic")
    ###############################
    # curative actions relationship#
    curative_actions = db.relationship('CurativeAction', backref='accountant',
                                       lazy="dynamic")
    ###############################
    # corrective actions relationship#
    ca_pilote = db.relationship('CorrectiveAction', backref='pilote', foreign_keys="CorrectiveAction.pilot_id",
                                lazy="dynamic")
    ca_led_by = db.relationship('CorrectiveAction', backref='led_by', foreign_keys="CorrectiveAction.led_by_id",
                                lazy="dynamic")
    ca_defined_by = db.relationship('CorrectiveAction', backref='defined_by',
                                    foreign_keys="CorrectiveAction.defined_by_id",
                                    lazy="dynamic")
    ca_set_up_by = db.relationship('CorrectiveAction', backref='set_up_by',
                                   foreign_keys="CorrectiveAction.set_up_by_id",
                                   lazy="dynamic")
    #################################
    # preventive actions relationship#
    pa_pilote = db.relationship('PreventiveAction', backref='pilote', foreign_keys="PreventiveAction.pilot_id",
                                lazy="dynamic")
    pa_led_by = db.relationship('PreventiveAction', backref='led_by', foreign_keys="PreventiveAction.led_by_id",
                                lazy="dynamic")
    pa_defined_by = db.relationship('PreventiveAction', backref='defined_by',
                                    foreign_keys="PreventiveAction.defined_by_id",
                                    lazy="dynamic")
    pa_set_up_by = db.relationship('PreventiveAction', backref='set_up_by',
                                   foreign_keys="PreventiveAction.set_up_by_id",
                                   lazy="dynamic")

    #################################

    def __repr__(self):
        return '<User %r>' % (self.nickname)

    def get_id(self):
        try:
            return unicode(self.id)  # python 2
        except NameError:
            return str(self.id)  # python 3

    def is_anonymous(self):
        return False

    def is_active(self):
        return True

    def is_authenticated(self):
        return True

    @staticmethod  # return a list usable for forms
    def form_list():
        users = User.query.all()
        users_list = []
        for user in users:
            users_list.append((unicode(user.id), unicode(user.firstname + ' ' + user.lastname)))
        return users_list
