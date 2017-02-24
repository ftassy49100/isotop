from app import db
from sqlalchemy.orm import relationship
from sqlalchemy import Table, Column, Integer, ForeignKey
import attribute
import preventiveAction
import curativeAction
import correctiveAction
import topic


class QualityFolder(db.Model):
    """Core element of application ; linked to several users, corrective, curative and preventive actions, topic,
    and attributes.
    """
    __tablename__ = 'it_quality_folder'
    id = db.Column(db.Integer, primary_key=True)
    opened_by_id = db.Column(db.Integer, db.ForeignKey('it_user.id'))
    opening_date = db.Column(db.DateTime)
    anomaly_type_id = db.Column(db.Integer, db.ForeignKey('it_anomaly_type.id'))
    topic_id = db.Column(db.Integer, db.ForeignKey('it_topic.id'))
    report = db.Column(db.String(800))
    # attribute relationship#
    #owned_attributes_id = db.Column(db.Integer, db.ForeignKey('it_attribute.id'))
    #owned_attributes = relationship("Attribute", backref="quality_folder", cascade="all, delete-orphan",
    #                                single_parent=True)
    ########################
    risk_level = db.Column(db.Integer)
    risk_occurrence = db.Column(db.Integer)
    closing_date = db.Column(db.DateTime)
    # actions relationships##
    corrective_actions = db.relationship('CorrectiveAction', backref="quality_folder",
                                               cascade="all, delete-orphan", lazy="dynamic")
    preventive_actions = db.relationship('PreventiveAction', backref="quality_folder",
                                               cascade="all, delete-orphan", lazy="dynamic")
    curative_actions = db.relationship('CurativeAction', backref="quality_folder", cascade="all, delete-orphan",
                                             lazy="dynamic")
    ########################
    def __repr__(self):
        return '<Dossier %r>' % (self.id)

    def forms(self):
        self.forms = []
